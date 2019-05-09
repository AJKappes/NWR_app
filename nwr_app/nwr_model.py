# Python file for nutrient waste recycling model
from scipy.special import gamma
import numpy as np

def convert_temp(cel_temp):
    far_temp = cel_temp * 9/5 + 32
    return far_temp

def gamma_pdf(x, theta, k):
    g_pdf = theta ** (-k) / gamma(k) * x ** (k - 1) * np.exp(- x / theta)
    if x > 0 and theta > 0 and k > 0:
        return g_pdf
    else:
        raise ValueError('x, theta, and k must be greater than 0')
