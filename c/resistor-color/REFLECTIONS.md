# Exercism C Track: Resistor Color

## Lessons

### Returning arrays from functions

Returning an array from a function is not possible in C. You can however return a pointer to the first element of the array. Arrays are **passed by reference**, so the memory address with the original value is passed instead of a copy of the value.

I declared the array locally within the function so it was stored on the C stack. This continualy resulted in the following error: 

```error: address of stack memory associated with local variable 'colors' returned [-Werror,-Wreturn-stack-address]```

[This article](https://codeforwin.org/c-programming/pass-return-array-function-c) suggested the only way to return the array values when declaring it locally would be to allocate it dynamically on the heap instead using `malloc` or to declare it as a `static` variable. Declaring it dynamically resulted in the following error:

```resistor_color.c:13:27: error: array initializer must be an initializer list```

```const resistor_band_t colors[] = malloc(sizeof(int) * 10)```

I opted to try a static variable instead.

### Static variables

`static` variables store the values in the program data portion of memory. This allows the values to carry over across function calls.

[Static variables](https://codeforwin.org/c-programming/static-variables-c)