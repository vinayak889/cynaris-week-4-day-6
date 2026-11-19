# W4D6: CI/CD with GitHub Actions & Docker

A Django sample app for practicing automated tests, Docker image builds, Docker Compose with PostgreSQL, GitHub Actions, and optional SSH deployment.

## Local run (Docker required)
1. Copy `.env.example` to `.env` and replace values.
2. Run `docker compose up --build`.
3. Open `http://localhost:8000/` and `http://localhost:8000/health/`.

## Pipeline behavior
- Pull requests and pushes to `main`: test job runs.
- Pushes to `main` after tests pass: build and push Docker image, then SSH deploy.

## GitHub Actions secrets
Add repository Actions secrets: `DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`, `DEPLOY_HOST`, `DEPLOY_USER`, `DEPLOY_SSH_KEY`. The deploy job requires a Linux server with Docker installed, SSH access configured, and inbound port 8000 available (or configure a reverse proxy). Do not commit secrets or `.env`.

## Notes
This is a learning starter, not a hardened production deployment. The SSH deploy example launches the container without injecting Django/PostgreSQL settings; configure production environment variables and a persistent external database before using it outside a demo. The app test suite uses Django's default test database configuration.
