build:
	docker build -t cmd2 .
run:
	docker run -it -d --name cmds -p 8000:80 -v /work/neo/docker/volume/data:/data -v /work/neo/docker/volume/nginx-site-enabled:/etc/nginx-site-enabled -v /work/neo/docker/volume/nginxlog:/var/log/nginx cmd2
exec:
	docker exec -it cmds /bin/bash
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi -f $$(docker images -q)
