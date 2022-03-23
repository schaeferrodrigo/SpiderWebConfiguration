# -*- coding: utf-8 -*-
#==============================================================================
from fsolve_method import*
from basic_functions import*
import numpy as np

def central_configuration(root, theta):
    points = np.array([[0,0]])
    for r in root:
        for the in theta:
            x = r*np.cos(the)
            y = r*np.sin(the)
            new_point = np.array([[x,y]])
            points = np.append(points,new_point, axis = 0 )
    return points


if __name__ == '__main__':
    print(central_configuration(root,theta))
