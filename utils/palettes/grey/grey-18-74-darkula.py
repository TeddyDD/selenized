from __future__ import division
import selenized_base

# Variant based on fg and bg lightness of darkula palette from Jetbrains
name = "Darkula"

palette = selenized_base.generate_palette(
    background=(18, 0, 0),
    # actual foreground shade is  74, -3, -9
    foreground=(74, 0, 0),
    monotone_spec={
        "bg_bright_1": [1/10,  1],
        "bg_bright_2": [1/4,   1],
        "fg_dim":      [2/4,   1],
        "fg_dim_2":    [3/4,   1],
        "fg_bright_2": [1+1/8, 1],
        "fg_bright":   [1+1/4, 1],
    },
)

