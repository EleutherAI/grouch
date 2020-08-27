#!/usr/bin/env bash

docker run --rm -it -p 5000:5000 -v $PWD/app/data:/app/data grouch