# Exercism Python Track

## Lessons

### Using object methods and shifting away from procedural programming
Looking up object methods opens new possiblilities for ways of doing things without having to write procedures. My solution to this exercise still appears very procedural compared to other solutions I looked at after completing the exercise. Object methods can make development faster and make code simpler and more readable than following paths of logical procedure. I aim to make a program simple and easy to read. While it is hard to tell looking at a program you very recently wrote, my procedural way of writing code seems harder to read and follow. My goal is to find a balance between procedural and object-oriented programming styles that is as readable as possible. 

Look at this segment of my solution:

```python
if letter in vowels:
    # 'qu' edge case handling
    if letter == 'u' and cluster.endswith('q'):
        cluster += letter
        text[index] = word.removeprefix(cluster) + cluster + suffix
        break
    # 'yt' edge case handling
    elif letter == 't' and cluster.endswith('y'):
        cluster = ""
        text[index] = word + suffix
        break
    else:
        text[index] = word.removeprefix(cluster) + cluster + suffix
        break
else:
    # 'xr' edge case handling
    if (letter == 'r' and cluster.endswith('x')):
        cluster = ""
        text[index] = word + suffix
        break
    # 'yt' edge case handling
    elif letter == 't' and cluster.endswith('y'):
        cluster = ""
        text[index] = word + suffix
        break
    cluster += letter
```

The above seqment repeats:

```python
text[index] = word.removeprefix(cluster) + cluster + suffix
```
and
```python
text[index] = word + suffix
```

The purpose of this is to rotate certain letters from the front of the word to the rear.

However in some of the other solutions I reviewed, this logic was replaced with a much simpler function:

```python
def rotate(word):
    return word[1:] + word[0]
```

Using the above function, they rotated the letters of the word until a vowel was found except in the defined edge cases, and thus the solution was simplified. 