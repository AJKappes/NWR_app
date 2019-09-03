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

def phos_func(*args, loc, soil_test, acres):
    '''
    Function takes feedstock and manure volume arguments and computes phosphorus nutrient outflow
    in kg/time step.

    3.79 constant converts gallon to liter
    0.9112 nutrient portion remaining post liquid-solid seperation after AD output to lagoon
    2.205 constant converts kilogram to pound
    '''
    coefs = [.035, .107, .34, .011, .13, .023]
    # [blood, fish_by, paper_pulp, ob, gt, manure]
    tip_fees = [0.03609, 0.05, 0.0415, 0.05, 0.05, 0]
    # [blood, pulp] tipping fees
    out_list = []
    rev_list = []

    for i in range(len(coefs)):
        out_list.append(3.79 * coefs[i] * args[i])
        rev_list.append(tip_fees[i] * args[i])

    phos_out = round(2.205 * 0.9112 * sum(out_list), 3)
    lb_acre = round(phos_out / acres, 3)
    input_rev = round(sum(rev_list), 3)

    if loc == 'West' or loc == 'west':
        if soil_test < 20:
            p_index = 'Low'
            rec_p_app = '0-300'
            if lb_acre > 300:
                app_decision = 'Do not apply'
            else:
                app_decision = 'Apply'

        if 20 <= soil_test < 40:
            p_index = 'Medium'
            rec_p_app = '0-200'
            if lb_acre > 200:
                app_decision = 'Do not apply'
            else:
                app_decision = 'Apply'

        if 40 <= soil_test <= 100:
            p_index = 'High'
            rec_p_app = '0-30'
            if lb_acre > 30:
                app_decision = 'Do not apply'
            else:
                app_decision = 'Apply'

        if soil_test > 100:
            p_index = 'Excessive'
            rec_p_app = '0'
            app_decision = 'Do not apply'

    if loc == 'East' or loc == 'east':
        if soil_test < 10:
            p_index = 'Low'
            rec_p_app = '0-300'
            if lb_acre > 300:
                app_decision = 'Do not apply'
            else:
                app_decision = 'Apply'

        if 10 <= soil_test < 25:
            p_index = 'Medium'
            rec_p_app = '0-200'
            if lb_acre > 200:
                app_decision = 'Do not apply'
            else:
                app_decision = 'Apply'

        if 25 <= soil_test <= 50:
            p_index = 'High'
            rec_p_app = '0-30'
            if lb_acre > 30:
                app_decision = 'Do not apply'
            else:
                app_decision = 'Apply'

        if soil_test > 50:
            p_index = 'Excessive'
            rec_p_app = '0'
            app_decision = 'Do not apply'

    return [phos_out, lb_acre, p_index, rec_p_app, app_decision, input_rev]


#phos_func(10, 15, 20, 25, 30, 35, loc='west', soil_test=51, acres=4)

