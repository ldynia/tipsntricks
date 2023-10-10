```bash
# Restarting torq #1
alisyed@cgebase:~> pbsnodes -a
cgebase2:~ # /etc/init.d/pbs_mom status
cgebase2:~ # /etc/init.d/pbs_mom stop
cgebase2:~ # /etc/init.d/pbs_mom start
cgebase2:~ # /etc/init.d/pbs_mom status
cgebase2:~ # pbsnodes -a

# Restarting torq #2
sudo find /var/spool/torque/mom_logs/ -ctime +14 | xargs gzip
sudo find /var/spool/torque/server_priv/jobs/ -type f -mtime +14 -exec rm -f {} \;
sudo /etc/init.d/pbs_mom restart
sudo /etc/init.d/pbs_server restart
sudo /etc/init.d/maui restart

# kill stuber jobs
sudo showq -r
sudo ./scripts/bash/fix_torq.sh
```
