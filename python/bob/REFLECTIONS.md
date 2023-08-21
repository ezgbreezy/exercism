# Python: Bob

## Lessons

### String methods
The Bob exercise reinforced using object methods. When using a string method, the method name must be followed by '()':

```python
hey_bob = hey_bob.strip()
```

Omitting the '()' would only assign the method itself.

```python
>>> hey_bob = hey_bob.strip
>>> hey_bob
<built-in method strip of str object at 0x102869fb0>
```

As discussed in CS50P, you can call multiple methods sequentially as long as the methods each return a copy of the string (and not a boolean for example):

```python
# This works
hey_bob = hey_bob.strip().capitalize()

# This does not, since the .isupper() method evaluates to true or false, making hey_bob of type 'bool' before calling .strip(). 
hey_bob = hey_bob.isupper().strip()

# This works but hey_bob will now become a 'bool' instead of containing the original string
hey_bob = hey_bob.strip().isupper()
```
