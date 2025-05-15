build:
	docker build -t nodejs .
run:
	docker run -it -d -p 8000:8000 --name nodejs nodejs
exec:	
	docker exec -it nodejs /bin/bash
start:
	docker start nodejs
stop:
	docker stop nodejs
logs:
	docker logs nodejs
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi -f $$(docker images -q)
