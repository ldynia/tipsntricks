```bash

$ docker run --rm -it -v $PWD:/app python:3.7 bash

$ poetry config repositories.testpypi https://test.pypi.org/legacy/
$ poetry config pypi-token.testpypi <access-token>

$ poetry build
$ poetry publish -r testpypi -u ldynia
```
