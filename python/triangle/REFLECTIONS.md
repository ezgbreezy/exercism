# Exercism Python Track: Triangle

## Lessons

### Using the DRY (Don't Repeat Yourself) principle

Each function in this exercise first required validating whether or not it was a triangle. This process is the same each time. It was apparent that a new function was necessary to implement the DRY principle. 


### Linking multiple comparison operators

For the function `scalene()`, I initally linked together multiple comparison operators like so:

```python
    # Check if scalene triangle
    if sides[0] != sides[1] != sides[2]:
        return True
    else:
        return False
```

This had a bug due to the fact that linking in this way doesn't ensure that `sides[0] != sides[2]`. Here `sides[0]` is compared to `sides[1]`, then `sides[1]` is compared to `sides[2]`, but the problem required all to be compared to one another. The solution was to simply add this missing comparison to the end of the chain:

```python
    # Check if scalene triangle
    if sides[0] != sides[1] != sides[2] != sides[0]:
        return True
    else:
        return False
```
