---
id: ds_starter
aliases: []
tags: []
---

# Data Science Starter Snippets

## Preamble-1 / Quick Start 1
A quick start or a preamble to data science projects.
I have written [my own matplotlib stylesheet](https://gist.github.com/s-shifat/5f35e9d53d41a3195a8a86885f989fa1), roughtly following the guidelines for scientific publications.
To edit it, simply download the stylesheet in the same directory as the notebook/script file you're working (otherwise use absolute path) on and
use that instead $\rightarrow$ `plt.style.use("./s_shifat_mpl_stylesheet.mplstyle")`.

**Note:** *Nice thing about `plt.style.use()` is, it can be [ mixed ](https://matplotlib.org/stable/users/explain/customizing.html#composing-styles) with other built-in (outputs of [ `plt.style.available` ](https://matplotlib.org/stable/users/explain/customizing.html#using-style-sheets)) or custom styles chronologically as well using a list.*

```python
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# some nice aesthetics
plt.style.use(
    "https://gist.githubusercontent.com/s-shifat/5f35e9d53d41a3195a8a86885f989fa1/"
    "raw/e0005b8b0965c819510d719896baf8aa2faec914/s_shifat_mpl_stylesheet.mplstyle"
)

# mpl.use("nbagg")  # interactive backend

# %%
DATA_PATH = "./data.csv"
df = pd.read_csv(DATA_PATH)
df

# %%
df.info()

```


## Preamble-2 / Quick Start 2
The above example keeps the initial plot aesthetics away from the code to reduce clutter a bit.
However, to control plot aesthetics right from your code $\rightarrow$

```python
# %%
import numpy as np
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# some plot aesthetics
mpl.rcParams.update({
    "text.usetex": False,
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Computer Modern"],
    "axes.titlesize": 14,
    "axes.labelsize": 12,
    "legend.fontsize": 12,
    "xtick.labelsize": 12,
    "xtick.direction": "out",
    "ytick.labelsize": 12,
    "ytick.direction": "out",
    "figure.figsize": (8, 6),
})

# mpl.use("nbagg")  # interactive backend


# %%
DATA_PATH = "./data.csv"
df = pd.read_csv(DATA_PATH)
df

# %%
df.info()

```
