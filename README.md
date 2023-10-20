По  сертифікатам API Kubernetes:

1. Отримання сертифікату:
   - Так само треба взяти сертифікат Let`s Encrypt. Я використовував  Cert-Manager для автоматичного отримання та поновлення сертифікатів.

2. Збереження сертифіката:
 В мене вони зберігаються  :
API Kubernetes: в /etc/kubernetes/pki/apiserver.crt
Приватні ключі: в etc/kubernetes/pki/apiserver.key


3. Конфігурація API сервера:
   - Додав у файл розташування API та приватних ключів у файл у `/etc/kubernetes/manifests/kube-apiserver.yaml`.Можна використовувати параметри `--tls-cert-file` та `--tls-private-key-file`, щоб вказати шляхи до сертифіката та ключа. Сам файл: 1.yaml

4. Перезапуск API сервера:
   - Перезапустити командою  `kubectl delete pod kube-apiserver-control -n kube-system`. 
   kubectl get componentstatuses- для перевірки стану API сервера
