#!/bin/bash
#After destructive attack (rm -rf / rm messages.txt)
docker-compose down
docker-compose up --force -d
