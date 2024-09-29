#!/bin/sh

# Instructions here: https://joss.readthedocs.io/en/latest/submitting.html#docker
docker run --rm -it \
    -v $PWD:/data \
    -u $(id -u):$(id -g) \
    --env JOURNAL=joss \
    openjournals/inara:latest \
    -o pdf \
    paper.md


echo Generating preprint
docker run --rm -it \
    -v $PWD:/data \
    -u $(id -u):$(id -g) \
    --env JOURNAL=joss \
    openjournals/inara:latest \
    -o preprint \
    paper.md

