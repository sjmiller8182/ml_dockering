#!/bin/bash

docker stop mlexample
docker rm mlexample

docker build --no-cache --tag mle:dev .
docker run --publish 1313:1313 --name mlexample mle26:1.0
