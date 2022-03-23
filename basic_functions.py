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

def phi_and_derivatives(r , theta,num_lines ):
    phi_value = 0.
    first_der_value = 0.
    second_der_value =0.
    for k in range(0, num_lines):
        term = 1/np.sqrt(1 + r**2 -2*r*np.cos(theta[k]))
        phi_value += term

        first_num = np.cos(theta[k]) - r
        first_der_value += first_num*(term)**3

        second_num = -1-r**2 +2*r*np.cos(theta[k]) +3 *first_num**2
        second_der_value = second_num *(term)**5

    return [phi_value, first_der_value, second_der_value]

def force_mi(radii, index , jndex , mass_dist , num_lines , theta):
    if jndex == 0:
        return - mass_dist[jndex]/radii[index]**2

    elif jndex == index:
        return -mass_dist[index]*xi(theta,num_lines) /((2**(3/2))*(radii[index]**2))

    elif jndex >0 and jndex <1 :
        y = radii[jndex]/radii[index]
        phi , der_phi = phi_and_derivatives(y , theta, num_lines)[0:2]
        return -mass_dist[jndex]*(phi + y*der_phi)/radii[index]**2
    else:
        x = radii[index]/radii[jndex]
        der_phi= phi_and_derivatives(x , theta, num_lines)[1]
        return mass_dist[jndex]*(x**2)*der_phi/radii[index]**2

def vector_f(radii, mass_dist , num_lines , theta , num_circles):
    vector = []
    for index in range(1, num_circles +1):
        sum = 0.
        for jndex in range(1, num_circles+1):
            sum+= force_mi(radii, index , jndex , mass_dist , num_lines , theta)
        value_ith = -radii[index] - sum # lambda = -1
        vector.append(value_ith)
    return np.array(vector)


def der_f(radii, num_circles,num_lines, mass_dist, theta , m_0):
    Jacobian_matrix = []
    for index in range(1, num_circles+1):
        row = []
        for jndex in range(1 , num_circles+1):
            if jndex == index:

                first_part = mass_dist[index]*xi(theta , num_lines)/np.sqrt(2) - 2*m_0
                #print(first_part)
                #first sum:
                if index == 1:
                    sum_1 =0.
                else:
                    sum_1 = 0.
                    for k in range(1,index):
                        y = radii[k]/radii[index]
                        phi , first_der_phi , second_der_phi = phi_and_derivatives(y , theta,num_lines )
                        term = mass_dist[k]*(2 * phi + 4*y*first_der_phi + (y**2)*second_der_phi)
                        sum_1 += term

                #second sum:
                if index ==num_circles:
                    sum_2 = 0.
                else:
                    sum_2 = 0.
                    for k in range(index+1 , num_circles+1):
                        x = radii[index]/radii[k]
                        second_der_phi = phi_and_derivatives(x , theta,num_lines )[2]
                        term_2 = mass_dist[k]*(x**3)*second_der_phi
                        sum_2 += term_2
                print("radii=" ,radii[index])
                value_der_f = -1-(first_part - sum_1 - sum_2)/radii[index]**3

            elif jndex < index:
                y = radii[jndex]/radii[index]
                first_der_phi , second_der_phi =  phi_and_derivatives(y , theta,num_lines )[1:3]
                value_der_f = mass_dist[jndex]*(2*first_der_phi + y*second_der_phi)/radii[index]**3
            else:
                x = radii[index]/radii[jndex]
                first_der_phi , second_der_phi =  phi_and_derivatives(x , theta,num_lines )[1:3]
                value_der_f = (x**3)*mass_dist[jndex]*(2*first_der_phi + x*second_der_phi)/radii[index]**3
            row.append(value_der_f)
        Jacobian_matrix.append(row)
    return  np.array(Jacobian_matrix)



def lambda_i(index , radii , mass_dist, num_lines, theta,num_circles):
    sum = 0
    for jndex in range(1 , num_circles + 1 ):
        term = force_mi(radii, index, jndex , mass_dist, num_lines, theta)
        sum += term
    return sum/radii[index]

def Lambda(radii, mass_dist, num_lines, theta,num_circles):
    L= [0 ]
    for index in range(1, num_circles):
        Lambda_i = lambda_i(index , radii , mass_dist, num_lines, theta,num_circles) - lambda_i(index+1 , radii , mass_dist, num_lines, theta,num_circles)
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
    print(phi_and_derivatives(0.5,theta,num_lines ))
    print(force_mi([0,0.5,2], 1 , 1, mass_dist , num_lines , theta))
    print(vector_f([0,0.5,2], mass_dist , num_lines , theta,num_circles))
    print(lambda_i( 1 , [0,0.5,2] , mass_dist , num_lines , theta,num_circles  ))
    print(Lambda([0,0.5,2] , mass_dist , num_lines , theta , num_circles ))
    print( der_f([0,1,5], num_circles,num_lines, mass_dist, theta,1.))
