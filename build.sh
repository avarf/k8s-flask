#!/bin/bash -eux

docker build -f Dockerfile -t avarf/k8s-flask .
docker push avarf/k8s-flask:latest