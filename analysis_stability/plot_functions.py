from functions import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def readFile(nameFile):

    quantity_values, percent_values = np.array([]) , np.array([])
    file = open(nameFile)
    lines = file.readlines()
    for line in lines[:]:
        words = line.split()
        quantity, percent = float(words[0]) , float(words[-1])
        quantity_values = np.append(quantity_values,quantity)
        percent_values = np.append(percent_values,percent)
    file.close()
    return [quantity_values , percent_values]
        


def plotUnstableConfByQuantity(nameFile):

    x_axis , y_axis = readFile(nameFile)
    print(x_axis)
    print(y_axis)
    plt.bar(x_axis, y_axis)
    plt.savefig("figs/percFigs/perc"+nameFile)
    plt.close()


def PlotNumLinesByNumCircles():
    
    df = pd.read_csv('allConfig.csv')
    unstableDF = unstableConfigurations(df)[0]
    unstableDF.plot('NumLines', 'NumCircles', style = '.')
    plt.savefig('figs/frequency')



    
if __name__=='__main__':
    #plotUnstableConfByQuantity('RegisterByNumberOfLines')
    #plotUnstableConfByQuantity('RegisterByNumberOfCircles')
    #plotUnstableConfByQuantity('RegisterByNumberOfBodies')
    PlotNumLinesByNumCircles()