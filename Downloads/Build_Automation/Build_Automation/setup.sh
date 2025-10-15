# Quick Setup Script for CI/CD Demo

echo "🚀 Setting up CI/CD Demo Project..."

# Install dependencies
echo "📦 Installing dependencies..."
npm install

# Create .env file from example
echo "⚙️ Creating environment file..."
cp env.example .env

# Build Docker image locally
echo "🐳 Building Docker image..."
docker build -t cicd-demo-app .

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Update k8s/deployment.yaml with your Docker Hub username"
echo "2. Configure GitHub secrets (DOCKERHUB_USERNAME, DOCKERHUB_TOKEN, KUBECONFIG)"
echo "3. Push to GitHub to trigger the CI/CD pipeline"
echo ""
echo "Test locally:"
echo "- Run app: npm start"
echo "- Test Docker: docker run -p 3000:3000 cicd-demo-app"
echo "- Test K8s: kubectl apply -f k8s/"
