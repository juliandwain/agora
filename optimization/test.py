import numpy as np
import scipy.linalg as la
from typing import Tuple


def monte_carlo_sampling(num_samples: int, parameters: int) -> np.ndarray:
    """Monte Carlo design evaluation.

    Parameters
    ----------
    num_samples : int
        The number of random sample points to be used.
    parameters : int
        The number of parameters.

    Returns
    -------
    np.ndarray
        The monte carlo design matrix of size (n, parameters).
    """
    rng = np.random.default_rng()  # define a random number generator
    samples = rng.uniform(low=0.0, high=1.0, size=(num_samples, parameters))
    return samples


def distance(samples: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Calculate the distance between points.

    Parameters
    ----------
    samples : np.ndarray of shape (n, d)
        The sample for which the distances should be calculated. 
        The shape results from the number of sample points n and the number of parameters,
        i.e. the number of dimensions, considered.

    Returns
    -------
    np.ndarray
        The distance matrix of shape (n, n) where n is the number of sample points.
        The first row corresponds to the distance of the first point to all other points and so forth.
    np.ndarray
        The upper triangular entries of the distance matrix.

    Notes
    -----
    The structure of the matrix can be described as

        sqrt((x1 - x1)^2) sqrt((x1 - x2)^2) ... sqrt((x1 - xn)^2)
    D = ...               ...               ... ...
        sqrt((xn - x1)^2) sqrt((xn - x2)^2) ... sqrt((xn - xn)^2)

    """
    n = samples.shape[0]  # get the number of sample points
    matrix = la.norm(np.repeat(samples, n, axis=0) - np.vstack([samples] * n), axis=-1).reshape((n, n))
    matrix = 0.5 * (matrix + matrix.transpose())  # ensure that the matrix is symmetric
    triu = matrix[np.triu_indices(n, k=1)]  # extract only the upper diagonal entries
    return matrix, triu


num_samples = 5_000
d = 20
mc_d = monte_carlo_sampling(num_samples, d)
_, distances = distance(mc_d)
# np.repeat(samples, n, axis=0)
# np.vstack([samples]*n)
