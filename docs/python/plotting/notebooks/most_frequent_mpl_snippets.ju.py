# %% [markdown]
"""
## Preamble
"""

# %%
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Some nice styling
plt.style.use("seaborn-v0_8")
mpl.rcParams.update({
    "font.family": "Times New Roman",
    "axes.titlesize": 18,
    "axes.labelsize": 14,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
})

# %%
x = np.arange(-4*np.pi, 4*np.pi + 0.01, 0.01)
y = x**3 * np.sin(x) * np.cos(x)

x_left, x_right, interval = -2*np.pi, 2*np.pi, np.deg2rad(90)
custom_xticks = np.arange(x_left, x_right + interval, interval)
custom_xticks_labels = np.int16(np.rint(np.degrees(custom_xticks)))

# %% [markdown]
"""
## Quick Plot: set the basic plotting elements all at once


To see what other parameters can be set. visit [`matplotlib.axes.Axes.set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html)
"""

# %%
fig_size = (8.5, 6)
fig, ax = plt.subplots(figsize=fig_size)

ax.plot(x, y)

ax.set(
    title= 'My Title',

    xlabel = '$\\leftarrow X \\rightarrow$',
    xlim = (x_left, x_right),
    xscale = 'linear', # or 'log', <function> etc.

    ylabel = '$\\leftarrow Y \\rightarrow$',
    ylim = (-100, 50),
)


fig.set_layout_engine('constrained')
# fig.savefig('myplot.png', dpi=600)

plt.show()

# %% [markdown]
"""
or use a dictionary  with the valid key word arguments $\rightarrow$
```python
ax_properties = {
    "title": "My title",
    "xlabel": "x",
    "ylabel": "y",
    # etc...
}
ax.set(**ax_properties)

```
"""

# %% [markdown]
"""
## Add rotation to tick labels

Stolen from [StackOverflow](https://stackoverflow.com/q/10998621)
"""

# %% [markdown]
"""
### Rotating xtick labels wihtout custom ticks and labels
"""

# %%
plt.plot(x, y)

# simplest
plt.xticks(rotation=45)

# or 
ax.tick_params(axis='x', labelrotation=45)

# %% [markdown]
"""
### Rotating xtick labels with custom ticks and labels
"""

# %%
plt.plot(x, y)
ax  = plt.gca()

ax.set_xticks(custom_xticks, custom_xticks_labels, rotation=90)

plt.show()

