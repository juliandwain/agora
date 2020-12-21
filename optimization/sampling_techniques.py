# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Design Space Exploration
# %% [markdown]
# ## Sampling Techniques
#
# A **sample** is a collection of design vectors $\vec{x_{A}}$ and output values $\vec{y_{A}}$ with $A=1,...,N$ being the design index and $N$ being the sample size.
# These designs are choosen using a **sampling method**, i.e. the Design of Experiment (DoE).
# Sampling is used to probe the design space.

# %%
import numpy as np

# %% [markdown]
# ### Full Factorial Design

# %%


def full_factorial():
    levels = 4
    parameters = 2
    n = levels ** parameters
    full_fac = np.zeros((n, parameters), dtype=float)
    for j in range(parameters):
        counter = 1
        for i in range(n):
            if counter > levels:
                counter = 1
            full_fac[i, j] = counter
            rem_dim = parameters - j
            if i % (levels ** rem_dim) == 0:
                counter += 1
    return full_fac


# %%
ff = full_factorial()


# %%
ff


# %%
get_ipython().run_line_magic('timeit', 'full_factorial()')


# %%
def full_factorial1():
    pass
