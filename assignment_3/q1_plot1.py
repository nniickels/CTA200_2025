# Assignment 3 code for CTA200 2025 by Nicole Jiang
# Imported .py file for q1 plot 1 of Jupyter notebook 

# Import statements
import numpy as np
import matplotlib.pyplot as plt

def iterate_q1_plot1(N=500, z=0, max_iter=30) -> np.array :
    """ Iteration code for question 1 plot 1. 

    Parameters:
    - N: int, number of x and y 
    - z: int, initial value of z (z0)
    - max_iter: int, maximum iterations 

    Returns: 
    - diverged: np.array, a boolean array that tells which points escape

    """

    # Create complex grid
    x = np.linspace(-2, 2, N) # 1D arrays
    y = np.linspace(-2, 2, N)
    x, y = np.meshgrid(x, y) # 2D NxN grid of x and y
    c = x + 1j * y  # 2D NxN array c of complex numbers

    # Iterate through z and mark escaped points
    diverged = np.zeros(c.shape, bool)  # Set up boolean array, same size as c, to mark points that diverge. Initialize as filled with False
    for i in range(max_iter):  
        with np.errstate(over="ignore", invalid="ignore"):  # Ignore error statement that shows up because values go to inf
            z = z**2 + c  
        diverged |= (np.abs(z) > 2)  # Switches points in diverged to True if np.abs(z) > 2 since 2 is escape radius

    return diverged 
 
