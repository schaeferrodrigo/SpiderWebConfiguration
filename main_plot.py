# -*- coding: utf-8 -*-
#==============================================================================
import parameters as par
from plot_data import *


def main_plot():

    inf_c , sup_c = par.inf_c, par.sup_c
    inf_l , sup_l = par.inf_l, par.sup_l

    for num_circles in range(inf_c, sup_c+1):
        for line in range(inf_l, sup_l):
            num_lines = 2*line
            plot(num_lines, num_circles)


if __name__ == '__main__':
    main_plot()
