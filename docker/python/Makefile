build:
	docker build -t python .
run:
	docker run -it -d -p 3000:3000 --name python python
exec:	
	docker exec -it python /bin/bash
start:
	docker start python
stop:
	docker stop python
logs:
	docker logs python
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi -f $$(docker images -q)
