#ifndef RESISTOR_COLOR_H
#define RESISTOR_COLOR_H

typedef enum {
BLACK, BROWN, RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET, GREY, WHITE
} resistor_band_t;

// Function definition for returning list of colors
resistor_band_t * colors(void);

// Function definition for color code lookup
int color_code(resistor_band_t color);

#endif
