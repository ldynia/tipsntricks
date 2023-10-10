# Self Signed sert

ssl.conf
```
[req]
default_bits        = 4096
distinguished_name  = req_distinguished_name
prompt              = no
req_extensions      = req_ext

[ca]
default_ca  = CA_default

[CA_default]

default_days      = 365
default_crl_days  = 30
default_md        = sha1

[req_distinguished_name]
commonName                  = acme.com
countryName                 = DK
localityName                = Copenhagen
organizationName            = ACME
organizationalUnitName      = IT
stateOrProvinceName         = Denmark

[req_ext]
subjectAltName = @alt_names

[alt_names]
DNS.1 = localhost
IP.1  = 0.0.0.0
IP.2  = 127.0.0.1
```

```shell
openssl req -x509 -newkey rsa:4096 -keyout /etc/ssl/private/private-key.pem -config /usr/src/config/ssl.conf -out /etc/ssl/private/certificate.pem -passout pass:foobar
chmod 600 /etc/ssl/private/certificate.pem
```
