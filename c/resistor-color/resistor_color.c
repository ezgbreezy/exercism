#include "resistor_color.h"

#include <stdio.h>
#include <stdlib.h>

// Return color code
int color_code(resistor_band_t color)
{
    return color;
}

// Return list of colors
resistor_band_t * colors(void)
{
    static resistor_band_t colors[] = {BLACK, BROWN, RED, ORANGE, YELLOW, 
                                      GREEN, BLUE, VIOLET, GREY, WHITE};

    return colors;
}
