# === 전체 워크플로우 ===
all : build run k8init appdep appsvc getdep getsvc getpod
restart: k8stop appdep appsvc getdep getsvc getpod
stop: k8stop dockerstop

# === Docker 빌드 및 실행 ===
build:
	docker build -t remote .
run:
	docker run -it -d -p 8000:8000 --name remote remote
exec:	
	docker exec -it remote /bin/bash
dstart:
	docker start remote
dstop:
	docker stop remote
dlogs:
	docker logs remote
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi -f $$(docker images -q)

# === Kubernetes 초기화 ===
k8init: k8commit k8clean

k8commit:
	docker commit remote remoteapi
	docker tag remoteapi impelfin/remoteapi
	docker push impelfin/remoteapi

k8clean:
	docker rm -f $$(docker ps -aq)
	docker rmi -f $$(docker images -q)

# === Kubernetes 명령 ===
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

getnode:
	kubectl get nodes

klogs:
	kubectl logs $$(kubectl get pod --no-headers | grep remoteapi | awk '{print $$1}')

# === Kubernetes 삭제 ===
k8stop: delsvc deldep delpod

delsvc:
	kubectl delete svc remoteapi

deldep:
	kubectl delete deployment remoteapi

delpod:
	kubectl get pod --no-headers | grep remoteapi | awk '{print $$1}' | xargs -r -I {} kubectl delete pod {} --force

# === Kubernetes 상세 정보 ===
desdep:
	kubectl describe deployment remoteapi

dessvc:
	kubectl describe svc remoteapi

despod:
	kubectl describe pod $$(kubectl get pod --no-headers | grep remoteapi | awk '{print $$1}')
