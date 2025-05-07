build:
	docker build -t node_signal_test_app .
run:
	docker run -it -p 8000:8000 --name node_signal node_signal_test_app 
history:
	docker history node_signal
stop:
	docker stop node_signal
kill:
	docker kill --signal="SIGTERM" node_signal
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi -f $$(docker images -q)
