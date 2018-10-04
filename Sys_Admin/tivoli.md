# list backuped dirs
dsmc query backup /var -subdir=yes

# retrive backup dir
dsmc restore /srv/www/compare/production/ /tmp/xxx/ -subdir=yes -latest
dsmc restore /etc/postfix/main.cf /tmp/xxx/ -latest

#############

You need to install the IBM Tivoli Storage Manager client on your centos machines.

ftp://index.storsys.ibm.com/tivoli-storage-management/maintenance/client/v7r1/Linux/
http://www.ibm.com/support/knowledgecenter/SSGSG7_7.1.6/client/t_inst_linuxx86client.html

You also need to set them up, so that they back up exactly what they need, but stay clear of the problematic system files like mmapped status files, devices etc.

I suggest looking in /opt/tivoli/tsm/client/ba/bin/dsm.sys and /opt/tivoli/tsm/client/ba/bin/dsm.opt, but modify for centos.

Tell me when the services are installed, and configured, and I will connect them up to the backup.

#############

Finally, when you have centos on compare01, it is essential that you write a script that monitors the raid state of /home disk. It is not responsible

to have the raid state unmonitored. You need to make a script that at least

  Write a single status line, e.g. 'UNKNOWN','OK', 'WARNING' or 'CRITICAL' depending on result (perhaps more informative would be nice, but just one line)

  exit with status

     OK=0, WARNING=1,CRITICAL=2,UNKNOWN=3

 Is rigorous with testing all elements of the process to not report OK, if there was a problem testing.

https://nagios-plugins.org/doc/guidelines.html (but my description above cover the minimum)

#############

Dell machines have a tool for monitoring system health, such as fanspeed, voltage, temperature, disk health, amperage, memory failures, etc.
With centos, it should be easier to make a script that monitors this for your HP systems. Same guidelines as above.
This will allow you to do planned replacements of failing components instead of waiting full system crashes - which waits for no one.

#############
