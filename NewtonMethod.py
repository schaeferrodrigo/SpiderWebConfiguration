# -*- coding: utf-8 -*-
#==============================================================================
from basic_functions import *
import numpy as np
from parameters import *

def NewtonMethod(radii_initial, mass_dist , num_lines , theta,num_circles ,m_1):
    radii = radii_initial
    radii_norm  = np.delete(radii,0)
    print('inverse matrix =' ,np.linalg.inv(der_f(radii, num_circles,num_lines, mass_dist, theta,m_1)))
    print(vector_f(radii, mass_dist , num_lines , theta,num_circles))
    while np.linalg.norm(vector_f(radii, mass_dist , num_lines , theta,num_circles)) >1e-16:
        inverse_matrix = np.linalg.inv(der_f(radii, num_circles,num_lines, mass_dist, theta))
        #print('inverse matrix =' , inverse_matrixs)
        f = vector_f(radii, mass_dist , num_lines , theta,num_circles)
        next_r = radii_norm - np.dot(inverse_matrix, f)
        radii_norm = next_r
        radii= np.insert(radii_norm, 0 , 0 )
        #print("norm of f =", np.linalg.norm(vector_f(radii, mass_dist , num_lines , theta,num_circles)))
        #print('candidate = ', radii)
    return radii




if __name__ == '__main__':
    print(NewtonMethod([0,.5,1.5], mass_dist , num_lines , theta,num_circles,m_1))
