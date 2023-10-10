### Loging

```bash
$ dmesg
$ journalctl -fxe

$ systemctl status ypbind.service

$ tail -f /var/log/secure
$ tail -f /var/log/messages

#SELinux
$ tail -f /var/log/audit/audit.log

# hardware info
$ dmidecode > /tmp/dmidecode.txt
$ /opt/hp/hpdiags/hpdiags -t > /tmp/hpdiags.txt

$ hpsum --use_latest --silent --target <ip_address> --user <userid> --passwd <password>
$ hpsum --use_latest --silent --target localhost --user 0 --passwd rootboy05

tail -f /var/log/messages
tail -f /var/log/audit/audit.log
```

### Monitoring
```bash
# display meory info in GB
$ cat /proc/meminfo | awk '{print $1 "\t" $2/1024/1024 " GB"}'

# actual memory used memory
$ free -g | grep -e'-/+' | awk '{print "Memory: " $3 "/" $4 " GB [Used/Free]"}'
```


### HP
```bash
$ hpssacli ctrl all show status
$ hpssacli ctrl all diag file=/var/log/ADUReport.zip
$ hpssacli ctrl all show config
```


```bash
$ dmesg -H -T
$ dmidecode | grep -i proliant
$ dmidecode –type system | grep Manufacturer

```
