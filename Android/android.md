# Uninstall packages

### ADB
Link to [
Android Debug Bridge](https://developer.android.com/studio/command-line/adb)

```bash
$ adb devices -l
$ adb shell
```

### Package Manager
```bash
# package manager
$ pm --help
$ pm list packages

# list disabled and enabled packages
$ pm list packages -d
$ pm list packages -e

# find all google packages
$ pm list packages | grep google

# uninstall package
$ pm uninstall -k --user 0 <name of package>
```
