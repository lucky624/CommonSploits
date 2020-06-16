#!/bin/bash
imageName=the_hole_service
containerName=the_hole_container
memory=200m

containerRunning=$(docker inspect --format="{{ .State.Running }}" $containerName 2> /dev/null)

if [ "$containerRunning" == "true" ]; then
        docker rm -f $containerName &> /dev/null
        docker run --restart=always -d -p 5003:5003 --name $containerName --memory=$memory $imageName
else
        docker rm -f $containerName &> /dev/null
        docker run --restart=always -d -p 5003:5003 --name $containerName --memory=$memory $imageName
fi