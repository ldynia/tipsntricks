Links:
- [default-environment-variables](https://docs.github.com/en/actions/reference/environment-variables#default-environment-variables)
- [context](https://docs.github.com/en/actions/reference/context-and-expression-syntax-for-github-actions#github-context)

**debug_action.yaml**

```yaml
name: CI
on:
  push:
    branches: [ actions ]
  workflow_dispatch:
    branches: [ master, actions ]
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        include:
          - python: 3.6
            django: 2.2
            toxenv: py36-django22
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v1
        name: Set up Python ${{ matrix.python }} ${{ matrix.django }}
        with:
          python-version: ${{ matrix.python }}
      - name: Debug
        env:
          GITHUB_CONTEXT: ${{ toJson(github) }}
          COMMIT_MESSAGE: ${{ github.event.head_commit.message }}
        run: |
          python --version
          echo $GITHUB_CONTEXT
          ls -l $PWD
```
