build:
	docker build -t mysql .
run:
	docker run -it -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 -v /work/neo/docker/mysql/mysqld:/var/run/mysqld -v /work/neo/docker/mysql/mysql:/app --name mysql mysql
exec:	
	docker exec -it mysql /bin/bash
start:
	docker start mysql
stop:
	docker stop mysql
logs:
	docker logs mysql
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi -f $$(docker images -q)
