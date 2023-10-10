# Grep

```
# SHOWS ALL NEGATIVE NUMBERS EG. -7.45264
$ grep -E -o [-][0-9]+.[0-9]+ ex1.dat

# DISPLAY BLOCK SIZE 1GB
sudo du -csh --block-size=1G *

# REPLACE STRING WITH ALL FILES THAT CONTAIN A SEARCHED STRING
$ grep -lr "models.user_group_invites" core/ | xargs sed -i -e 's/models.user_group_invites/models.invitation/g'
$ sed -i -e 's/#   StrictHostKeyChecking ask/    StrictHostKeyChecking no/g' /etc/ssh/ssh_config

$ grep -lr "from app.api.serializers" app/api/views | xargs sed -i -e 's/from app.api.serializers/from app.models.serializers/g'
$ grep -lr "from core." tests/ | xargs sed -i -e 's/from core./from app./g'

$ grep -lr "from core.models.frontend_user.frontend_user" . | xargs sed -i -e 's/from core.models.frontend_user.frontend_user/from core.models.frontend_user/g'
$ grep -lr "core.models.user_extended" . | xargs sed -i -e 's/core.models.user_extended/core.models.user_metadata/g'

# GREP IDS FOR RSYNC PROCESS
$ ps -aux | grep rsync | awk '{print $2}'

# GREP IDS FOR RSYNC PROCESS AND KILL THEM ALL
$ kill -9 ps -aux | grep rsync | egrep -v grep | awk '{print $2}'

#RENAME EXTENSION OF FILES FORM scss to sass
$ rename .scss .sass *.scss
```


# Find

```
# Find files that are older than 14 days
$ find . -type f -mtime +14

# Delete files younger than 1 day
$ find . -type f -mtime +1 -delete

# Find all filese that belong to cgeadm group and change mode of group to write
$ find . -group cgeadm -exec chmod g+w {} \;

# Find broken symlink
$ find -L . -type l
$ find . -xtype l

# xtype is a test performed on a dereferenced link
$ find . -xtype l | grep "Too many levels of symbolic links rsync"

# Find paths to of broken links
$ find . -type l -! -exec test -e {} \; -print
$ find /home -type d -not -name "databases" -not -name "projects" -not -name "data[1,2]" -exec chmod -R g+rx {} \;
$ find /home -type d -not -name "databases" -not -name "projects" -not -name "data[3,4]" -exec chmod -R g+rx {} \;

root@ludd-dell:~# find . -type d -not -name "database" -not -name "projects" -not -name "data[1,2]" -exec chmod 755 {} \;
```
