# Exercism C Track: Difference of Squares

## Lessons

### Declaring variables in recursive calls, thinking recursively (sum_of_squares)

This problem required repetitively iterating through each natural number from the input until 0, squareing it and then adding it to a total, finally returning that total. The n-1 nature of the problem suggested there was a recursive solution.

I first tried returning a combination of the number squared plus the recursive call, this wasn't working. In my mind there was a mental block: I kept thinking if I declared a variable, it would be redeclared and reset back to 0 each time. This was only the case because I was thinking of recursion like a loop. Once I thought through the control flow and decided to try it and see what happened, the results I got were very close to the answer. From there it was minor tweaking to get the math right. 

```c
unsigned int sum_of_squares(unsigned int number)
{  
    int total = 1;
    if (number > 1)
    {
        total = pow(number, 2) + sum_of_squares(number - 1);
    }
    return total;
}
```

While I've worked with and practiced recursion a little bit, this was the first time I was presented a problem that I could solve however I wanted, identified that it could be done recursively and successfully implemented the recursive solution. 
___

### Manipulating after the return in a recursive function (square_of_sum())

I made an attempt to solve the next function `square_of_sum()` recursively too. I was not able to get around having to apply to square the total after the recursive calls had all returned, ultimately coming to the conclusion: If you need to manipulate the value after the return, recursive will not work. So I implemented the following solution:

```c
unsigned int square_of_sum(unsigned int number)
{
    int total = 0;
    while (number > 0)
    {
        total += number;
        number--; 
    }
    return pow(total, 2);
}
```

This was a simple solution that worked. Perhaps there is a way using conditionals, but I was not able to find the logic. 

___

### Space and Time Complexity

Using a loop to solve was not the fastest solution to `square_of_sum`. That solution had a time complexity of O(n) since we had to calculate the sum n times, 1 for each iteration through the loop. Using a formula could have achieved O(1), excuting the sum only once no matter the size of the input. 

```c
unsigned int square_of_sum(unsigned int number)
{
    return ((number * (number + 1)) / 2) * ((number * (number + 1)) / 2);
}
```

This is also true for the recursive solution to `sum_of_squares`, the more efficient O(1) solution would have looked like:

```c
unsigned int sum_of_squares(unsigned int number)
{  
    return (number * (number + 1) * ((number * 2) + 1) / 6);
}
```

Source: [Difference between square of sum of numbers and sum of square of numbers
](https://learnersbucket.com/examples/algorithms/difference-between-square-of-sum-of-numbers-and-sum-of-square-of-numbers/) by [Prashant Yadav](https://learnersbucket.com/author/know_prashant/)
