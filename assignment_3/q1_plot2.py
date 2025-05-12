# Assignment 3 code for CTA200 2025 by Nicole Jiang
# Imported .py file for q1 plot 2 of Jupyter notebook 

# Import statements
import numpy as np
import matplotlib.pyplot as plt

def iterate_q1_plot2(N=500, z=0, max_iter=30) -> np.array :
    """ Iteration code for question 1 plot 2. 

    Parameters:
    - N: int, number of x and y 
    - z: int, initial value of z (z0)
    - max_iter: int, maximum iterations 

    Returns: 
    - count: np.array, NxN int array of iteration count for when points escape

    """

    # Create complex grid
    x = np.linspace(-2, 2, N) # 1D arrays
    y = np.linspace(-2, 2, N)
    x, y = np.meshgrid(x, y) # 2D NxN grid of x and y
    c = x + 1j * y  # 2D NxN array c of complex numbers

    # Iterate through z and mark escaped points 
    diverged = np.zeros(c.shape, bool)  # Set up boolean array, same size as c, to mark points that diverge. Initialize as filled with False 

    # Iterate through z, this time recording escape iteration 
    count = np.zeros(c.shape, int)  # Hold iteration count 
    for i in range(1, max_iter + 1):  # Start at 1 for first update z0 -> z1
        with np.errstate(over="ignore", invalid="ignore"):  # Ignore error statement that shows up because values go to inf  
            z = z**2 + c  
        just_div = (np.abs(z) > 2) & (~diverged)  # Just diverged array will hold points that diverge for the first time
        count[just_div] = i  # Record iteration count when point escapes
        diverged[just_div] = True  # Record that point diverged 

    return count

