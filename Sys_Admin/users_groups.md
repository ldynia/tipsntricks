```bash
# CREATE NEW USER
$ useradd username

# SET PASSWORD FOR NEW USER
$ passwd username

# ADD www EXISTING USER TO cgeadm GROUP
$ usermod -a -G group_name user_name
$ usermod -A group_name user_name

# DISPLAY USER user_name ID
$ id -u user_name

# DISPLAY ALL GROUPS THAT USER www BELONGS TO
$ groups user_name
$ id user_name

# LIST GROUPS MEMBERS
http://www.cyberciti.biz/faq/linux-list-all-members-of-a-group/

# REMOVE USER FROM A GROUP
$ usermod -R group_name user_name
```
