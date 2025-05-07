build-base:
	docker build -t web-base -f Dockerfile.base .
build:
	docker build -t photoview .
inspect:
	docker inspect --format="{{.Config.OnBuild}}" web-base
run:
	docker run -it -d -p 8000:80 photoview 
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi -f $$(docker images -q)
