all : build run k8init appdep appsvc getdep getsvc getpod
restart : delsvc deldep delpod appdep appsvc getdep getsvc getpod
stop : delsvc deldep delpod
build:
	docker build -t remote .
run:
	docker run -it -d -p 8000:8000 --name remote remote
exec:	
	docker exec -it remote /bin/bash
start:
	docker start remote
stop:
	docker stop remote
logs:
	docker logs remote
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi -f $$(docker images -q)

k8init:
	docker commit remote remoteapi
	docker tag remoteapi impelfin/remoteapi
	docker push impelfin/remoteapi
	docker rm -f $$(docker ps -aq)
	docker rmi -f $$(docker images -q)
getnode:
	kubectl get nodes
appdep:
	kubectl apply -f deployment.yaml
appsvc:
	kubectl apply -f service.yaml
getdep:
	kubectl get deployment
getsvc:
	kubectl get svc -o wide
getpod:
	kubectl get pod -o wide
delsvc:
	kubectl delete svc remoteapi
deldep:
	kubectl delete deployment remoteapi
delpod:
	kubectl get pod | grep remoteapi | awk '{print $$1}' | xargs -I {} kubectl delete pod {} --force
desdep:
	kubectl describe deployment remoteapi
dessvc:
	kubectl describe svc remoteapi
despod:
	kubectl describe pod remoteapi
