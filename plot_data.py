# -*- coding: utf-8 -*-
#==============================================================================
import matplotlib.pyplot as plt
from read_data import *


def plot(num_lines,num_circles):
    x_axis, y_axis = read_data(num_lines,num_circles)
    xmax , xmin = np.amax(x_axis) , np.amin(x_axis)
    ymax , ymin = np.amax(y_axis) , np.amin(y_axis)

    #print(x_axis)
    #print(y_axis)

    plt.figure()
    plt.plot(x_axis,y_axis , "o")
    #plt.axis([xmin-1, xmax+1, ymin -1 , ymax+1])
    plt.axis([-5,5,-5,5])

    num_lines, num_circles = str(num_lines) , str(num_circles)
    plt.savefig("figs/num_lines_"+num_lines+"_and_num_circles_"+num_circles )






if __name__ == '__main__':
    plot(2,1)
