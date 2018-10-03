# Git

### Tags
```
$ git tag -l
$ git tag -n
$ git tag 0.5 -m "test tag"
$ git push origin --tags <branch>
```

### Delete
```
# remove deleted files
$ git rm $(git ls-files --deleted)

# remove remote branch on origin
$ git push origin --delete branch_name
```

### Shortuct to deployment
```
$ alias git-all="git push origin develop && git checkout master && git merge develop && git push origin master && git checkout develop"
```


### Find

```
# find commit with deleted file
$ git rev-list -n 1 HEAD -- <path/to/deleted/file.py>

# example
$ git rev-list -n 1 HEAD -- app/tasks/file_upload.py
$ git show <commit>
```
