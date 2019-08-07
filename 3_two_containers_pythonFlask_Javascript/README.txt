# My first GET call to the server
It runs a container with a flask server (see example 2).
This repo also contains a frontend/ folder dedicated to an
example of GET call to the server, that you can execute by
the command line, with nodejs, in order to programmatically
interact with the server.

ref: https://nodejs.org/de/docs/guides/nodejs-docker-webapp/

1. Launch the flask server from its folder
    1. Build the image
    /flaskapp>docker image build -t fapi:v0.1 .
    2. Run the container in background
    >docker container run -ti -d -p 5000:5000 --name=appflask fapi:v0.1
    3. To see what's happening in the container
    >docker container logs appflask

2. Execute the nodeJS script
    >node frontend/index