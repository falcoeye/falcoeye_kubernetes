# First clean up
minikube delete
docker system prune -f

# Start with modified settings
# minikube start --driver=docker --cpus=8 --memory=32000 \
#   --extra-config=kubelet.cpu-manager-policy=static \
#   --extra-config=kubelet.cgroup-driver=cgroupfs \
#   --feature-gates="AllowInsecureOptions=true" \
#   --bootstrapper=kubeadm \
#   --extra-config=kubelet.authentication-token-webhook=true

minikube start --driver=docker --cpus=8 --memory=32000 \
  --kubernetes-version=v1.28.0  # Using a more stable version