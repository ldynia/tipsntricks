# Windows Subsystem for Linux

https://docs.microsoft.com/en-us/windows/wsl/install
https://docs.docker.com/desktop/windows/wsl/

```bash
wsl --list --online
wsl --list --verbose
wsl --set-default-version 2
wsl --install -d Ubuntu
wsl --setdefault Ubuntu
```

# DNS

https://github.com/microsoft/WSL/issues/5420

```
# /etc/wsl.conf
sudo bash -c 'echo "[network]" > /etc/wsl.conf'
sudo bash -c 'echo "generateResolvConf = false" >> /etc/wsl.conf'

# /etc/resolv.conf
sudo rm /etc/resolv.conf
sudo bash -c 'echo "nameserver 10.73.223.218" > /etc/resolv.conf'
sudo bash -c 'echo "nameserver 10.73.223.219" >> /etc/resolv.conf'
```

# CERTs

```
curl -L onet.pl
cp * /usr/local/share/ca-certificates
sudo update-ca-certificates
curl -L onet.pl
```
