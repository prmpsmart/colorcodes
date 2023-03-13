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

| name | min | max |
| --- | --- | --- |
| red | 0 | 255 |
| green | 0 | 255 |
| blue | 0 | 255 |
| R | 0 | F |
| G | 0 | F |
| B | 0 | F |
| hue | 0 | 360 |
| saturation | 0 | 1 |
| lightness | 0 | 1 |
| value or brightness | 0 | 1 |
| cyan | 0 | 1 |
| magenta | 0 | 1 |
| yellow | 0 | 1 |
| black | 0 | 1 |

