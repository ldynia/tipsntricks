https://qiita.com/tkprof/items/2ec4ed58790efba3778d
http://ask.xmodulo.com/enable-elrepo-repository.html
https://qiita.com/tkprof/items/2ec4ed58790efba3778d

```bash
$ yum repolist
$ yum repolist enabled

$ yum-config-manager --disable

$ yum --disablerepo="*" --enablerepo="elrepo-kernel" list
$ yum --disablerepo="*" --enablerepo="elrepo-kernel" list available
$ yum --disablerepo="*" --enablerepo="elrepo-kernel" install kernel-ml-headers

$ yum --enablerepo=elrepo-kernel -y swap kernel-devel -- kernel-ml-devel
$ yum --enablerepo=elrepo-kernel -y swap kernel-headers -- kernel-ml-headers
$ yum -y remove kernel
```
