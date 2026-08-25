# 🚀 DevOps Learning Resources 

A curated DevOps learning repository containing ** video resources, official documentation, hands-on practice, projects, and a structured learning path**.

The goal is to learn DevOps practically instead of only watching tutorials.

---

## 🎥 Main Video Course

### DevOps Engineer Zero to Hero 2026 — The Techzeen

**Language:** Hindi / Urdu  
**Level:** Beginner → Job Ready  
**Topics:** Linux, Git, Docker, AWS, Terraform, CI/CD, Kubernetes and related DevOps tools.

👉 **YouTube Playlist:**  
https://www.youtube.com/playlist?list=PL50hSdfH4uDsyUM02ZHI2m0YBpihCYsml

> Tip: Don't just watch the playlist. After every major topic, create a small project and push your work to GitHub.

---

# 🗺️ Recommended DevOps Roadmap

Learn the tools in roughly this order:

```text
Linux & Networking
        ↓
Git & GitHub
        ↓
Bash / Shell Scripting
        ↓
Docker
        ↓
Docker Compose
        ↓
AWS / Cloud Basics
        ↓
CI/CD
        ↓
Jenkins / GitHub Actions
        ↓
Terraform (Infrastructure as Code)
        ↓
Ansible
        ↓
Kubernetes
        ↓
Helm
        ↓
Monitoring & Logging
(Prometheus + Grafana)
        ↓
Security / DevSecOps
        ↓
Projects + Deployment
```

---

# 1. 🐧 Linux

### What to learn

- Linux filesystem
- Files and directories
- `ls`, `cd`, `pwd`, `cp`, `mv`, `rm`
- Permissions: `chmod`, `chown`
- Processes and jobs
- `ps`, `top`, `kill`
- Package management
- SSH
- Environment variables
- Services and systemd
- Logs
- Networking commands
- Bash scripting

### Documentation

