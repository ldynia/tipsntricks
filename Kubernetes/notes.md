# Kubernetes
[kubernetesbyexample.com](http://kubernetesbyexample.com/)
[kubernetes bootcamp](https://schoolofdevops.github.io/ultimate-kubernetes-bootcamp/)
[playground](https://labs.play-with-k8s.com)
[link](https://www.techrepublic.com/article/how-to-install-a-kubernetes-cluster-on-centos-7/)
[link](https://www.digitalocean.com/community/tutorials/how-to-create-a-kubernetes-1-10-cluster-using-kubeadm-on-centos-7)
[link](https://itnext.io/kubernetes-on-ubuntu-on-virtualbox-60e8ce7c85ed)
[link](https://medium.com/@KevinHoffman/building-a-kubernetes-cluster-in-virtualbox-with-ubuntu-22cd338846dd)



# Installation
[install kubeadm](https://kubernetes.io/docs/setup/independent/install-kubeadm/)
[install kubernetes cluster in VM I](https://medium.com/@KevinHoffman/building-a-kubernetes-cluster-in-virtualbox-with-ubuntu-22cd338846dd)
[install kubernetes cluster in VM II](https://itnext.io/kubernetes-on-ubuntu-on-virtualbox-60e8ce7c85ed)
[install kubernetes cluster in VM III](https://developers.caffeina.com/a-kubernetes-cluster-on-virtualbox-20d64666a678)

## Networking
[network](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/)

**Flannel** to work correctly, you must pass `--pod-network-cidr=10.244.0.0/16` to kubeadm init.

```bash
# Set /proc/sys/net/bridge/bridge-nf-call-iptables to 1
$ sysctl net.bridge.bridge-nf-call-iptables=1

# Install Wave Net
$ kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"

# Install Flannel network -  You might run it as none root user. Second link is for Kubernetes v1.7+
$ kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/bc79dd1505b0c8681ece4de4c0d86c5cd2643275/Documentation/kube-flannel.yml
$ kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```

## Metrics
```bash
$ git clone  https://github.com/kubernetes-incubator/metrics-server.git
$ kubectl apply -f kubectl create -f metrics-server/deploy/1.8+/

# Fix  issue as off Dec 2018 with Metrics Server
$ wget -c https://gist.githubusercontent.com/initcron/1a2bd25353e1faa22a0ad41ad1c01b62/raw/008e23f9fbf4d7e2cf79df1dd008de2f1db62a10/k8s-metrics-server.patch.yaml
$ kubectl patch deploy metrics-server -p "$(cat k8s-metrics-server.patch.yaml)" -n kube-system
```


## Ingress Traefik

[user-guide](https://docs.traefik.io/user-guide/kubernetes/)

```bash
$ kubectl apply -f https://raw.githubusercontent.com/containous/traefik/master/examples/k8s/traefik-rbac.yaml
```

```yaml
# traefik-ds.yaml
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: traefik-ingress-controller
  namespace: kube-system
---
kind: DaemonSet
apiVersion: extensions/v1beta1
metadata:
  name: traefik-ingress-controller
  namespace: kube-system
  labels:
    k8s-app: traefik-ingress-lb
spec:
  template:
    metadata:
      labels:
        k8s-app: traefik-ingress-lb
        name: traefik-ingress-lb
    spec:
      hostNetwork: true
      serviceAccountName: traefik-ingress-controller
      terminationGracePeriodSeconds: 60
      containers:
      - image: traefik
        name: traefik-ingress-lb
        ports:
        - name: http
          containerPort: 80
        - name: admin
          containerPort: 8080
        securityContext:
          capabilities:
            drop:
            - ALL
            add:
            - NET_BIND_SERVICE
        args:
        - --api
        - --kubernetes
        - --logLevel=INFO
---
kind: Service
apiVersion: v1
metadata:
  name: traefik-ingress-service
  namespace: kube-system
  labels:
    k8s-app: traefik-ingress-lb
spec:
  selector:
    k8s-app: traefik-ingress-lb
  ports:
    - protocol: TCP
      port: 80
      name: web
    - protocol: TCP
      port: 8080
      name: admin
```

```bash
# Create DaemonSet
$ kubectl apply -f traefik-ds.yaml
# $ kubectl apply -f https://raw.githubusercontent.com/containous/traefik/master/examples/k8s/traefik-deployment.yaml
```

## Ingress Nginx
[Tutorial](https://medium.com/@Oskarr3/setting-up-ingress-on-minikube-6ae825e98f82)
[Kubernetes !!!! Nginx Ingress Controller Instalation](https://github.com/kubernetes/ingress-nginx)

**Installation of nginx ingress controller**
```bash
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/mandatory.yaml
```

```bash
# Inspiration from minikube -check commented lines
- /nginx-ingress-controller
  #- --default-backend-service=$(POD_NAMESPACE)/default-http-backend
  - --configmap=$(POD_NAMESPACE)/nginx-configuration
  #- --configmap=$(POD_NAMESPACE)/nginx-load-balancer-conf
  - --tcp-services-configmap=$(POD_NAMESPACE)/tcp-services
  - --udp-services-configmap=$(POD_NAMESPACE)/udp-services
  - --publish-service=$(POD_NAMESPACE)/ingress-nginx
  - --annotations-prefix=nginx.ingress.kubernetes.io
  #- --report-node-internal-ip-address
```

**Service Deployment**
```yaml
# svc-ingress-nginx-lb.yaml -Create load balancing service using LoadBalancer or NodePort
# link: https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/provider/cloud-generic.yaml
kind: Service
apiVersion: v1
metadata:
  name: ingress-nginx
  namespace: ingress-nginx
  labels:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
spec:
  #type: NodePort
  type: LoadBalancer
  externalTrafficPolicy: Local
  externalIPs:
  - 192.168.121.110
  - 192.168.121.111
  - 192.168.121.112
  - 192.168.121.113
  selector:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
  ports:
    - name: http
      port: 80
      targetPort: http
    - name: https
      port: 443
      targetPort: https
```


```bash
# Create service or apply for already deployed services
$ kubectl apply -f svc-ingress-nginx-lb.yaml

# Verify installation and version of the controller
$ kubectl get svc -n ingress-nginx
$ kubectl get deploy -n ingress-nginx
$ kubectl get pods --all-namespaces -l app.kubernetes.io/name=ingress-nginx
$ kubectl exec -it <POD_NAME> -n ingress-nginx -- /nginx-ingress-controller --version

# Trubeleshooting
$ kubectl describe nodes
```

## Metrics Server

```bash
$ git clone  https://github.com/kubernetes-incubator/metrics-server.git
$ kubectl apply -f metrics-server/deploy/1.8+/
```


# Cluster
```bash
# check machine's uuid
$ sudo cat /sys/class/dmi/id/product_uuid
```

```bash
# init and create join token for Flannel
$ kubeadm init --apiserver-advertise-address=$(hostname -i) --pod-network-cidr=10.244.0.0/16

# init and create join token for Wave Net
$ kubeadm init --apiserver-advertise-address=$(hostname -i)

# You might do this
$ export KUBECONFIG=$HOME/.kube/config
$ export KUBECONFIG=/etc/kubernetes/kubelet.conf
$ kubectl get nodes

# copy newly created config files as a non root user (normal user)
$ mkdir -p $HOME/.kube
$ sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
$ sudo chown $(id -u):$(id -g) $HOME/.kube/
$ sudo chown $(id -u):$(id -g) $HOME/.kube/config

# reprint token
$ kubeadm token create --print-join-command

# Validate if cluster is setup correctly
$ kubectl version
$ kubectl cluster-info
$ kubectl get nodes
$ kubectl get componentstatuses

# Restart kubelet service
$ kubeadm reset
$ systemctl restart kubelet
```

# Dashboard & Visualizer
## Dashboard
```bash
$ kubectl create -f https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/recommended/kubernetes-dashboard.yaml
$ kubectl get svc -n kube-system
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)         AGE
kube-dns               ClusterIP   10.96.0.10      <none>        53/UDP,53/TCP   33h
kubernetes-dashboard   NodePort    10.101.11.169   <none>        80:31000/TCP    5m23

$ curl 10.101.11.169
$ curl $(hostname -i):31000
```

## Visualizer
```bash
# Set up visualizer
$ git clone  https://github.com/schoolofdevops/kube-ops-view
$ kubectl apply -f kube-ops-view/deploy/
$ kubectl get svc kube-ops-view
NAME            TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
kube-ops-view   NodePort   10.96.72.110   <none>        80:32105/TCP   26h

# On host execute
http://node_ip:32105/#scale=1.0
```

# Pod
```bash
# Dry run - test
$ kubectl apply -f <FILE.yaml> --dry-run

$ kubectl get pods
$ kubectl get pods --all-namespaces
$ kubectl get pods --all-namespaces -o wide
$ kubectl get pod <POD_NAME> -o yaml
$ kubectl get pods --show-labels

$ kubectl describe <POD_NAME>

$ kubectl run -i --tty busybox2 --image=busybox --restart=Never -- sh
$ kubectl exec -it busybox2 -- sh
$ kubectl exec -it busybox2 -- nslookup httpd

$ kubectl exec -it <POD_NAME>  sh
$ kubectl exec -it <POD_NAME> -c <CONTAINER_NAME> -- bash

$ kubectl port-forward <POD_NAME> GUEST_PORT:CONTAINER_PORT

$ kubectl edit <POD_NAME>

$ kubectl logs -f <POD_NAME>
$ kubectl logs -f <POD_NAME> -c <CONTAINER_NAME>

$ kubectl delete <POD_NAME>
```

# Voluems
```yaml
  # Container declaration
  volumeMounts:
    - name: pg-data
      mountPath: /var/lib/postgresql/data
    - name: data
      mountPath: /var/www/app
# Pod declaration
volumes:
  - name: pg-data
    hostPath:
      path: /var/lib/postgres
      type: DirectoryOrCreate
  # Temporary directory
  - name: data
    emptyDir: {}
```

# Namespace
```bash
$ kubectl --namespace=<INSERT-NAMESPACE-NAME-HERE> run nginx --image=nginx
$ kubectl --namespace=<INSERT-NAMESPACE-NAME-HERE> get pods

# Change view
$ kubectl create ns <NAMESPACE>
$ kubectl config set-context $(kubectl config current-context) --namespace=<NAMESPACE>
```

# ReplicaSet
```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: vote
spec:
  replicas: 5
  minReadySeconds: 20
  selector:
    matchLabels:
      role: vote
    matchExpressions:
      - {key: version, operator: In, values: [v1, v2, v3]}
  template:
    metadata:
      name: vote
      labels:
        app: python
        role: vote
        version: v1
    spec:
      containers:
        - name: app
          image: schoolofdevops/vote:v1
          ports:
            - containerPort: 80
              protocol: TCP
````

```bash
$ kubectl get pods --show-labels
$ kubectl get rs
$ kubectl edit rs/vote
$ kubectl describe rs vote
```


# Deployments
```bash
$ kubectl get deployments --all-namespaces -o wide
$ kubectl scale --replicas=5 -f dep-nginx.yaml
$ kubectl -n <NAMESPACE> get deployments
$ kubectl -n <NAMESPACE> get rs
$ kubectl rollout status deployment <NAME>
$ kubectl rollout pause deployment <NAME>
$ kubectl rollout history deployment <NAME>
$ kubectl rollout undo deployment <NAME> --to-revision=1
```

# ConfigMaps

```yaml
# vote-cm.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: vote
  namespace: instavote
data:
  OPTION_A: Visa
  OPTION_B: Mastercard
```

```bash
$ kubectl apply -f vote-cm.yaml
$ kubectl get cm
$ kubectl edit cm <NAME>
```

#### From File
```yaml
volumeMounts:
  - name: redis
    subPath: redis.conf
    mountPath: /etc/redis.conf
volumes:
- name: redis
configMap:
  name: redis
restartPolicy: Always
```

```bash
$ kubectl create configmap --from-file  redis.conf redis
```

#### Secrets

```bash
$ echo "admin" | base64
$ echo "password" | base64
```

```yaml
# db-secrets.yaml
apiVersion: v1
kind: Secret
metadata:
  name: db
  namespace: instavote
type: Opaque
data:
  POSTGRES_USER: YWRtaW4=
  POSTGRES_PASSWD: cGFzc3dvcmQ=
```

```bash
$ kubectl apply -f db-secrets.yaml
$ kubectl get secrets
```
