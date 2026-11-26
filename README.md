# DevOps Practice Project

A beginner-friendly project to practise Linux shell scripting, Python testing, Docker, Docker Compose, Jenkins, Kubernetes, and GitHub Actions.

## Project structure

```text
.
├── app/
│   ├── app.py
│   └── test_app.py
├── scripts/
│   ├── build.sh
│   └── run.sh
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── .github/workflows/ci.yml
├── Dockerfile
├── docker-compose.yml
└── Jenkinsfile
```

## 1. Run the application locally

Requires Python 3.10 or newer.

```bash
python app/app.py
```

Open http://localhost:8080 or check http://localhost:8080/health.

Run tests:

```bash
python -m unittest discover -s app -p 'test_*.py' -v
```

## 2. Build and run with Docker

```bash
chmod +x scripts/*.sh
./scripts/build.sh
./scripts/run.sh
```

Then visit http://localhost:8080.

## 3. Run with Docker Compose

```bash
docker compose up --build
```

Stop it with `Ctrl+C`, or run `docker compose down` in another terminal.

## 4. Jenkins

Create a Jenkins Pipeline job pointing to this repository. The included `Jenkinsfile` runs Python unit tests and builds the Docker image. The Jenkins agent needs Python 3 and Docker installed, with permission to run Docker commands.

## 5. Kubernetes

Build the image in an environment accessible to your cluster, and make it available to the cluster nodes (or push it to a registry and update the image in `k8s/deployment.yaml`).

Apply the manifests:

```bash
kubectl apply -f k8s/
kubectl get deployments,pods,services
kubectl port-forward service/devops-practice-service 8080:80
```

Visit http://localhost:8080. Remove the resources with `kubectl delete -f k8s/`.

## 6. GitHub Actions

The workflow in `.github/workflows/ci.yml` runs unit tests and builds the Docker image on pushes and pull requests.

## Suggested learning order

1. Read the Python app and run the unit tests.
2. Practise the shell scripts and Linux permissions.
3. Build, inspect, run, and stop the Docker container.
4. Understand each Jenkins pipeline stage.
5. Deploy the app to Kubernetes and inspect its pods and service.
6. Push a change and watch the GitHub Actions workflow.

This is a learning starter, not a production deployment. Add registry credentials, image versioning, resource limits, security scanning, and deployment approvals before using it for real workloads.
