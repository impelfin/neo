all : appdep getdep getsvc getpod
restart : delsvc deldep delpod appdep getdep getsvc getpod
stop : delsvc deldep delpod
getnode:
	kubectl get nodes
appdep:
	kubectl apply -f deployment.yaml
getdep:
	kubectl get deployment
getsvc:
	kubectl get svc -o wide
getpod:
	kubectl get pod -o wide
delsvc:
	kubectl delete svc $(name)
deldep:
	kubectl delete deployment $(name)
delpod:
	kubectl get pod | grep $(name) | awk '{print $$1}' | xargs -I {} kubectl delete pod {} --force
desdep:
	kubectl describe deployment $(name)
dessvc:
	kubectl describe svc $(name)
despod:
	kubectl describe pod $(name)