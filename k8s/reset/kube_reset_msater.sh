#!/bin/bash

kubeadm reset -f

systemctl restart kubelet

rm -rf /etc/cni/net.d/*

rm -rf /var/lib/etcd

rm -rf /var/lib/kubelet/*

rm -rf /etc/kubernetes

rm -rf $HOME/.kube/config

systemctl restart containerd

systemctl daemon-reexec

systemctl restart kubelet

kubeadm init --apiserver-advertise-address=192.168.1.111
