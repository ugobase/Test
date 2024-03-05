from flask import Flask,render_template, jsonify
import socket
import random

app = Flask(__name__) 

@app.route('/Master Server')
def master():
    return render_template("/master_server.html")

@app.route("/health") 
def healthstatus():    
    return render_template("/health.html")

@app.route('/hostname')
def hostname():
    return socket.gethostname()

@app.route('/hostnameIp')
def hostnameIp():
    return socket.gethostbyname(socket.gethostname())

rnd = random.randint(1, 1000) 
@app.route('/master/<int:x>')
def game_master(x):
    while x != rnd: 
        if x < rnd:
            return jsonify(answer ="Higher!")
            #return "<h1>Higher!</h1>"

        elif x > rnd:
            return jsonify(answer = "Lower!")
            #return "<h1>Lower!</h1>"
            
    else:
        return jsonify(answer ="Won!")
        #return "<h1>Won!</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=5002, host="0.0.0.0")


# Debug mode: Enabling debug mode with debug=True can be helpful during development, but it's recommended to disable it in production. Debug mode may expose sensitive information and pose security risks..


