# %% [markdown]
"""
## Standard Imports
"""

# %%
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8")


# %%
x = np.arange(-10, 10, 0.01)
y = x**3 * np.sin(x) * np.cos(x)

# %% [markdown]
"""
## Set the basic plotting elements all at once


To see what other parameters can be set. visit [`matplotlib.axes.Axes.set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html)
"""

# %%
fig_size = (8.5, 6)
fig, ax = plt.subplots(figsize=fig_size)

ax.plot(x, y)

ax.set(**{
    'title': 'My Title',

    'xlabel': 'X - label',
    'xlim': (-8.5, 8.5),
    'xscale': 'linear', # or log, function etc.

    'ylabel': 'Y - label',
    'ylim': (-200, 200),
})

plt.show()

