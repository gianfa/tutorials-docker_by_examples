# My first live updating with persistency
Here a container will be ran, and all changes made to server.py 
will be live update.


ref: https://training.play-with-docker.com/beginner-linux/#Task_3

Instructions:
0. Define a WORKDIR inside the DockerFile and copy in it the files to be persistently edited
    Dockerfile|
        WORKDIR    /dockwork
        COPY       . /dockwork/
1. Build the image
    > docker image build -t fapi:v0.1 .
2. Run the container in background, mounting the volume from current dir (if
   here the code is execute) to the WORKDIR.
    > docker container run -ti -p 5000:5000 -v "$(pwd)":/dockwork/ fapi:v0.1
3. In server.py change the output of the hello() function and see what happens
    from the browser. You won't need to rebuild the image in order to see the changes.


# alternative flag #
 --mount type=bind,source="$(pwd)",target=/dockwork/site/ \
