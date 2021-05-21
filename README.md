# docker_copy_file_example

Example on how to copy a file from a docker container

1. docker build -t <image_name> .

2. docker run --name=<container_name> <image_name>

3. docker cp <conainer_name>:/test.txt .
