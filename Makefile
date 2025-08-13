.PHONY: up down logs build shell

up:
	@echo "Starting up services..."
	@docker-compose up --build -d

down:
	@echo "Stopping services..."
	@docker-compose down --remove-orphans

logs:
	@echo "Tailing logs for all services..."
	@docker-compose logs -f

build:
	@echo "Building (or rebuilding) Docker images..."
	@docker-compose build

shell:
	@echo "Accessing the app container shell..."
	@docker-compose exec app bash
