# My first server
It will run a container launching a flask server.



1. Build the image
>docker image build -t fapi:v0.1 .
2. Run the container in background
>docker container run -ti -d -p 5000:5000 --name=appflask fapi:v0.1
3. To see what's happening in the container
>docker container logs appflask
4. Open a browser and go to: http://localhost:5000.
   Since it is set on localhost, with 5000 as port, you will see what the server is serving.
