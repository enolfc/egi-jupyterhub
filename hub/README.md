# Some notes


## Secrets 

This expects some secrets to be available to the service related to the CheckIn integration:

```
kubectl create secret generic --namespace jupyterhub jupyterhub \
        --from-literal=oauth-client-id=${OAUTH_CLIENT_ID} \
        --from-literal=oauth-client-secret=${OAUTH_CLIENT_SECRET} \
        --from-literal=oauth-callback-url=https://${SUBDOMAIN}/hub/oauth_callback 
```

## NFS

NFS should be accessible from every Kubernetes node. Working setup:
```
/exports nodeip(rw,root_squash)
```
