# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np

def generate_mass_dist(num_circles,factor ,m_0):
    mass_dist = [m_0, 1.]
    index = 2

    while index <= num_circles:
        next_mass = mass_dist[-1]*factor
        mass_dist.append(next_mass)
        index +=1

    return np.array(mass_dist)


if __name__ == '__main__':
    mass = generate_mass_dist( num_circles, factor_mass, m_0)
    print(mass)
