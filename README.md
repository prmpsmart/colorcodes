# convert_color_codes

The convert_color_codes module deals with the conversion of color codes. Conversion from these codes HSV/HSB, RGB, CMYK, HSL from one to another.

## Installation

You can install _convert_color_codes_ from PyPI:

```
pip install convert_color_codes
```

It is supported on Python 2, 3 ...

## How to use

``` python
from convert_color_codes import *
```

There are several functions like `rgb2hex(red, green, blue)`, see the table:

|  | `rgb2...(red:int, green:int, blue:int)` | `hex2...("#RRGGBB" | "#RGB")` | `hsl2...(hue:int, saturation:int, lightness:int)` | `hsv2...(hue:int, saturation:int, value:int)`<br/>`hsb2...(hue:int, saturation:int, brightness:int)` | `hsv2...(cyan:int, magenta:int, yellow:int, black:int)` |
| `rgb` → `(red:int, green:int, blue:int)` |  | ✓ | ✓ | ✓ | ✓ |
| `hex` → `"#RRGGBB"` | ✓ |  | ✓ | ✓ | ✓ |
| `hsl` → `(hue:int, saturation:int, lightness:int)` | ✓ | ✓ |  | ✓ | ✓ |
| `hsv` or `hsb` → `(hue:int, saturation:int, brightness:int)` | ✓ | ✓ | ✓ |  | ✓ |
| `cmyk` → `(cyan:int, magenta:int, yellow:int, black:int)` | ✓ | ✓ | ✓ | ✓ |  |

The values have different ranges:

| name | min | max | type |
| --- | --- | --- | --- |
| red | 0 | 255 | int |
| green | 0 | 255 | int |
| blue | 0 | 255 | int |
| R | 0 | F | str |
| G | 0 | F | str |
| B | 0 | F | str |
| hue | 0 | 360 | int or float |
| saturation | 0 | 1 | float |
| lightness | 0 | 1 | float |
| value or brightness | 0 | 1 | float |
| cyan | 0 | 1 | float |
| magenta | 0 | 1 | float |
| yellow | 0 | 1 | float |
| black | 0 | 1 | float |

