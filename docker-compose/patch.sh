#!/bin/bash
#After patch service (fix vulnerabilities or bugs)
docker-compose down
docker-compose up --build -d
