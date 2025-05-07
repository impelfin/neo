build:
	docker build -t cmd1 .
run:
	docker run -it -d --name cmds -p 8000:80 cmd1
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
