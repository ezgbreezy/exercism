#include "isogram.h"

bool is_isogram(const char phrase[])
{
    // Check if NULL
    if (phrase == NULL)
    {
        return false;
    }

    // Create working copy of phrase
    char *copy = malloc(strlen(phrase) + 1);
    strcpy(copy, phrase);
    
    // Create counter for each letter, set counts to zero
    int counter[26];
    for (int i = 0; i < 26; i++)
    {
        counter[i] = 0;
    }

    for (int i = 0; phrase[i] != '\0'; i++)
    {
        // Convert to lowercase
        copy[i] = tolower(phrase[i]);

        // Increment counter for alphabetical characters
        if (copy[i] != ' ' && copy[i] != '-')
        {
            counter[copy[i] - 'a']++;

            // Check if character appears more than once
            if (counter[copy[i] - 'a'] > 1)
            {
                free(copy);
                return false;
            }
        }
        
    }

    free(copy);

    return true;
}
