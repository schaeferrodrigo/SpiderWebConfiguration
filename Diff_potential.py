# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np


def S_ij(x,y, xx, yy , m_i, m_j):
    dx , dy = x -xx , y-yy
    r = np.sqrt((x-xx)**2 + (y-yy)**2)
    u_ij = np.array([dx/r,dy/r ])

    first_term  = m_i*m_j/(r**3)
    second_term = np.diag([1,1]) - 3*u_ij*u_ij.reshape(2,1)
    return  first_term*second_term


def DV_matrix(num_lines, num_circles,mass_dist , x_values, y_values):

    all_bodies = num_lines*num_circles + 1
    DV_value = np.zeros([all_bodies,all_bodies], dtype = object)

    mass=[mass_dist[0]]
    for index in range(1, len(mass_dist)):
        mass.extend([mass_dist[index]]*num_lines)

    print(mass)
    for i in range(0, all_bodies ):

        M_i =np.diag(np.array([mass[i],mass[i]]))
        print('index i = ',i)
        sum = 0
        if i != 0:
            for j in range(0, i):
                print('index j =', j)
                DV_value[i,j] = DV_value[j,i]
                sum += DV_value[i,j]
        if i != (all_bodies -1):
            for j in range(i+1, all_bodies):
                print('index j =', j)
                m_i, m_j = mass[i],mass[j]
                x , y = x_values[i] , y_values[i]
                xx , yy = x_values[j] , y_values[j]
                s_ij = S_ij(x,y, xx, yy, m_i, m_j)
                print('values of S_ij = ', s_ij)
                DV_value[i,j] = s_ij
                sum += s_ij

        print('mass matrix= ' , M_i)
        print("the sum is " , sum)
        DV_value[i,i] = M_i - sum
        line = np.concatenate(DV_value[i,:],axis = 1).reshape(2, 2*all_bodies)
        if i == 0:
            matrix = line
        else:
            matrix = np.concatenate([matrix, line], axis =0).reshape(2*(i+1), 2*all_bodies)
    return [DV_value,matrix]


def linear_instability(num_lines, num_circles,mass_dist , x_values, y_values):

    D2V = DV_matrix(num_lines, num_circles,mass_dist , x_values, y_values)

    eigenvalues = np.linalg.eig(D2V[1])[0]
    odd_check = 0

    for eigenvalue in eigenvalues:
        print('eigenvalue = ', eigenvalues)
        if np.abs(eigenvalue) <=1e-6:
            return 'impossible to define'
        if eigenvalue < 0:
            odd_check +=1

    if odd_check % 2 == 0:
        return 'linear stable'
    else:
        return 'linear unstable'





if __name__ == '__main__':
    from mass_dist_generator import *

    mass = generate_mass_dist( 2, 0.8, 2)
    x_values = [0.0 , 0.6299605249474365 , -0.6299605249474365]
    y_values = [0.0,0.0,7.714791404660645e-17 ]


    DV = DV_matrix(1,1, mass, x_values, y_values)
    print('DV = ', DV[0])
    print('whole_matrix= ',DV[1])
    print('eigenvalues = ', np.linalg.eig(DV[1]))
    print('linear_instability?', linear_instability(1,1, mass, x_values, y_values))
