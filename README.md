To obtain a new certificate for a new deployment or service via cert-manager in Kubernetes, you need to specify in your Ingress or CertificateRequest resource that the new certificate is for a host or service. Here are the steps to do so:

1. Add Ingress or CertificateRequest

    You can use either Ingress or CertificateRequest, depending on how you plan to obtain the certificate.
    Ingress: If using Ingress for an application, simply add or update the Ingress resource and specify the new host that needs the certificate.

    For cert-manager, this would mean that it needs to take a certificate for the new host new-app.example.com.

2. Start the certificate handler:
    cert-manager will detect a new Ingress or CertificateRequest if configured correctly and try to request the certificate automatically. After successful issuance of the certificate, it will be saved in the prompted secretName. storage path : /etc/kubernetes/secrets/namespace_name/secret_name

3. Now the new deployment or service will have SSL/TLS protection with  a new certificate that was automatically generated via cert-manager.
cert-manager will monitor the validity period of certificates and, if necessary, update them or request a new certificate.