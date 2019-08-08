# VOLUME declaration in docker-compose - 1 container
Binding container to volume, allowing reciprocal PERSISTENT editing

Here one container is pulled up by docker-compose and, then, it
is persistently editable in live update.

ref1: https://training.play-with-docker.com/docker-volumes/
ref2: https://docs.docker.com/storage/volumes/


Instructions:
1. Build the image
    > docker image build -t fapi:v0.1 flaskapp/
2. Create the docker-compose.yml file
    Specify 'volumes'  as HOSTPATH:WORKDIR, see below
3. Launch the system
    >docker-compose up
-. Now edit the flaskapp/ files and see how they update.


Commented example
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

