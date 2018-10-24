# Kubernetes


[playground](https://labs.play-with-k8s.com)

[install kubeadm](https://kubernetes.io/docs/setup/independent/install-kubeadm/)

[install kubernetes cluster in VM](https://medium.com/@KevinHoffman/building-a-kubernetes-cluster-in-virtualbox-with-ubuntu-22cd338846dd)

[install kubernetes cluster in VM](https://itnext.io/kubernetes-on-ubuntu-on-virtualbox-60e8ce7c85ed)
[install kubernetes cluster in
VM](https://developers.caffeina.com/a-kubernetes-cluster-on-virtualbox-20d64666a678)


[network](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/)

[link](https://www.techrepublic.com/article/how-to-install-a-kubernetes-cluster-on-centos-7/
)

[link](https://www.digitalocean.com/community/tutorials/how-to-create-a-kubernetes-1-10-cluster-using-kubeadm-on-centos-7
)

[link](https://itnext.io/kubernetes-on-ubuntu-on-virtualbox-60e8ce7c85ed)

[link](https://medium.com/@KevinHoffman/building-a-kubernetes-cluster-in-virtualbox-with-ubuntu-22cd338846dd)

### Set network

**Flannel** to work correctly, you must pass `--pod-network-cidr=10.244.0.0/16` to kubeadm init.



```bash
# Set /proc/sys/net/bridge/bridge-nf-call-iptables to 1
$ sysctl net.bridge.bridge-nf-call-iptables=1

# Install network
$ kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/bc79dd1505b0c8681ece4de4c0d86c5cd2643275/Documentation/kube-flannel.yml

# Check if networking is working
$ kubectl get pods --all-namespaces
```

### Start Kluster
```bash
# check machine's uuid
$ sudo cat /sys/class/dmi/id/product_uuid
```

```bash
# init and create join token
$ kubeadm init --apiserver-advertise-address=$(hostname -i) --pod-network-cidr=10.244.0.0/16

# copy newly created config files
$ mkdir -p $HOME/.kube
$ sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
$ sudo chown $(id -u):$(id -g) $HOME/.kube/config

# reprint token
$ kubeadm token create --print-join-command

# display nodes
$ kubctl get nodes
```

### Restart kubelet service
```bash
$ kubeadm reset
$ systemctl restart kubelet
```
