all:
	docker volume create open-local
	docker volume create open-webui-local
dry:
	docker compose --dry-run up -d
run:
	docker compose up -d
stop:
	docker compose down
rm:
	docker volume rm ollama local
	docker volume rm open-webui-local