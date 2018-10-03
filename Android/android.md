# Uninstall packages

https://developer.android.com/studio/command-line/adb

```bash
$ adb devices -l
$ adb shell
$ pm --help
$ pm list packages

# list disabled and enabled packages
$ pm list packages -d
$ pm list packages -e

$ pm list packages | grep google
$ pm list packages -d
$ pm uninstall -k --user 0 <name of package>
```
