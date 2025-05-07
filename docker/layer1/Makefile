build:
	docker build -t ubuntu .
run:
	docker run -it -d --name ubuntu ubuntu 
history:
	docker history ubuntu
exec:
	docker exec -it ubuntu /bin/bash
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi -f $$(docker images -q)
