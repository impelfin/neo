all:
	json-server --watch ./data.json --host 0.0.0.0 --port 5000 &
install:
	pip install json-server
ps:
	ps -ef | grep json-server
kill:
	kill -9 `ps -ef | grep json-server | cut -d " " -f8`
