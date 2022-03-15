# -*- coding: utf-8 -*-
#===============================================================================
import numpy as np

def angles(num_lines):
    all_theta= []
    for k in range(0 , num_lines):
        all_theta.append( 2*np.pi* k / num_lines)
    return np.array(all_theta)

def xi( theta , num_lines ):
    sum = 0
    for index in range(1,num_lines):
        element = 1/np.sqrt(1-np.cos(theta[index]))
        sum += element
    return sum


def force_mi(radii, index , jndex , mass_dist , num_lines , theta):
    if jndex == 0:
        return - mass_dist[jndex]/radii[index]**2

    elif jndex == index:
        return -mass_dist[index]*xi(theta,num_lines) /((2**(3/2))*(radii[index]**2))

    else:
        sum = 0
        for k in range( 0 , num_lines ):
            theta_k = theta[k]
            num = mass_dist[jndex]*(radii[index] - radii[jndex]*np.cos(theta_k))
            den = (radii[index]**2 + radii[jndex]**2 - 2*radii[index]*radii[jndex]*np.cos(theta[k]))**(3/2)
            term = -num/den
            sum += term
        return sum


def lambda_i(index , radii , mass_dist, num_lines, theta):
    sum = 0
    for jndex in range(1 , num_circles + 1 ):
        term = force_mi(radii, index, jndex , mass_dist, num_lines, theta)
        sum += term
    return sum/radii[index]

def Lambda(radii, mass_dist, num_lines, theta):
    L= [0 ]
    for index in range(1, num_circles):
        Lambda_i = lambda_i(index , radii , mass_dist, num_lines, theta) - lambda_i(index+1 , radii , mass_dist, num_lines, theta)
        L.append(Lambda_i)
    return np.array(L)

#===============================================================================
#teste

if __name__ == '__main__':
    from parameters import *
    theta = angles(num_lines)
    xi_value = xi(theta, num_lines)
    print(theta)
    print(xi_value - (2 + np.sqrt(2)/2))
    print(force_mi([0,0.5,2], 1 , 1, mass_dist , num_lines , theta))
    print(lambda_i( 1 , [0,0.5,2] , mass_dist , num_lines , theta  ))
    print(Lambda([0,0.5,2] , mass_dist , num_lines , theta ))
