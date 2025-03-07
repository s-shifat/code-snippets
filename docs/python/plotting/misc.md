---
id: misc
aliases: []
tags: []
---

## Change Backend / Use figure toolbars
Use matplotlib toolbars in jupyter notebook environment.

```python
matplotlib.use('nbagg')  # For Tool bars in plot
```
Other backends:

```python
matplotlib.use('TkAgg')  # For Tool bars in plot
# or
matplotlib.use('Qt5Agg')  # For Tool bars in plot
```

While using `ipython` and a terminal that supports image rendering like `kitty` magic commands also work:
```ipython
%matplotlib tk
#or
%matplotlib qt
```




I am currently using `kitty` terminal. To use kitty as backend for python's matplotlib library. use the following:

1. Install it:

    ```bash
    pip install --user matplotlib-backend-kitty

    ```

2. Use it (say in `ipython` or vanila `python`):
    ```python
    import matplotlib
    matplotlib.use('module://matplotlib-backend-kitty')
    import matplotlib.pyplot as plt
    ```


More on [this](https://github.com/jktr/matplotlib-backend-kitty) link.





## Use Latex in global scope
It will display numbers in latex format and also the formula.

```python
plt.rcParams['text.usetex'] = True
```

## Format Dates in axis
Let's say I only want to show hours and minutes in the time axis (x-axis)


```python
from matplotlib.dates import DateFormatter
```

```python
time_format = DateFormatter("%H:%M")

ax.xaxis.set_major_formatter(time_format)
```

> python date string formats are found [here](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
