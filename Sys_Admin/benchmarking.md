http://askubuntu.com/questions/87035/how-to-check-hard-disk-performance

```bash
# write seped
$ dd if=/dev/zero of=/dd_test_zero_test_1 bs=1G count=5
$ dd if=/dev/zero of=~/dd_test_zero_test_1 bs=1M count=1024

#cleaer cache
$ sudo sh -c "sync && echo 3 > /proc/sys/vm/drop_caches"

# read seped
$ dd if=dd_test_zero_test_1 of=/dev/null bs=1G
$ dd if=dd_test_zero_test_1 of=/dev/null bs=1M
```

```bash
hwinfo --short
lspci | grep "RAID"
```
