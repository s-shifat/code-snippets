---
id: misc
aliases: []
tags: []
---

## Use figure toolbars
Use matplotlib toolbars in jupyter notebook environment.

```python
matplotlib.use('nbagg')  # For Tool bars in plot
```

## Use Latex in global scope
It will display numbers in latex format and also the formula.

```python
plt.rcParams['text.usetex'] = True
```

## Format Dates in axis
Let's say I only want to show hours and minutes in the time axis (x-axis)

```python
from matplotlib.dates import DateFormatter

time_format = DateFormatter("%H:%M")

ax.xaxis.set_major_formatter(time_format)
```

> python date string formats are found [here](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
