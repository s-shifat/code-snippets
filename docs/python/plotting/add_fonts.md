---
id: add_fonts
aliases:
  - add_fonts
tags: []
---

# add_fonts

```python
# A pseudo scenario
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100, 0.2)
y = x**2

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y)

```

## Option1: Fonts installed and Setup in global scope
If a particular font is already installed in the development machine/system and for the plotting you want to use it in each plot (ie. global scope)

```python
plt.rcParams['font.family'] = 'Times New Roman'
```

## Option2: Fonts installed and Setup Plot Element specific
Tip: Most of the text contatining elements have `font` or similar keyword argument
```python
ax.set_title('x vs y', font='Times New Roman')  # Title
ax.set_xlabel('x m/s', font='Arial')  # Label
ax.set_xticks(
    np.arange(0, 100, 20),
    lables=np.arange(0, 100, 20),
    font='Source Code Pro'
)  # tick labels
```


## List The font names available to matplotlib

from [StackOverflow](https://stackoverflow.com/a/73938907/13497846)
```python
from matplotlib import font_manager
```

```python
sorted(font_manager.get_font_names())
```

## Load a font file without systemwide installation
```python
from matplotlib import font_manager
```

```python
font_path = "path/to/font.ttf"  
font_props = font_manager.FontProperties(fname=font_path)

ax.plot(x, y)

# Apply the custom font
ax.set_title("x vs y", fontproperties=font_props, fontsize=14)
ax.set_xlabel("X-axis Label", fontproperties=font_props)
ax.set_ylabel("Y-axis Label", fontproperties=font_props)
ax.legend(prop=font_props)
```


## Setup Font Size
setup font size of different components in global scope.
More at: [Customizing Matplotlib with Style sheets and rcParams](https://matplotlib.org/stable/users/explain/customizing.html)

```python
import matplotlib as mpl
```

```python
# Set LaTeX-style font
mpl.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern"],
    "axes.labelsize": 12,
    "axes.titlesize": 14,
    "legend.fontsize": 12,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
})


```
