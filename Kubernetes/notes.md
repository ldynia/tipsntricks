# Kubernetes


[kubernetesbyexample.com](http://kubernetesbyexample.com/)
[playground](https://labs.play-with-k8s.com)

[install kubeadm](https://kubernetes.io/docs/setup/independent/install-kubeadm/)

[install kubernetes cluster in VM](https://medium.com/@KevinHoffman/building-a-kubernetes-cluster-in-virtualbox-with-ubuntu-22cd338846dd)

[install kubernetes cluster in VM](https://itnext.io/kubernetes-on-ubuntu-on-virtualbox-60e8ce7c85ed)
[install kubernetes cluster in
VM](https://developers.caffeina.com/a-kubernetes-cluster-on-virtualbox-20d64666a678)


[network](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/)

[link](https://www.techrepublic.com/article/how-to-install-a-kubernetes-cluster-on-centos-7/)

[link](https://www.digitalocean.com/community/tutorials/how-to-create-a-kubernetes-1-10-cluster-using-kubeadm-on-centos-7)

[link](https://itnext.io/kubernetes-on-ubuntu-on-virtualbox-60e8ce7c85ed)

[link](https://medium.com/@KevinHoffman/building-a-kubernetes-cluster-in-virtualbox-with-ubuntu-22cd338846dd)

### Set network

**Flannel** to work correctly, you must pass `--pod-network-cidr=10.244.0.0/16` to kubeadm init.

```bash
# Set /proc/sys/net/bridge/bridge-nf-call-iptables to 1
$ sysctl net.bridge.bridge-nf-call-iptables=1

# Install Flannel network -  You might run it as none root user
$ kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/bc79dd1505b0c8681ece4de4c0d86c5cd2643275/Documentation/kube-flannel.yml

# For Kubernetes v1.7+
$ kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml


# Install Wave Net
$ kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"
```

### Start Kluster
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
$ export KUBECONFIG=/etc/kubernetes/kubelet.conf
$ kubectl get nodes

# copy newly created config files as a non root user (normal user)
$ mkdir -p $HOME/.kube
$ sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
$ sudo chown $(id -u):$(id -g) $HOME/.kube/config

# reprint token
$ kubeadm token create --print-join-command

# Validate if cluster is setup correctly
$ kubectl version
$ kubectl cluster-info
$ kubectl get nodes
$ kubectl get componentstatus
```

### Restart kubelet service
```bash
$ kubeadm reset
$ systemctl restart kubelet
```

### Dashboard

```bash
$ kubectl create -f https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/recommended/kubernetes-dashboard.yaml

$ kubectl get svc -n kube-system
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)         AGE
kube-dns               ClusterIP   10.96.0.10      <none>        53/UDP,53/TCP   33h
kubernetes-dashboard   NodePort    10.101.11.169   <none>        80:31000/TCP    5m23

$ curl 10.101.11.169
$ curl $(hostname -i):31000
```


### Create pod
```bash
$ kubectl get pods
$ kubectl get pods --all-namespaces
$ kubectl get pods --all-namespaces -o wide

$ kubectl run -i --tty busybox2 --image=busybox --restart=Never -- sh
$ kubectl exec -it busybox2 -- sh
$ kubectl exec -it busybox2 -- nslookup httpd
```

### Access container within a pod
```bash
$ kubectl exec -it <PODNAME> -c <CONTAINER_NAME> -- bash
```

### Deployments
```bash
$ kubectl get deployments --all-namespaces -o wide
$ kubectl scale --replicas=5 -f dep-nginx.yaml
$ kubectl -n demo get deployments
$ kubectl -n demo get rs
```

### Ingress
[Tutorial](https://medium.com/@Oskarr3/setting-up-ingress-on-minikube-6ae825e98f82)
[Kubernetes !!!! Nginx Ingress Controller Instalation](https://github.com/kubernetes/ingress-nginx)

```bash
# Mandatory step
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/mandatory.yaml

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

# Create load balancing service using LoadBalancer or NodePort svc-ingress-nginx-lb.yaml
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
