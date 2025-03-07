---
id: misc
aliases: []
tags: []
---

# Change Backend / Use figure toolbars
Use matplotlib figure toolbars in jupyter notebook environment.

```python
matplotlib.use('nbagg')  # For Figure Tool bars embedded in jupyter output cell
```
Other backends:

```python
matplotlib.use('TkAgg')
# or
matplotlib.use('Qt5Agg')
```
There are also few other cool backends built-in, which can be divided into 2 categories: Interactive and Non-interactive.

To see what's available:

```python
from matplotlib.backends import backend_registry, BackendFilter
print("Interactives:", backend_registry.list_builtin(BackendFilter.INTERACTIVE))
print("Non-interactives:", backend_registry.list_builtin(BackendFilter.NON_INTERACTIVE))
```

### Inline / commandline plotting

#### Inline + Interactive
While using `ipython` and a terminal that supports image rendering like [`kitty`](https://github.com/kovidgoyal/kitty?tab=readme-ov-file) magic commands also work:

Technically this should work in jupyter notebooks too.
```ipython
%matplotlib tk
#or
%matplotlib qt
```
### Kitty and matplotlib

#### Inline + Non-interactive
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
. 
More on [this](https://github.com/jktr/matplotlib-backend-kitty) link.





# Use Latex in global scope
It will display numbers in latex format and also the formula.

```python
plt.rcParams['text.usetex'] = True
```

# Format Dates in axis
Let's say I only want to show hours and minutes in the time axis (x-axis)


```python
from matplotlib.dates import DateFormatter
```

```python
time_format = DateFormatter("%H:%M")

ax.xaxis.set_major_formatter(time_format)
```

> python date string formats (I like to call it python date format table) are found [here](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
