# Docker

This folder contains the learning resources and reference materials related to **Docker** prepared as part of the DevOps assignment.

## Contents

### Docker Cheat Sheet

A quick reference covering important Docker concepts, commands, and commonly used operations.

Topics include:

* Docker basics
* Docker images
* Docker containers
* Dockerfile
* Docker Hub
* Building Docker images
* Running containers
* Managing images and containers
* Common Docker commands

### Docker Workflow

A visual workflow explaining how Docker works from application development to running a container.

The workflow covers:

```text
Application Code
       ↓
   Dockerfile
       ↓
  Docker Image
       ↓
 Docker Container
       ↓
 Running Application
```

It also shows how Docker images can be stored, pushed to, and pulled from a container registry such as Docker Hub.

---

## What is Docker?

Docker is a platform used to **build, package, and run applications in containers**.

A container packages an application together with the dependencies it needs, allowing it to run consistently across different environments.

### Basic Docker Flow

```text
Code
  ↓
Dockerfile
  ↓
Image
  ↓
Container
  ↓
Application
```

---

## Important Docker Concepts

| Concept        | Description                                                |
| -------------- | ---------------------------------------------------------- |
| **Dockerfile** | A file containing instructions for building a Docker image |
| **Image**      | A read-only template used to create containers             |
| **Container**  | A running instance of a Docker image                       |
| **Docker Hub** | A registry used to store and share Docker images           |
| **Volume**     | Used for persistent data storage                           |
| **Network**    | Allows containers to communicate with each other           |

---

## Common Docker Commands

```bash
# Check Docker version
docker --version

# Download an image
docker pull <image>

# List Docker images
docker images

# Build an image
docker build -t <image-name> .

# Run a container
docker run <image-name>

# List running containers
docker ps

# List all containers
docker ps -a

# Stop a container
docker stop <container-id>

# Start a stopped container
docker start <container-id>

# Remove a container
docker rm <container-id>

# Remove an image
docker rmi <image-id>

# Push an image to Docker Hub
docker push <username>/<image-name>
```

---

## How to Use This Folder

Use the **Docker Cheat Sheet** for quick revision of Docker commands and concepts.

Use the **Docker Workflow** for understanding the overall process of building and running applications using Docker.

These resources are intended as quick references for students learning Docker as part of the DevOps assignment.

---

## Objective

The objective of this section is to provide simple and practical Docker resources that help in understanding:

* Containerization
* Docker images
* Docker containers
* Dockerfiles
* Docker commands
* Docker Hub
* Docker application workflow

---

## Contribution

This Docker section is part of the **DevOps Assignment — Group 08**.

Team members contribute their respective Docker resources through GitHub branches and Pull Requests.

