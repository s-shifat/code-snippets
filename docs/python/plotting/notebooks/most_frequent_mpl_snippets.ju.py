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
x = np.arange(-10, 10, 0.01)
y = x**3 * np.sin(x) * np.cos(x)

# %% [markdown]
"""
## Quick Plot: set the basic plotting elements all at once


To see what other parameters can be set. visit [`matplotlib.axes.Axes.set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html)

I did it in *unpacking-dictionary way* for reusing purpose.
"""

# %%
fig_size = (8.5, 6)
fig, ax = plt.subplots(figsize=fig_size)

ax.plot(x, y)

ax_properties = {
    'title': 'My Title',

    'xlabel': 'X - label',
    'xlim': (-8.5, 8.5),
    'xscale': 'linear', # or log, function etc.

    'ylabel': 'Y - label',
    'ylim': (-200, 200),

}

ax.set(**ax_properties)

# or don't use `ax_proerties` at all
# ax.set(title="My Title", xlabel='X - label', ...)

plt.show()

