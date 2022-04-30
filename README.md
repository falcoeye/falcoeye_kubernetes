# falcoeye_kubernetes
k8s config files for falcoeye

```python
from falcoeye_kubernetes import FalcoServingKube

resnet = FalcoServingKube("resnet")

# to deploy Resnet deployment
resnet.start()

# to check if deployed
resnet.is_running()

# to get IP address
resnet.get_service_address()

# to delete deployment
resnet.delete_deployment()

# to delete service
resnet.delete_service()

```
