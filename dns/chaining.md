# DNS Chaining

```bsh
CNAME           >                       CNAME >                             CNAME > A Record
ztar.live.com > eart-aks-prod-we. > eart-green-aks-prod-we.live.com > 10.86.40.5

$ dig +short ztar.live.com
eart-aks-prod-we.live.com.
eart-green-aks-prod-we.live.com.
10.86.40.5

$ nslookup ztar.live.com
Server:         10.73.223.216
Address:        10.73.223.216#53

ztar.live.com canonical name = eart-aks-prod-we.live.com.
eart-aks-prod-we.live.com     canonical name = eart-green-aks-prod-we.live.com.
Name:   eart-green-aks-prod-we.live.com
Address: 10.86.40.5
```
