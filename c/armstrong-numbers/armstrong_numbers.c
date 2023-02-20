#include <math.h>
#include <stdio.h>

#include "armstrong_numbers.h"

bool is_armstrong_number(int candidate)
{
    int count = 0;
    int number = candidate; // Create copy
    
    // Count digits
    do
    {
        number /= 10;
        count++; 
    } while (number >= 1);

    // TEST: Print count
    printf("COUNT: %i\n", count);
    
    number = candidate; // Reset copy
    int digits[count];

    // Isolate digits
    for (int i = count - 1; i >= 0; i--)
    {
        digits[i] = number % 10;
        number /= 10;
    }
    
    // TEST: Print extracted digits
    printf("DIGITS: ");
    for (int i = 0; i < count; i++)
    {
        printf("%i", digits[i]);
    }
    printf("\n");

    // Reset number
    number = 0;

    // Calculate number
    for (int i = 0; i < count; i++)
    {
        number += pow(digits[i], count);
    }

    // TEST: Print number
    printf("NUMBER: %i\n", number);

    // Check if number is Armstrong Number
    if (number == candidate)
    {
        return true;
    }

    return false;
}

