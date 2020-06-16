#!/bin/bash
imageName=the_hole_service
containerName=the_hole_container
memory=200m

docker build -t $imageName -f Dockerfile  .

containerRunning=$(docker inspect --format="{{ .State.Running }}" $containerName 2> /dev/null)

if [ "$containerRunning" == "true" ]; then
        docker rm -f $containerName &> /dev/null
        docker run -d -p 5003:5003 --restart=always --name $containerName --memory=$memory $imageName
else
        docker rm -f $containerName &> /dev/null
        docker run -d -p 5003:5003 --restart=always --name $containerName --memory=$memory $imageName
fi
