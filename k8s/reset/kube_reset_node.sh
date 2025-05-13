kubeadm reset -f

systemctl restart kubelet

scp master:/root/.kube/token .kube/

.kube/token
