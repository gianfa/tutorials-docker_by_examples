# VOLUME declaration in docker-compose - 1 container
Binding container to volume, allowing reciprocal PERSISTENT editing



ref1: https://training.play-with-docker.com/docker-volumes/
ref2: https://docs.docker.com/storage/volumes/

Instructions:
1. Build the two images
    1. Server flask
    > docker image build -t fapi:v0.1 flaskapp/
    2. NodeJs frontend
    > docker image build -t fejs:v0.1 frontend/
2. Create the docker-compose.yml file
    1. specify the flask server 'container_name' with a SERVERCONTAINERNAME value.
    2. adapt hostnames inside the frontend/ files to be SERVERCONTAINERNAME (ex: localhost -> SERVERCONTAINERNAME)
3. Launch the system
    >docker-compose up

docker-compose.yml|
    version: '3'

    services:
    appflask:
        image: fapi:v0.1
        container_name: appflask
        hostname: appflaskhost
        build: .
        ports:
        - "5000:5000"
        volumes:
        - <PATHToTheContainerSource_FromtheRoot>:<WORKDIR_ofThe_DockerFile_ofTheTargetContainer>:ro

