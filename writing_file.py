# -*- coding: utf-8 -*-
#==============================================================================
from points_configuration import*

def writing_data(num_circles, num_lines, root, theta,mass_dist):
    circle = str(num_circles)
    lines = str(num_lines)
    name_file = "num_lines_" + lines+"_and_num_circles_"+circle
    file = open("data/"+name_file, "w")
    points = central_configuration(root, theta)
    for point in points:
        x , y = point
        x = str(x)
        y = str(y)
        file.write(x+" "+ y+"\n")

    for mass in mass_dist:
        mass = str(mass)
        file.write(mass + " ")
    #file.write(points)
    #file.write(mass)
    file.close()







if __name__ == '__main__':
    from parameters import *
    from fsolve_method import *
    #writing_data(num_circles,num_lines)
    #several_data(1,5,1,5)
