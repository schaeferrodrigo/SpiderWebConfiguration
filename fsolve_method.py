# -*- coding: utf-8 -*-
#==============================================================================
from scipy.optimize import fsolve
from basic_functions import*
#from parameters import *


def solution_method(mass_dist, num_lines,theta,num_circles):

    def func_to_be_solved(radii):
        radii = np.insert(radii, 0 , 0 )
        return vector_f(radii, mass_dist , num_lines , theta,num_circles)

    root = fsolve(func_to_be_solved, range(1, num_circles+1), xtol = 1e-10)
    return root
