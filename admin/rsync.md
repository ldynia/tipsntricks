
## HOW TO RSYNC FILES AS A ROOT
http://webcache.googleusercontent.com/search?q=cache:http://www.ustrem.org/en/articles/rsync-over-ssh-as-root-en/
Rsync is widely used tool for incremental file transfer. It has several features that make it very attractive for easy to setup backup policy. You can run it over ssh to for additional security. Here's the issue here: most ssh servers are configured not to allow root login ("PermitRootLogin" set to "no"), but you need root permissions to read certain files. Here's the remedy for this.

First, on the remote server add the rsync user to the sudoers file, so that he can execute rsync with no password. Add this to /etc/sudoers:
rsyncuser ALL= NOPASSWD:/usr/bin/rsync

Then use --rsync-path option to make rsync run with sudo:
[user@localserver]$ rsync -a -e "ssh" --rsync-path="sudo rsync" rsyncuser@remoteserver:/data/to/sync /archi
