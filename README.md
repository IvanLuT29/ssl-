# ssl-
Застосування Jetstack's cert-manager, Let's Encrypt і NGINX Ingress Controller у вашому проекті допоможе автоматизувати управління SSL/TLS-сертифікатами і забезпечити безпеку з'єднань для вашого додатку в середовищі Kubernetes. Ось кроки для використання цих технологій у вашому проекті:

1. Установіть Kubernetes та Helm: Перш за все, переконайтеся, що у вас є Kubernetes кластер і Helm встановлені в вашому проекті. Helm допоможе вам керувати розгортанням додатків та іншими ресурсами.

2. Розгортайте NGINX Ingress Controller:

    - Для цього скористайтеся Helm для розгортання NGINX Ingress Controller. Виконайте наступні команди, щоб додати репозиторій і розгорнути контролер:
    
    #nginx.sh

    Це дозволить вам використовувати NGINX Ingress Controller для маршрутизації трафіку у вашому кластері Kubernetes.

3. Встановити cert-manager:
    #cert-manager.sh
    Cert-manager допомагатиме вам автоматизувати управління сертифікатами.

4. **Настройте ClusterIssuer:**

    - Створіть ClusterIssuer для видання сертифікатів, визначте тип виклику (HTTP-01 або DNS-01), та вкажіть необхідні параметри, такі як електронна адреса, сервер, і інші параметри.

    4.1. **HTTP-01 Challenge:** Якщо ви використовуєте HTTP-01, ваша конфігурація ClusterIssuer може виглядати приблизно так:

    ```yaml
    apiVersion: cert-manager.io/v1
    kind: ClusterIssuer
    metadata:
      name: prod-issuer
    spec:
      acme:
        email: example@example.com
        server: https://acme-v02.api.letsencrypt.org/directory
        privateKeySecretRef:
          name: prod-issuer-account-key
        solvers:
        - http01:
            ingress:
              class: nginx
    ```

    4.2. **DNS-01 Challenge:** Якщо ви використовуєте DNS-01, ваша конфігурація ClusterIssuer може виглядати приблизно так:

    ```yaml
    apiVersion: cert-manager.io/v1
    kind: ClusterIssuer
    metadata:
      name: prod-issuer
    spec:
      acme:
        email: example@example.com
        server: https://acme-v02.api.letsencrypt.org/directory
        privateKeySecretRef:
          name: prod-issuer-account-key
        solvers:
        - dns01:
            cloudflare:
              apiTokenSecretRef:
                name: cloudflare-api-token-secret
                key: api-token
    ```

    В даному прикладі використовується Cloudflare як провайдер DNS, і потрібно мати API-токен від Cloudflare.

5. **Створіть Ingress:**

    - Створіть Ingress ресурс для вашого додатку. У цьому ресурсі ви можете вказати маршрути для вашого додатку та налаштувати отриманий сертифікат.

    Наприклад, якщо ви використовуєте стандартний Kubernetes Ingress, ваша конфігурація може виглядати приблизно так:

    ```yaml
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: cafe-ingress
      annotations:
        cert-manager.io/cluster-issuer: prod-issuer
        acme.cert-manager.io/http01-edit-in-place: "true"
    spec:
      ingressClassName: nginx
      tls:
      - hosts:
        - cert.example.com
        secretName: cafe-secret
      rules:
      - host: cert.example.com
        http:
          paths:
          - path: /tea
            pathType: Prefix
            backend:
              service:
                name: tea-svc
                port:
                  number: 80
          - path: /coffee
            pathType: Prefix
            backend:
              service:
                name: coffee-svc
                port:
                  number: 80
    ```

    Важливо налаштувати `cert-manager.io/cluster-issuer` на ім'я вашого ClusterIssuer і підставити ваші дан
