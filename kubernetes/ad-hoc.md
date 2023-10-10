kubeadm init --apiserver-advertise-address=10.128.29.51 --pod-network-cidr=10.244.0.0/16
kubeadm token create --print-join-command


mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config


kubeadm join 10.128.29.51:6443 --token uds7vm.yknayvnihx4776we --discovery-token-ca-cert-hash sha256:17e39d7bb885d4b88b36543e01d4ad6f259ebe187d9573cd11e8d33debbe1d71


kubectl apply -n kube-system -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 |tr -d '\n')"



----------
https://www.admintome.com/blog/accessing-kubernetes-dashboard/

kubectl create -f https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/recommended/kubernetes-dashboard.yaml


kubectl proxy --accept-hosts='^.*$' --address='10.128.29.51' &
kubectl proxy --accept-hosts='^.*$' --address=$(hostname -i) &

--- dashboard

http://10.128.29.51:8001/api/v1/namespaces/kube-system/services/kubernetes-dashboard/

http://10.128.29.51:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/



