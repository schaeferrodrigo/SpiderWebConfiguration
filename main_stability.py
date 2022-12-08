# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np
import parameters as par
from read_data import *
from Diff_potential import *
from mass_dist_generator import *


def main():
    factor_mass = par.factor_mass
    m_1 = par.m_1
    inf_c , sup_c = par.inf_c, par.sup_c
    inf_l , sup_l = par.inf_l, par.sup_l

    name_file = "linear_stability"
    file = open("data/"+name_file, "w")

    for num_circles in range(inf_c, sup_c+1):
        for line in range(inf_l, sup_l):
            num_lines = 2*line
            mass_dist = generate_mass_dist(num_circles,factor_mass ,m_1)
            x_values, y_values = read_data(num_lines,num_circles)
            result = linear_instability(num_lines, num_circles,mass_dist , x_values, y_values)
            file.write(result + ' '+str(num_lines*num_circles+1)+' ' +str(num_lines)+' '+str(num_circles) + '\n')
    file.close()


if __name__ == '__main__':
    main()
