build:
	docker build -t ubuntu .
run:
	docker run -it --name ubuntu ubuntu
history:
	docker history ubuntu
ps:
	docker ps -a
img:	
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi -f $$(docker images -q)
