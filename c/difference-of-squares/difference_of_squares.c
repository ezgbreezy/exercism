#include "difference_of_squares.h"

unsigned int sum_of_squares(unsigned int number)
{  
    int total = 1;
    if (number > 1)
    {
        total = pow(number, 2) + sum_of_squares(number - 1);
    }
    return total;
}

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

unsigned int difference_of_squares(unsigned int number)
{
    return (square_of_sum(number) - sum_of_squares(number));
}
