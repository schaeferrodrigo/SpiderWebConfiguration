# -*- coding: utf-8 -*-
#==============================================================================
import matplotlib.pyplot as plt
import numpy as np

def read_data(num_lines, num_circles):
    num_lines , num_circles= str(num_lines) , str(num_circles)

    x_values  = np.array([])
    y_values = np.array([])
    file = open("data/num_lines_"+num_lines+"_and_num_circles_"+num_circles ,"r")
    lines = file.readlines()
    for line in lines[:-1]:
        x,y = line.split()
        x ,y = float(x) , float(y)
        x_values = np.append(x_values, x)
        y_values =np.append(y_values, y)
        #print([x,y])
    file.close()
    return [x_values, y_values]


if __name__ == '__main__':
    x,y =read_data(2,1)
    print(x)
    print(y)
