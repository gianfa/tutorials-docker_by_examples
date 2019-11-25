# Make projects interacting between each other. Networking.

## Final achievement
We're gonna setup a minimum global project in order to make each service able to communicate with the others.


### The projects
<img src="https://github.com/gianfa/docker_by_examples/blob/master/_img/networking_tree.png" width="500">
As you can see we have:
* two projects, each one having:
    * its proper docker compose
    * proper services associated with *workidirs*

We have a flask server in each project and a express server in the *proj2*.

## Instructions
Follow the steps below to see how you can make two projects interact.
### Steps:
    1. setup the project and launch it
        1.1. proj1> docker-compose up
        1.2. proj2> docker-compose up
    2. inspect the network
        2.1. proj1> docker inspect proj1net1
        2.1. Take a look to 'Containers' property to have a list of assoctiaed containers
    3. Check the communication
        3.1. proj2> docker exec -it container21 sh
        3.2. # ping -w 3 container11  # now you should see it regularly pinging
        3.3. # ping -w 3 proj1_serv1  # now you should see it regularly pinging
        3.4. # exit
        3.5. proj2> docker exec -it container22 sh
        3.6. # node index  # now you should see the script to give you the final result of a sum() call to container11
        3.7. # exit
(notice that "#" is the bash cursor, you don't have to write it!)

        
## Expected result
From the picture below you can see the results of the steps above, with little modifications.
<img src="https://github.com/gianfa/docker_by_examples/blob/master/_img/networking_exp_res.png">


## Resources
* [Connect Containers, official docs](https://docs.docker.com/v17.09/engine/userguide/networking/work-with-networks/#create-networks)
* [Docker Network inspect](https://docs.docker.com/engine/reference/commandline/network_inspect/)
* [Finding Container Network](https://stackoverflow.com/questions/43904562/docker-how-to-find-the-network-my-container-is-in)
