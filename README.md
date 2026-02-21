# FRESHKIDS: GitHub Actions Demo 

A beginner-friendly demo project showing four essential GitHub Actions workflows that every developer should know.

---

## Project Structure

```
freshkids-github-actions-demo/
 .github/
 workflows/
 1-secret-scan.yml # TruffleHog secret scanning
 2-test.yml # pytest automated testing
 3-docker.yml # Docker build & push
 4-deploy.yml # Staged deployment with approval gate
 app/
 app.py # Simple Flask web app
 tests/
 test_app.py # pytest test suite
 Dockerfile # Container definition
 requirements.txt # Python dependencies
 README.md
```

---

## The Pipeline Flow

```
Code pushed to GitHub
 
 
 Secret Scan ← catches leaked API keys / passwords
 
 
 Run Tests ← catches broken code before it ships
 
 
 Docker Build ← packages the app into a container
 
 
 Deploy Staging ← auto-deploys for testing
 
 
 Manual Approval ← human reviews before going live
 
 
 Deploy Production
```

---

## Setup

### 1. Fork / clone this repo

```bash
git clone https://github.com/YOUR_USERNAME/freshkids-github-actions-demo
cd freshkids-github-actions-demo
```

### 2. Add GitHub Secrets

Go to **Settings → Secrets and variables → Actions** and add:

| Secret | Description |
|--------|-------------|
| `DOCKERHUB_USERNAME` | Your Docker Hub username |
| `DOCKERHUB_TOKEN` | Docker Hub access token (create at hub.docker.com → Account Settings → Security) |

### 3. Set up GitHub Environments

Go to **Settings → Environments** and create:
- `staging` — no restrictions
- `production` — add yourself as a Required Reviewer

### 4. Push code and watch it run!

```bash
git add .
git commit -m "trigger pipeline"
git push origin main
```

---

## Run Tests Locally

```bash
pip install -r requirements.txt
pytest tests/ -v
```

## Run the App with Docker

```bash
docker build -t freshkids-demo .
docker run -p 5000:5000 freshkids-demo
# Visit http://localhost:5000
```

---

## What You'll Learn

- **Secret scanning**: How TruffleHog detects leaked credentials automatically
- **Automated testing**: How pytest integrates with GitHub Actions to block broken code
- **Docker in CI**: How to build and version container images on every push
- **Deployment gates**: How to use GitHub Environments for staged rollouts with approval

---

## Demo Scenarios for Filming

### Happy path — everything works
Push clean code and watch all 4 stages go green.

### Break the secret scan
Add a fake API key to any file:
```python
API_KEY = "AKIA1234567890ABCDEF" # Fake AWS key pattern — TruffleHog will catch it
```

### Break the tests
Edit `app/app.py` and change the home message, then push without updating tests.

### Break the Docker build
Introduce a syntax error in the Dockerfile.

---

*Made for [FRESHKIDS](https://youtube.com/@freshkids) — cybersecurity & tech education for beginners.*
