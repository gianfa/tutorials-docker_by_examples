# My first Microservices architecture

It uses a docker-compose file to run two communicating services:
    * backend, as a server
    * frontend, as a client


see also https://docs.docker.com/compose/compose-file/#depends_on
ref1: https://runnable.com/docker/basic-docker-networking
ref2: https://docs.docker.com/network/bridge/ 

1. Build the two images
    1. Server flask
    > docker image build -t fapi:v0.1 flaskapp/
    2. NodeJs frontend
    > docker image build -t fejs:v0.1 frontend/
2. Create the docker-compose.yml file
    1. specify the flask server 'container_name' with a SERVERCONTAINERNAME value.
    2. adapt hostnames inside the frontend/ files to be SERVERCONTAINERNAME (ex: localhost -> SERVERCONTAINERNAME)
3. Launch both the system
    >docker-compose up


