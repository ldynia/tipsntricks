# Ansible

### Ad-Hoc
```bash
ansible -vvvv -u vagrant -m ping all
ansible -vvvv -u vagrant -m shell -a 'hostname' all
ansible -vvvv -u vagrant -m shell -a 'df -h' all
ansible -vvvv -u vagrant -m shell -a 'whoami' all
ansible -vvvv -u vagrant -m shell -a 'yes | docker container prune' all
```

### Playbook
```bash
$ ansible-playbook -K -s -u vagrant playbook.yml  
$ ansible-playbook --ask-sudo-pass --user=vagrant playbook.yml
```



### Variables

Check service status
```yaml
- name: "Obtain state of kublet service"
  command: systemctl status kubelet.service
  register: kubelet_status
  failed_when: kubelet_status.rc > 3

- debug:
    msg: "{{ kubelet_status.stdout }}"
  when: "'running' not in kubelet_status.stdout"
```
