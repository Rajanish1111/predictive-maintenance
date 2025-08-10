.PHONY: up sim

up:
	docker compose up --build

sim:
	python3 simulator/telemetry_simulator.py