- [Linux Kernel Documentation](https://docs.kernel.org/)
- [GNU Coreutils Manual](https://www.gnu.org/software/coreutils/manual/coreutils.html)
- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/)

### Practice

Build a Bash script that:

1. Checks disk usage.
2. Checks running services.
3. Creates a backup.
4. Compresses the backup.
5. Saves logs with timestamps.

---

# 2. 🔀 Git & GitHub

### What to learn

- Git fundamentals
- Repository
- Commit
- Branch
- Merge
- Rebase
- Pull Request
- Merge conflicts
- `.gitignore`
- Tags
- GitHub Actions
- SSH authentication

### Documentation

- [Git Documentation](https://git-scm.com/doc)
- [Git Book](https://git-scm.com/book/en/v2)
- [GitHub Documentation](https://docs.github.com/)

### Must-know commands

```bash
git init
git clone
git status
git add
git commit
git push
git pull
git branch
git checkout
git switch
git merge
git rebase
git log
git stash
git tag
```

---

# 3. 🌐 Networking Basics

Before going deep into cloud and Kubernetes, understand networking.

### Learn

- IP address
- IPv4 / IPv6
- Subnetting
- CIDR
- DNS
- HTTP / HTTPS
- TCP / UDP
- Ports
- SSH
- NAT
- Firewall
- Load Balancer
- Reverse Proxy
- TLS / SSL

### Useful resources

- [MDN HTTP Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [Cloudflare Learning Center](https://www.cloudflare.com/learning/)
- [Cisco Networking Basics](https://www.cisco.com/c/en/us/solutions/small-business/resource-center/networking/networking-basics.html)

---

# 4. 🐳 Docker

Docker is one of the most important DevOps skills.

### Learn

- Containers
- Images
- Dockerfile
- Docker Hub
- Volumes
- Networks
- Port mapping
- Environment variables
- Multi-stage builds
- Docker Compose
- Container logs
- Container security

### Documentation

- [Docker Documentation](https://docs.docker.com/)
- [Docker Get Started](https://docs.docker.com/get-started/)
- [Docker Reference](https://docs.docker.com/reference/)

### Practice Project

Containerize a simple backend application:

```text
Application
    ↓
Dockerfile
    ↓
Docker Image
    ↓
Docker Container
    ↓
Docker Compose
    ↓
Application + Database
```

---

# 5. ☁️ AWS / Cloud

Start with the AWS services commonly used in DevOps.

### Learn

- EC2
- IAM
- VPC
- Security Groups
- S3
- EBS
- Load Balancer
- Auto Scaling
- CloudWatch
- Route 53
- RDS
- ECR
- ECS / EKS basics

### Documentation

- [AWS Documentation](https://docs.aws.amazon.com/)
- [AWS Getting Started](https://aws.amazon.com/getting-started/)
- [AWS Architecture Center](https://aws.amazon.com/architecture/)

### Practice

Deploy a Dockerized application to an AWS EC2 instance.

---

# 6. 🔄 CI/CD

Understand the complete pipeline:

```text
Developer
   ↓
Git Push
   ↓
Build
   ↓
Test
   ↓
Docker Build
   ↓
Security Scan
   ↓
Docker Registry
   ↓
Deploy
   ↓
Monitor
```

### Learn

- Continuous Integration
- Continuous Delivery
- Continuous Deployment
- Build pipelines
- Automated testing
- Secrets
- Artifacts
- Deployment strategies
- Rollback

---

# 7. ⚙️ Jenkins

Jenkins is a popular automation server used to create CI/CD pipelines.

### Learn

- Jenkins installation
- Jobs
- Pipeline
- Jenkinsfile
- Agents
- Credentials
- Webhooks
- Build triggers
- Pipeline stages
- Docker integration

### Documentation

- [Jenkins Documentation](https://www.jenkins.io/doc/)
- [Jenkins Pipeline Documentation](https://www.jenkins.io/doc/book/pipeline/)

### Practice

Create:

```text
GitHub
  ↓
Jenkins Webhook
  ↓
Build
  ↓
Test
  ↓
Docker Build
  ↓
Docker Push
  ↓
Deploy
```

---

# 8. 🟣 GitHub Actions

GitHub Actions is extremely useful when your source code is already hosted on GitHub.

### Learn

- Workflows
- Events
- Jobs
- Steps
- Runners
- Secrets
- Environment variables
- Artifacts
- Matrix builds
- Deployment workflows

### Documentation

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Actions Quickstart](https://docs.github.com/en/actions/quickstart)

### Example workflow idea

```text
Push Code
   ↓
Run Tests
   ↓
Build Docker Image
   ↓
Push Image
   ↓
Deploy Application
```

---

# 9. 🏗️ Terraform — Infrastructure as Code

Terraform allows infrastructure to be defined as code.

### Learn

- Providers
- Resources
- Variables
- Outputs
- State
- Modules
- Data sources
- `init`
- `plan`
- `apply`
- `destroy`
- Remote state
- State locking
- Terraform modules

### Documentation

- [Terraform Documentation](https://developer.hashicorp.com/terraform/docs)
- [Terraform Tutorials](https://developer.hashicorp.com/terraform/tutorials)
- [Terraform CLI](https://developer.hashicorp.com/terraform/cli)
- [Terraform Language](https://developer.hashicorp.com/terraform/language)

### Basic workflow

```bash
terraform init
terraform validate
terraform plan
terraform apply
terraform destroy
```

### Practice Project

Provision:

```text
AWS
 ├── VPC
 ├── Subnet
 ├── Security Group
 ├── EC2
 └── IAM
```

using Terraform.

---

# 10. 🤖 Ansible

Ansible is useful for configuration management and automation.

### Learn

- Inventory
- Playbooks
- Tasks
- Modules
- Variables
- Handlers
- Roles
- Templates
- Loops
- Conditionals
- Idempotency

### Documentation

- [Ansible Documentation](https://docs.ansible.com/)
- [Ansible User Guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)

### Practice

Automate server setup:

```text
New Server
   ↓
Install Docker
   ↓
Install Nginx
   ↓
Create User
   ↓
Copy Configuration
   ↓
Start Services
```

---

# 11. ☸️ Kubernetes

Kubernetes is used for container orchestration.

### Learn in this order

1. Containers
2. Pods
3. Deployments
4. ReplicaSets
5. Services
6. ConfigMaps
7. Secrets
8. Namespaces
9. Volumes
10. Ingress
11. Probes
12. Resource limits
13. StatefulSets
14. Jobs / CronJobs
15. RBAC
16. Autoscaling

### Documentation

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Kubernetes Concepts](https://kubernetes.io/docs/concepts/)
- [Kubernetes Tutorials](https://kubernetes.io/docs/tutorials/)
- [kubectl Reference](https://kubernetes.io/docs/reference/kubectl/)

### Practice

Deploy:

```text
Frontend
   ↓
Kubernetes Service
   ↓
Backend
   ↓
Database
```

---

# 12. ⛵ Helm

Helm is a package manager for Kubernetes.

### Learn

- Charts
- Values
- Templates
- Releases
- `helm install`
- `helm upgrade`
- `helm rollback`
- Chart structure

### Documentation

- [Helm Documentation](https://helm.sh/docs/)

---

# 13. 📊 Monitoring — Prometheus + Grafana

A production DevOps engineer should understand observability.

### Prometheus

Used mainly for collecting and querying metrics.

- [Prometheus Documentation](https://prometheus.io/docs/)

### Grafana

Used to visualize metrics and build dashboards.

- [Grafana Documentation](https://grafana.com/docs/)

### Learn

- Metrics
- Time-series data
- Prometheus targets
- PromQL
- Alerting
- Grafana dashboards
- Application monitoring
- Infrastructure monitoring

---

# 14. 🔐 DevSecOps

Security should be part of the pipeline, not an afterthought.

### Learn

- Secrets management
- IAM
- Least privilege
- Container security
- Dependency scanning
- Image scanning
- SAST
- DAST
- TLS
- Network security
- Kubernetes security

### Useful tools

- [Trivy](https://trivy.dev/)
- [OWASP](https://owasp.org/)
- [SonarQube](https://docs.sonarsource.com/sonarqube-server/)
- [AWS Security Documentation](https://docs.aws.amazon.com/security/)

---

# 🧪 Hands-On Project Roadmap

Don't stop after completing videos. Build projects.

## Project 1 — Dockerized Application

**Skills:** Git + Docker + Docker Compose

```text
GitHub
  ↓
Application
  ↓
Dockerfile
  ↓
Docker Image
  ↓
Docker Compose
  ↓
Application + DB
```

---

## Project 2 — CI/CD Pipeline

**Skills:** GitHub Actions/Jenkins + Docker

```text
GitHub
  ↓
CI Pipeline
  ↓
Tests
  ↓
Docker Build
  ↓
Docker Hub / ECR
  ↓
Deployment
```

---

## Project 3 — AWS Deployment

**Skills:** AWS + Linux + Docker

Deploy a backend application on EC2.

Add:

- Nginx
- HTTPS
- Domain
- Security Group
- CloudWatch monitoring

---

## Project 4 — Terraform AWS Infrastructure

**Skills:** Terraform + AWS

Create the infrastructure using code instead of manually creating resources.

---

## Project 5 — Kubernetes Deployment

**Skills:** Docker + Kubernetes + Helm

Deploy a multi-container application to Kubernetes.

Add:

- Deployment
- Service
- ConfigMap
- Secret
- Ingress
- Health checks
- Resource limits

---

## Project 6 — Complete DevOps Project ⭐

Build an end-to-end production-style pipeline:

```text
                ┌──────────────┐
                │   Developer  │
                └──────┬───────┘
                       ↓
                  ┌─────────┐
                  │ GitHub  │
                  └────┬────┘
                       ↓
              ┌─────────────────┐
              │ CI/CD Pipeline  │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │ Build + Test    │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │ Docker Image    │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │ Container       │
              │ Registry        │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │ Kubernetes      │
              └────────┬────────┘
                       ↓
              ┌─────────────────┐
              │ Monitoring      │
              │ Prometheus      │
              │ Grafana         │
              └─────────────────┘
```

---

# 📚 Official Documentation Hub

| Technology | Documentation | Main Goal |
|---|---|---|
| Linux | [Docs](https://docs.kernel.org/) | OS & system fundamentals |
| Git | [Docs](https://git-scm.com/doc) | Version control |
| Docker | [Docs](https://docs.docker.com/) | Containers |
| AWS | [Docs](https://docs.aws.amazon.com/) | Cloud |
| Jenkins | [Docs](https://www.jenkins.io/doc/) | CI/CD automation |
| GitHub Actions | [Docs](https://docs.github.com/en/actions) | CI/CD |
| Terraform | [Docs](https://developer.hashicorp.com/terraform/docs) | Infrastructure as Code |
| Ansible | [Docs](https://docs.ansible.com/) | Configuration automation |
| Kubernetes | [Docs](https://kubernetes.io/docs/) | Container orchestration |
| Helm | [Docs](https://helm.sh/docs/) | Kubernetes packages |
| Prometheus | [Docs](https://prometheus.io/docs/) | Metrics |
| Grafana | [Docs](https://grafana.com/docs/) | Dashboards |
| Trivy | [Docs](https://trivy.dev/) | Security scanning |
| OWASP | [Docs](https://owasp.org/) | Application security |

---

# 🎯 What You Should Be Able to Do

After completing this roadmap, aim to be able to:

- [ ] Work comfortably in Linux
- [ ] Use Git and GitHub professionally
- [ ] Write basic Bash scripts
- [ ] Understand networking fundamentals
- [ ] Build and run Docker containers
- [ ] Write Dockerfiles
- [ ] Use Docker Compose
- [ ] Deploy applications on AWS
- [ ] Build CI/CD pipelines
- [ ] Use Jenkins or GitHub Actions
- [ ] Write Terraform configurations
- [ ] Automate servers with Ansible
- [ ] Deploy applications on Kubernetes
- [ ] Package Kubernetes applications with Helm
- [ ] Monitor applications with Prometheus and Grafana
- [ ] Perform basic DevSecOps/security scanning
- [ ] Explain the complete CI/CD workflow in an interview
- [ ] Build at least 2–3 end-to-end DevOps projects

---

# 🧠 How to Study

Use this cycle for every technology:

```text
Learn Concept
     ↓
Read Official Documentation
     ↓
Follow a Small Tutorial
     ↓
Build Something Yourself
     ↓
Break It
     ↓
Debug It
     ↓
Document It
     ↓
Push to GitHub
```

### Important Rule

**Don't learn 15 tools simultaneously.**

Finish the fundamentals of one layer before moving to the next.

For example:

```text
Linux
  ↓
Git
  ↓
Docker
  ↓
Cloud
  ↓
CI/CD
  ↓
Terraform
  ↓
Kubernetes
  ↓
Monitoring
  ↓
Security
```

---

# 💼 Interview Preparation

Prepare questions around:

### Linux
- Process vs thread
- File permissions
- SSH
- systemd
- Logs
- Networking commands

### Git
- Merge vs rebase
- `git reset` vs `git revert`
- Branching strategies
- Merge conflicts

### Docker
- Image vs container
- Dockerfile
- Volumes
- Networks
- Multi-stage builds

### CI/CD
- CI vs CD
- Pipeline stages
- Deployment strategies
- Rollback

### AWS
- EC2
- VPC
- IAM
- Security Groups
- Load Balancers
- Auto Scaling

### Terraform
- State
- `plan` vs `apply`
- Modules
- Providers
- Remote state

### Kubernetes
- Pod vs Deployment
- Service types
- ConfigMap vs Secret
- Ingress
- Probes
- Scaling

### Monitoring
- Metrics vs logs
- Prometheus
- PromQL
- Grafana
- Alerting

---

# ⭐ Recommended Priority

If you are short on time, prioritize:

```text
⭐⭐⭐⭐⭐ Linux
⭐⭐⭐⭐⭐ Git/GitHub
⭐⭐⭐⭐⭐ Docker
⭐⭐⭐⭐⭐ AWS
⭐⭐⭐⭐⭐ CI/CD
⭐⭐⭐⭐⭐ Kubernetes
⭐⭐⭐⭐ Terraform
⭐⭐⭐⭐ Networking
⭐⭐⭐ Ansible
⭐⭐⭐ Helm
⭐⭐⭐ Prometheus/Grafana
⭐⭐ Security / DevSecOps
```

---

# 🏁 Final Goal

The objective is **not** to collect certificates or finish playlists.

The objective is to reach this point:

> **"I can take an application from source code → build → test → containerize → provision infrastructure → deploy → monitor → troubleshoot."**

That is the mindset to target for a **job-ready DevOps Engineer**.

---

## ⭐ Repository Idea

Keep your own practical work in folders like:

```text
devops-learning/
│
├── linux/
├── bash/
├── git/
├── docker/
├── docker-compose/
├── aws/
├── github-actions/
├── jenkins/
├── terraform/
├── ansible/
├── kubernetes/
├── helm/
├── monitoring/
├── security/
└── projects/
```

Use this repository as your **DevOps learning journal + portfolio**.
