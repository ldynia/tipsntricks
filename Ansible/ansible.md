# Ansible


### Run Playbook
```bash
$ ansible-playbook -K -s -u vagrant playbook.yml  
$ ansible-playbook --ask-sudo-pass --user=vagrant playbook.yml
```

### Ad-Hoc
```bash
ansible -vvvv -u vagrant -m ping all
ansible -vvvv -u vagrant -m shell -a 'hostname' all
ansible -vvvv -u vagrant -m shell -a 'df -h' all
ansible -vvvv -u vagrant -m shell -a 'whoami' all
ansible -vvvv -u vagrant -m shell -a 'yes | docker container prune' all
```
