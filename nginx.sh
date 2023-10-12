helm repo add nginx-stable https://helm.nginx.com/stable
helm repo update
helm install nginx-kic nginx-stable/nginx-ingress --namespace nginx-ingress --set controller.enableCustomResources=true --create-namespace --set controller.enableCertManager=true
