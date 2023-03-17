#include "hamming.h"

int compute(const char *lhs, const char *rhs)
{
    int l = strlen(lhs);
    int r = strlen(rhs);
    int hamming = 0;

    // Test for valid string length
    if (l == r)
    {
        for (int i = 0; i < l; i++)
        {
            // If character is different, add 1 to hamming distance
            if (lhs[i] != rhs[i])
            {
                hamming++;
            }
        }
        return hamming;
    }
    else
    {
        // If not valid return -1
        return -1;
    }
    
}
