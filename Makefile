SHELL := /bin/bash

.PHONY: bootstrap up down logs check test fmt lint ci frontend backend svg

bootstrap:
	python3 -m venv .venv || true
	. .venv/bin/activate && pip install -U pip pre-commit
	pre-commit install
	npm -C frontend install

up:
	docker compose -f infra/docker-compose.yml up -d --build

down:
	docker compose -f infra/docker-compose.yml down

logs:
	docker compose -f infra/docker-compose.yml logs -f --tail=200 backend frontend db

check: lint test

lint:
	docker compose -f infra/docker-compose.yml exec -T backend ruff check
	docker compose -f infra/docker-compose.yml exec -T backend black --check .
	docker compose -f infra/docker-compose.yml exec -T backend mypy app || true

fmt:
	docker compose -f infra/docker-compose.yml exec -T backend black .
	docker compose -f infra/docker-compose.yml exec -T backend ruff check --fix
	docker compose -f infra/docker-compose.yml exec -T backend isort .

test:
	docker compose -f infra/docker-compose.yml exec -T backend pytest -q

backend:
	docker compose -f infra/docker-compose.yml up -d --build backend

frontend:
	docker compose -f infra/docker-compose.yml up -d --build frontend
