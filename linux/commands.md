# Commands

## diff

https://linuxhint.com/compare-two-files-linux/


## Conver file to single line

https://serverfault.com/questions/466683/can-an-ssl-certificate-be-on-a-single-line-in-a-file-no-line-breaks

```
awk 'NF {sub(/\r/, ""); printf "%s\\n",$0;}'  ca.pem
```
