#!/bin/sh

# Instructions here: https://joss.readthedocs.io/en/latest/submitting.html#docker
docker run --rm -it \
    -v $PWD:/data \
    -u $(id -u):$(id -g) \
    --env JOURNAL=joss \
    openjournals/inara:latest \
    -o pdf \
    paper.md


# docker run --rm \
#     --volume $PWD:/data \
#     --user $(id -u):$(id -g) \
#     --env JOURNAL=joss \
#     openjournals/inara