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

# TODO replace "docs/_static/img/" in paths in paper.preprint.tex with root directory
cat paper.preprint.tex | sed "s/docs\/_static\/img\///g" > tmp
mv tmp paper.preprint.tex