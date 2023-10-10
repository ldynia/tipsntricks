# Debug

### ping

```bash
$ ping -c1 test.app.example.com
PING circuit-green-aks-test-we.prod.com (10.86.39.50) 56(84) bytes of data.
```

### nslookup

```bash
$ nslookup test.app.example.com

Server:         10.73.223.218
Address:        10.73.223.218#53

test.app.example.com     canonical name = circuit-green-aks-test-we.prod.com.
Name:   circuit-green-aks-test-we.prod.com
Address: 10.86.39.50
```

### dig

```bash
$ dig test.app.example.com

; <<>> DiG 9.16.1-Ubuntu <<>> test.app.example.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 8717
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;test.app.example.com.           IN      A

;; ANSWER SECTION:
test.app.example.com.    3600    IN      CNAME   circuit-green-aks-test-we.prod.com.
circuit-green-aks-test-we.prod.com. 120 IN A  10.86.39.50

;; Query time: 10 msec
;; SERVER: 10.73.223.218#53(10.73.223.218)
;; WHEN: Wed Feb 23 13:41:35 CET 2022
;; MSG SIZE  rcvd: 114
```

### nc

```bash
$ nc -zvw 1 some.database.windows.net 1433
```

### telnet

```bash
$ telnet some.database.windows.net 1433
```
