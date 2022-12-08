# -*- coding: utf-8 -*-
#=============================================================================
import parameters as par
from mass_dist_generator import *
from basic_functions import *
from fsolve_method import *
from writing_file import *


def main():
    factor_mass = par.factor_mass
    m_1 = par.m_1

    inf_c , sup_c = par.inf_c, par.sup_c
    inf_l , sup_l = par.inf_l, par.sup_l

    for num_circles in range(inf_c, sup_c+1):
        for line in range(inf_l, sup_l):
            num_lines = 2*line

            mass_dist = generate_mass_dist(num_circles,factor_mass ,m_1)
            theta = angles(num_lines)

            root = solution_method(mass_dist, num_lines,theta,num_circles)

            writing_data(num_circles,num_lines,root,theta,mass_dist)


if __name__ == '__main__':
    main()
