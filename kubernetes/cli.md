# Handy CLI commands

## Get TLS certificates expiery date

```bash
for out in $(kubectl get secrets --field-selector type=kubernetes.io/tls --all-namespaces --no-headers | awk '{print $1 "," $2}'); do
    namespace=$(echo $out | cut -d "," -f 1)
    secret=$(echo $out | cut -d "," -f 2)
    expiry=$(kubectl get secret $secret -n $namespace -o "jsonpath={.data['tls\.crt']}" | base64 -d | openssl x509 -enddate -noout)
    echo $secret "in" $namespace "expiring" $expiry 
done
```
