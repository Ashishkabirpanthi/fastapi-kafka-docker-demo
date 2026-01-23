kafka:
	docker compose down -v
	docker compose build --no-cache
	docker compose up

prune_build:
	docker compose down -v
	docker system prune -f
	docker compose up --build

