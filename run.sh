#!/bin/sh

docker build -t test_image .

docker run --name=test_container test_image

docker cp test_container:/test.txt .