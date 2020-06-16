#!/bin/bash
containerName=the_hole_container

containerRunning=$(docker inspect --format="{{ .State.Running }}" $containerName 2> /dev/null)

if [ "$containerRunning" == "true" ]; then
        echo $containerName "is up"
else
        docker start $containerName
fi