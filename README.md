# orderforseu

docker 镜像生成：
docker build -f Dockerfile -t NAME:TAG .
docker run -it --name CONTAINER --shm-size="500M" --privileged --user root NAME:TAG