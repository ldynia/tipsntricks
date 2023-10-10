# SSL Cert

```bash
$ openssl genrsa -out private.key 4096
$ openssl req -new -sha256 -config ssl.conf -key private.key -out cert.csr

# Generate certnew.cer - Missing step

# Chain certnew.cer with CA cert
$ cat certnew.cer WebCA.cer > chain.crt

# Generate PFX (with empty password)
$ openssl pkcs12 -in chain.crt -inkey private.key -out certificate.pfx  -export 
```

## Inspect Certificate

```bash
 $ openssl x509 -text -noout -in cert.cer
 $ openssl x509 -inform der -in CERTIFICATE.der -text -noout
 ```
 
 ## Conver DER.cer to PEM
 ```bash
 openssl x509 -inform der -in certificate.cer -out certificate.pem
 ```
