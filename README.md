# orderforseu

东南大学自动请假加健康申报

docker 镜像生成：
docker build -f Dockerfile -t NAME:TAG .
docker run -it --name CONTAINER --shm-size="500M" --privileged --user root NAME:TAG

linux设置定时启动docker：
cd /etc
crontab -e
59 5 * * * docker start CONTAINER
systemctl restart crond
