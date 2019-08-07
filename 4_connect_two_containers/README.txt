# Connecting two containers through a shared network
It runs two containers:
    * A flask server, as backend,
    * A nodeJS script about REST calls, as frontend client.

ref1: https://runnable.com/docker/basic-docker-networking
ref2: https://docs.docker.com/network/bridge/ 

1. Build the two images
    1. Server flask
    /flaskapp> docker image build -t fapi:v0.1 .
    2. NodeJs frontend
    /frontend> docker image build -t fejs:v0.1 .
2. Manually create a network to be shared between containers
    Let's call it 'containers-net'
    > docker network create --driver=bridge containers-net
3. Launch both the containers on the new network
    0. configure the server calls, namely the host name, to the SERVERCONTAINERID [or SERVERCONTAINERNAME] in all frontend/ files.
    1. Server flask
    docker run -ti -d -p 5000:5000 --name=flaskapp --net=containers-net fapi:v0.1
    2. NodeJs frontend
    docker run -ti -p 80:80 --net=containers-net --rm fejs:v0.1


