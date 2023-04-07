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

| Source with Arguments →<br/>Target and Return Value ↓ | `rgb2...(red, green, blue)` | `hex2...("#RRGGBB" or "#RGB")` | `hsl2...(hue, saturation, lightness)` | `hsv2...(hue, saturation, value)`<br/>`hsb2...(hue, saturation, brightness)` | `hsv2...(cyan, magenta, yellow, black)` |
| --- | --- | --- | --- | --- | --- |
| `rgb` → `(red, green, blue)` |  | ✓ | ✓ | ✓ | ✓ |
| `hex` → `"#RRGGBB"` | ✓ |  | ✓ | ✓ | ✓ |
| `hsl` → `(hue, saturation, lightness)` | ✓ | ✓ |  | ✓ | ✓ |
| `hsv` or `hsb` → `(hue, saturation, brightness)` | ✓ | ✓ | ✓ |  | ✓ |
| `cmyk` → `(cyan, magenta, yellow, black)` | ✓ | ✓ | ✓ | ✓ |  |

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

