build:
	docker build -t mongo .
run:
	docker run -it -d -p 27017:27017 -v /work/neo/docker/mongodb/mongod:/data/db -v /work/neo/docker/mongodb/mongo:/app --name mongo mongo
exec:	
	docker exec -it mongo /bin/bash
start:
	docker start mongo
stop:
	docker stop mongo
logs:
	docker logs mongo
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi -f $$(docker images -q)
