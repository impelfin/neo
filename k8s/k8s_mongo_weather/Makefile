# === 전체 워크플로우 ===
all: build run k8init appdep appsvc getdep getsvc getpod
restart: k8stop appdep appsvc getdep getsvc getpod
stop: k8stop dockerstop

# === Docker 빌드 및 실행 ===
build:
	docker build -t mongo .
	docker build -t weather .

run:
	docker network create app-net || true
	docker run -it -d --network app-net --name mongo mongo
	docker run -it -d --network app-net -e MONGO_URL="mongodb://mongo:27017/weathers" -p 8000:8000 --name weather weather

exec:	
	docker exec -it weather /bin/bash

dockerstop:
	docker stop weather mongo

dockerstart:
	docker start weather mongo

logs:
	docker logs weather

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
	docker commit weather weathers
	docker tag weathers impelfin/weathers
	docker push impelfin/weathers

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
	kubectl logs $$(kubectl get pod --no-headers | grep weathers | awk '{print $$1}')

# === Kubernetes 삭제 ===
k8stop: delsvc deldep delpod

delsvc:
	kubectl delete svc weathers

deldep:
	kubectl delete deployment weathers

delpod:
	kubectl get pod --no-headers | grep weathers | awk '{print $$1}' | xargs -r -I {} kubectl delete pod {} --force

# === Kubernetes 상세 정보 ===
desdep:
	kubectl describe deployment weathers

dessvc:
	kubectl describe svc weathers

despod:
	kubectl describe pod $$(kubectl get pod --no-headers | grep weathers | awk '{print $$1}')
