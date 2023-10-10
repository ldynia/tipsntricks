# Domain


## Generate CSR cert and KEY

[link](https://www.liquidweb.com/kb/generating-certificate-signing-request-csr/)

```bash
$openssl req -new -newkey rsa:2048 -nodes -keyout *.domain.key -out *.domain.csr
```
