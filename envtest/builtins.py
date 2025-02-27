import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc

__all__ = ['rand_array', 'smooth_image','my_mat_solve','create_zeros']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
	return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()*b

def create_zeros(a):
	return np.zeros([a,a])