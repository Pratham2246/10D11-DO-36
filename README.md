# 🚗 Automotive Management API – DevOps Implementation Project

## 📌 Project Overview

The **Automotive Management API** is a FastAPI-based backend application developed as part of the Datagami Skill Based Course at Medicaps University.

This project demonstrates a complete DevOps lifecycle implementation including:

- Backend API development
- Docker containerization
- Kubernetes deployment
- Rolling update strategy
- Zero-downtime deployment
- CI automation using GitHub Actions

This project follows industry-standard DevOps practices.

---

## 🛠️ Technology Stack

- **Backend Framework:** FastAPI (Python)
- **Language:** Python 3.x
- **Containerization:** Docker
- **Orchestration:** Kubernetes (Minikube)
- **CI Pipeline:** GitHub Actions
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
automotive-app/
│
├── main.py
├── requirements.txt
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── .github/workflows/deploy.yml
└── README.md
```

---

## 🚀 API Features

The API provides the following endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Welcome message |
| POST | /vehicles | Add new vehicle |
| GET | /vehicles | Get all vehicles |
| GET | /vehicles/{id} | Get vehicle by ID |
| DELETE | /vehicles/{id} | Delete vehicle |

The API uses in-memory storage for demonstration purposes.

---

## 🐳 Docker Implementation

### Build Docker Image

```
docker build -t automotive-api:v1 .
```

### Run Docker Container

```
docker run -p 8000:8000 automotive-api:v1
```

The application runs on:

```
http://localhost:8000
```

FastAPI Swagger documentation:

```
http://localhost:8000/docs
```

---

## ☸ Kubernetes Deployment

### Apply Deployment

```
kubectl apply -f deployment.yaml
```

### Apply Service

```
kubectl apply -f service.yaml
```

### Check Running Pods

```
kubectl get pods
```

### Access Service via Minikube

```
minikube service automotive-service
```

---

## 🔄 Rolling Update Strategy

The Kubernetes Deployment is configured with:

- Strategy: RollingUpdate
- maxUnavailable: 0
- maxSurge: 1
- Replicas: 2

This ensures:

- Zero downtime deployment
- High availability
- Seamless version upgrades (v1 → v2)

---

## ⚙️ CI Pipeline – GitHub Actions

A CI pipeline is configured using GitHub Actions.

Workflow Location:

```
.github/workflows/deploy.yml
```

Pipeline automatically triggers on:

- Push to main branch

Pipeline steps:

1. Checkout repository
2. Build Docker image
3. Validate build process

Every commit to main automatically triggers CI execution.

---

## 📊 Deployment Architecture

Developer → GitHub → GitHub Actions → Docker Build → Kubernetes Deployment → Service Exposure

---

## 🎯 Learning Outcomes

Through this project, the following DevOps concepts were implemented:

- Backend API development
- Docker containerization
- Kubernetes Deployment & Service
- Rolling Update configuration
- Zero-downtime deployment strategy
- Git version control best practices
- CI automation with GitHub Actions

---

## 🔮 Future Enhancements

- Integration with MySQL database
- DockerHub automated image push
- Auto-deployment to Kubernetes from CI
- Horizontal Pod Autoscaling (HPA)
- Liveness & Readiness Probes
- Production-grade configuration

---

## 👨‍💻 Author

**Pratham Bhawar**  
Medicaps University  
Datagami Skill Based Course  
Academic Year: 2025–2026  

---

## ✅ Project Status

✔ Backend Developed  
✔ Dockerized  
✔ Kubernetes Deployed  
✔ Rolling Update Enabled  
✔ Zero Downtime Tested  
✔ CI Pipeline Configured  
✔ Production-Ready DevOps Workflow Implemented  

---

⭐ This project demonstrates a complete DevOps workflow using modern industry tools.
