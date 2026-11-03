# Retail ETL with Docker

A small batch pipeline that loads public retail sales data from CSV into PostgreSQL.
Everything runs with a single `docker compose up`.

## Architecture
```
data/*.csv ──► etl (Python) ──► postgres ◄── adminer (web UI, :8080)
```
<!-- TODO: replace with a proper diagram image when the project is done -->

## Tech stack
Docker, Docker Compose, Python 3.12, pandas, PostgreSQL 16

## Run it
```bash
cp .env.example .env
docker compose up --build
```
Then open http://localhost:8080 (Adminer) to look at the data.

## Design decisions
- TODO: why multi-stage build, why a non-root user, how re-runs avoid duplicates

## What I learned
- TODO

## Dataset
TODO: name + link of the public dataset (e.g. UCI Online Retail). No company data is used.
