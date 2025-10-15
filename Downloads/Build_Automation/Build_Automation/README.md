# CI/CD Demo Project

A complete demonstration of CI/CD pipeline using GitHub Actions, Docker, and Kubernetes.

## 🚀 Features

- **Automated Testing**: Runs tests on every push and pull request
- **Docker Build**: Multi-platform container builds (AMD64/ARM64)
- **Registry Push**: Automatic push to Docker Hub
- **Kubernetes Deployment**: Automated deployment to K8s cluster
- **Health Checks**: Built-in health monitoring
- **Rolling Updates**: Zero-downtime deployments

## 📋 Prerequisites

### Required Accounts & Services
- GitHub account
- Docker Hub account (or GitHub Container Registry)
- Kubernetes cluster (local, cloud, or managed)

### Required Tools (for local development)
- Node.js 18+
- Docker
- kubectl
- Git

## 🛠️ Setup Instructions

### 1. Fork/Clone Repository
```bash
git clone <your-repo-url>
cd cicd-demo-app
npm install
```

### 2. Configure GitHub Secrets

Go to your GitHub repository → Settings → Secrets and variables → Actions

Add the following secrets:

#### Docker Hub Secrets
- `DOCKERHUB_USERNAME`: Your Docker Hub username
- `DOCKERHUB_TOKEN`: Your Docker Hub access token

#### Kubernetes Secrets
- `KUBECONFIG`: Base64 encoded kubeconfig file

To get your kubeconfig:
```bash
# Get your kubeconfig
cat ~/.kube/config | base64 -w 0
```

### 3. Update Kubernetes Manifests

Edit `k8s/deployment.yaml` and replace `YOUR_DOCKERHUB_USERNAME` with your actual Docker Hub username:

```yaml
image: yourusername/cicd-demo-app:latest
```

### 4. Test Locally

#### Run the application:
```bash
npm start
# Visit http://localhost:3000
```

#### Build Docker image:
```bash
docker build -t cicd-demo-app .
docker run -p 3000:3000 cicd-demo-app
```

#### Test Kubernetes deployment:
```bash
kubectl apply -f k8s/
kubectl get pods
kubectl get services
```

## 🔄 CI/CD Pipeline Flow

### Pipeline Stages

1. **Test Stage**
   - Checkout code
   - Setup Node.js environment
   - Install dependencies
   - Run tests and linting

2. **Build & Push Stage**
   - Build Docker image for multiple platforms
   - Push to Docker Hub with tags
   - Cache layers for faster builds

3. **Deploy Stage** (main branch only)
   - Update deployment with new image tag
   - Apply Kubernetes manifests
   - Wait for rollout completion
   - Verify deployment

4. **Notify Stage**
   - Send deployment status notifications

### Trigger Conditions

- **Push to `main`**: Full pipeline (test → build → push → deploy)
- **Push to `develop`**: Test and build only
- **Pull Request**: Test only

## 📁 Project Structure

```
cicd-demo-app/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions workflow
├── k8s/
│   ├── deployment.yaml        # Kubernetes deployment
│   ├── service.yaml           # Kubernetes service
│   └── ingress.yaml           # Kubernetes ingress
├── app.js                     # Main application file
├── package.json               # Node.js dependencies
├── Dockerfile                 # Docker configuration
├── .dockerignore             # Docker ignore file
└── README.md                  # This file
```

## 🌐 Application Endpoints

- `GET /` - Main application info
- `GET /health` - Health check endpoint
- `GET /api/info` - Application information

## 🔧 Customization

### Environment Variables
- `PORT`: Application port (default: 3000)
- `NODE_ENV`: Environment (development/production)
- `APP_VERSION`: Application version

### Kubernetes Configuration
- Modify `k8s/deployment.yaml` for resource limits
- Update `k8s/service.yaml` for service type
- Configure `k8s/ingress.yaml` for external access

### Docker Configuration
- Update `Dockerfile` for different base images
- Modify `.dockerignore` for build optimization

## 🚨 Troubleshooting

### Common Issues

1. **Docker Hub Authentication**
   - Verify `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` secrets
   - Check token permissions

2. **Kubernetes Deployment Fails**
   - Verify `KUBECONFIG` secret is base64 encoded
   - Check cluster connectivity
   - Ensure image exists in registry

3. **Build Failures**
   - Check Dockerfile syntax
   - Verify all dependencies in package.json
   - Review GitHub Actions logs

### Debug Commands

```bash
# Check Kubernetes cluster status
kubectl cluster-info

# View pod logs
kubectl logs -l app=cicd-demo-app

# Check service endpoints
kubectl get endpoints

# Describe deployment
kubectl describe deployment cicd-demo-app
```

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Docker Hub](https://hub.docker.com/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Happy Deploying! 🚀**
