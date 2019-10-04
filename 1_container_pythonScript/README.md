
# First Docker container
It runs a container that executes index.py in order to print a sentence.
The --rm flag will remove the container right after the print execution.

Instructions:
> docker image build -t sayhello:v0.1 .
> docker run -ti --rm --name greetingapp sayhello:v0.1
