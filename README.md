# Flask Game App and containerization

This is a simple Flask application that consists of two servers: a Master Server and a Player Server. The Master Server generates a random number between 1 and 1000, and the Player Server tries to guess the number by making requests to the Master Server.


## Getting Started

These instructions will get you a copy of the project, up and running on your local machine for development and testing purposes.

### Prerequisites
Install the required dependencies with the assumption that python is already installed on your local machine.
Setup Python Virtual Environment (py -3 -m venv {Name of virtual environment}).
Activate virtual environment (.\\{Name of virtual environment}\Scripts\activate).
Install Flask (pip install Flask) and its dependencies.
You will need Docker installed on your machine. You can download Docker [here](https://www.docker.com/get-started).
You can also spin up a virtual server to install Docker on it. Attached is the userdata to install Docker on an AWS EC2.

#!/bin/bash
sudo yum update -y
sudo yum install docker -y
sudo usermod -a -G docker ec2-user
newgrp docker
systemctl start docker
systemctl enable docker

### Clone the Repository

First, clone this repository onto your local machine by using the following command:

git clone https://github.com/PPM-CloudOps/applicant-task-mgboji.git


## Application

1. Start the Master Server: python master_server.py

The Master Server will run on http://localhost:5002

2. Start the Player Server: python player_server.py

The Player Server will run on http://localhost:5000

3. Open your web browser and go to http://localhost:5000 to access the Player Server.

4. Open your web browser and go to http://localhost:5000/play to start the game. The Player Server will make requests to the Master Server to guess the random number.

5. The game will continue until the Player Server guesses the correct number. The game history, including the guesses and responses, will be displayed on the webpage.

## Endpoints

The following endpoints are available:

### Master Server

- `/Master Server` - Renders the master_server.html template.
- `/health` - Renders the health.html template.
- `/hostname` - Returns the hostname of the server.
- `/hostnameIp` - Returns the IP address of the server.
- `/master/<int:x>` - Takes an integer `x` as input and returns whether the guess is higher, lower, or the correct number.

### Player Server

- `/Player Server` - Renders the player_server.html template.
- `/health` - Renders the health.html template.
- `/hostname` - Returns the hostname of the server.
- `/hostnameIp` - Returns the IP address of the server.
- `/play` - Initiates the game by making requests to the Master Server to guess the random number.



### Building the Docker Images
To build the Docker images from the two (2) Dockerfiles, use this command (Base image is python3.9-slim):

```
docker build -t (image name) .
```

### Running the Docker Containers
Start a Docker containers from the images:

```
docker run -d -p 5002:5002 --name (container name) (image name)
```
docker run -d -p 5000:5000 --name (container name) (image name)

The Flask application inside the Docker containers will start and listen on port 5002 and 5000 respectively.

### Testing the Application
Now, your backend Flask application should be running at http://localhost:5000 and http://localhost:5002. You can send HTTP requests to this URL to interact with the application.

If you deploy it in an EC2 instance, enable the security group of instance to accept traffic on port 5000, port 5002 and access the
backend app with Postman app on http://instance-public-ip:5000 and http://instance-public-ip:5002.

### Endpoints
The following endpoints are available:

### Master Server

- `/Master Server` - Renders the master_server.html template.
- `/health` - Renders the health.html template.
- `/hostname` - Returns the hostname of the server.
- `/hostnameIp` - Returns the IP address of the server.
- `/master/<int:x>` - Takes an integer `x` as input and returns whether the guess is higher, lower, or the correct number.

### Player Server

- `/Player Server` - Renders the player_server.html template.
- `/health` - Renders the health.html template.
- `/hostname` - Returns the hostname of the server.
- `/hostnameIp` - Returns the IP address of the server.
- `/play` - Initiates the game by making requests to the Master Server to guess the random number.

### Running the Docker Compose

This yaml file contains the Docker Compose configuration  consisting of two services: player_server and master_server. 

### Player Server
The player_server service is built from the ./Player directory. It runs a player server that listens on port 5001. You can access the player server by visiting http://localhost:5001.

### Master Server
The master_server service is built from the ./Game directory. It runs a master server that listens on port 5004. You can access the master server by visiting http://localhost:5004.

### Application

To start the services, run the following command:

docker-compose up -d
The -d flag runs the services in detached mode, allowing them to run in the background.

To stop the services, use the following command:

docker-compose down