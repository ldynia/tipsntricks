## Replace string in all files

```bash
grep -rl 0.25.0 circuit/pipelines/ | xargs sed -i 's/0.25.0/0.26.0/g'
```

## Rename all files

```bash
find . -type f -name "producer.py" -execdir mv {} publisher.py \;
```

## Delete files with extensions

```bash
find . -name "*.pyc" -o -name "*.pyo" -exec rm -f {} \;
```

## Delete directory with extensions

```bash
find . -type d -name "__pycache__" -exec rm -rf {} \;
```

## Comment line that contains 'searched_string'

```bash
sed -e '/searched_string/ s/^#*/#/' -i /etc/apt/sources.list
```
