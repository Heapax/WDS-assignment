#!/bin/bash

set -e

echo "Deploying nasa-query job..."
echo "Creating nasa-query namespace..."
kubectl apply -f nasa-query-ns.yaml
echo "nasa-query namespace created"

echo "Creating nasa-query service account..."
kubectl apply -f nasa-query-sa.yaml
echo "nasa-query service account created"

echo "Creating nasa-query network policies..."
kubectl apply -f default-deny-all-np.yaml
echo "default deny all network policy created"
kubectl apply -f allow-dns-and-external-egress-np.yaml
echo "allow dns and external egress network policy created"

echo "Creating nasa-query RBAC role and rolebinding..."
kubectl apply -f nasa-query-role.yaml
echo "nasa-query role created"
kubectl apply -f nasa-query-role-binding.yaml
echo "nasa-query rolebinding created"

echo "Creating nasa-query persistent volume and persistent volume claim..."
kubectl apply -f nasa-data-pv.yaml
echo "nasa-data persistent volume created"
kubectl apply -f nasa-data-pvc.yaml
echo "nasa-data persistent volume claim created"

echo "Creating nasa-query job..."
kubectl apply -f nasa-query-job.yaml
echo "nasa-query job created"
