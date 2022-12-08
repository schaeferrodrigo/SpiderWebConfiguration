# -*- coding: utf-8 -*-
#==============================================================================
from scipy.optimize import fsolve
from basic_functions import*
import numpy as np
#from parameters import *



def solution_method(mass_dist, num_lines,theta,num_circles):

    def func_to_be_solved(radii):
        radii = np.insert(radii, 0 , 0 )
        return vector_f(radii, mass_dist , num_lines , theta,num_circles)

    #init_guess = np.array(range(1, num_circles+1)) + num_circles*[0.5] 
    init_guess =  range(1, num_circles+1)   
    root = fsolve(func_to_be_solved, init_guess , xtol = 1e-12)
    perturbation = 0.1
    while np.linalg.norm(func_to_be_solved(root)) >1e-10:
        init_guess = np.array(range(1, num_circles+1)) + num_circles*[perturbation]
        root = fsolve(func_to_be_solved, init_guess , xtol = 1e-12)
        perturbation +=0.1



    # Test to check that the output put of fsolve is correct

    teste  = np.linalg.norm(func_to_be_solved(root))
    if teste >1e-10:
        print('num_lines =', num_lines, 'num_circles = ', num_circles, 'Problem!!!!' )
        #print(teste)
        #print(func_to_be_solved(root))
        #print(np.isclose(func_to_be_solved(root), [0.0]*num_circles))
    return root
