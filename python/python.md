# Python

### Install Packages

Bind packaged to a specific python version.

```bash
$ python2   -m pip install SomePackage  # default Python 2
$ python2.7 -m pip install SomePackage  # specifically Python 2.7
$ python3   -m pip install SomePackage  # default Python 3
$ python3.4 -m pip install SomePackage  # specifically Python 3.4
```

### Pickel

```python
# Save a dictionary into a pickle file.
import pickle

favorite_color = {"lion": "yellow", "kitty": "red"}

pickle.dump(favorite_color, open("save.p", "wb"))

# Load the dictionary back from the pickle file.
favorite_color = pickle.load(open("save.p", "rb" ))
```


```python
# get dictionary value by key
getattr(object, object.key_name)
getattr(metadata, 'latitude') -> getattr(f.metadata, field.name)
```

### AssertionError
```python
try:
    s = True
    assert s is not True, "Something went wrong"
except AssertionError as err:
    print(err.args[0])
```

### Benchmarking
```python
import time

start_time = time.time()

main()

print("--- %s seconds ---" % (time.time() - start_time))
```
