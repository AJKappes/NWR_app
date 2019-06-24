# Python file for nutrient waste recycling model
from scipy.special import gamma
import numpy as np
import pandas as pd

# input function test

# def convert_temp(cel_temp):
#     far_temp = cel_temp * 9/5 + 32
#     return far_temp
#
# def gamma_pdf(x, theta, k):
#     g_pdf = theta ** (-k) / gamma(k) * x ** (k - 1) * np.exp(- x / theta)
#     if x > 0 and theta > 0 and k > 0:
#         return g_pdf
#     else:
#         raise ValueError('x, theta, and k must be greater than 0')

### nwr model ###

# phosphorus #

ex_data = pd.read_csv('/home/ajkappes/research/agri/Nutrient_Waste_Recycling/ADOPTfeedstocks.csv')

def phos_func(*args):
    '''
    Function takes feedstock and manure volume arguments and computes phosphorus nutrient outflow
    in kg/time step.

    3.79 constant converts gallon to liter
    '''
    coefs = [.035, .107, .34, .011, .13, .023]
    out_list = []

    for i in range(len(coefs)):
        out_list.append(3.79 * coefs[i] * args[i])

    phos_out = sum(out_list)

    return phos_out

#phos_func(10, 15, 20, 25, 30, 35)

