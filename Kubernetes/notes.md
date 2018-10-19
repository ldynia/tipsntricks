# Kubernetes


[install kubeadm](https://kubernetes.io/docs/setup/independent/install-kubeadm/)

[install kubernetes cluster in VM](https://medium.com/@KevinHoffman/building-a-kubernetes-cluster-in-virtualbox-with-ubuntu-22cd338846dd)
[install kubernetes cluster in VM](https://itnext.io/kubernetes-on-ubuntu-on-virtualbox-60e8ce7c85ed)
[install kubernetes cluster in VM](https://developers.caffeina.com/a-kubernetes-cluster-on-virtualbox-20d64666a678)



https://www.techrepublic.com/article/how-to-install-a-kubernetes-cluster-on-centos-7/

https://www.digitalocean.com/community/tutorials/how-to-create-a-kubernetes-1-10-cluster-using-kubeadm-on-centos-7


https://itnext.io/kubernetes-on-ubuntu-on-virtualbox-60e8ce7c85ed

https://medium.com/@KevinHoffman/building-a-kubernetes-cluster-in-virtualbox-with-ubuntu-22cd338846dd


```bash
# check uuid
$ sudo cat /sys/class/dmi/id/product_uuid

# init and create join token
$ kubeadm init
$ kubeadm token create --print-join-command
```

### Restart kubelet service
```bash
$ kubeadm reset
$ systemctl restart kubelet
$ kubeadm init
```
