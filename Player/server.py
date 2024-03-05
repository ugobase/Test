from flask import Flask,render_template, jsonify
import socket
import random
import requests

app = Flask(__name__) 

@app.route('/Player Server')
def player_server():
    return render_template("player_server.html")

@app.route("/health") 
def healthstatus():    
    return render_template('health.html')

@app.route('/hostname')
def hostname():
    return socket.gethostname()

@app.route('/hostnameIp')
def hostnameIp():
    return socket.gethostbyname(socket.gethostname())


master_url = "http://127.0.0.1:5002/master"
@app.route('/play')
def play():
    minimum = 1
    maximum = 1000
    guess = random.randint(minimum, maximum)
    game_history = []
    run = True

    while run:
        response = requests.get(f"{master_url}/{guess}").json()
        game_history.append((guess, response['answer']))

        if response["answer"] == 'Won!':
            return jsonify(answer="Player won!", game_history=game_history)

        if response["answer"] == 'Higher!':
            minimum = guess + 1
        else:
            maximum= guess - 1

        guess = random.randint(minimum, maximum)


if __name__== "__main__":
     app.run(debug=True, port=5000, host="0.0.0.0")



# # app = Flask(__name__)   # Special variable, name of the module. Flask knows where to look for their static files
# # @app.route("/")   # creating route. Type route in browser to go to different pages (Decorators). Handles backend and allows one write a function that returns info shown on webite for the route. Eg Contact and About pages
# # def home():    # / is the root page
# #     return "<h1>Hello World</h1>"
