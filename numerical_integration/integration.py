import numpy as np
from scipy import integrate
import os

def extractInformationFromNameFile(nameFile):
    Information=nameFile.split('_')
    numLines, numCircles = int(Information[2]) , int(Information[-1])
    return [numLines, numCircles]

def setNumOfLines(nameFile):
    global numLines
    numLines = extractInformationFromNameFile(nameFile)[0]
    return numLines


def circlePosition(index, numLines):
    return int(np.ceil(index/numLines))

def matrixMasses(circle, masses):
    Matrix = np.array([[masses[circle],0],[0,masses[circle]]])
    return Matrix

def setInitialMomenta(x, masses):
    numOfBodies = len(x)
    J = np.array([[0,1],[-1,0]])
    y = np.zeros((numOfBodies,2), dtype=object)
    for i in range(0, numOfBodies):
        circle = circlePosition(i,numLines)
        #print('circle = ', circle)
        M = matrixMasses(circle,masses)
        #print(x[i])
        y[i] = M.dot(J.dot(x[i]))
    return y


def gradU(index, numberOfBodies, x, masses):
    mass_i = masses[circlePosition(index , numLines)]
    gradU = np.zeros(2)
    x_i = x[index].astype('float64')
    for jndex in range(0,numberOfBodies):
        if jndex != index:
            mass_j = masses[circlePosition(jndex , numLines)]
            x_j = x[jndex].astype('float64')
            #print('gradU_i = ',mass_j*mass_i*(x_j - x_i)/np.linalg.norm(x_j-x_i)**3)
            gradU += mass_j*mass_i*(x_j - x_i)/np.linalg.norm(x_j-x_i)**3
    return gradU       

def vectorField(t,z):
    numberOfBodies = int(len(z)/4)
    
    x, y = np.array(z[0:int(len(z)/2)]).reshape(numberOfBodies,2) , np.array(z[int(len(z)/2):]).reshape(numberOfBodies, 2)
    J = np.array([[0,1],[-1,0]]) 
    dotX, dotY = np.zeros((numberOfBodies,2), dtype=object ) , np.zeros((numberOfBodies,2), dtype=object)
    matrixMass = np.array([[1,0],[0,1]])
    
    for index in range(0,numberOfBodies):

        #print(matrixMass)
        #print(x[index])
        inverseMatrix = np.linalg.inv(matrixMass)
        
        dotX[index] = -J.dot(x[index]) + inverseMatrix.dot(y[index])
        dotY[index] = -J.dot(y[index]) + gradU(index,numberOfBodies,x,masses ) 
        circle = int(np.ceil(index/numLines))
        if circle != np.ceil((index+1)/numLines) and (index+1)<numberOfBodies:
            matrixMass = matrixMasses(circle+1, masses)
    

 
    return np.append(dotX,dotY , 0)


def readData(nameFile):
    position = np.array([])
    file = open('../data/'+nameFile)
    lines = file.readlines()
    numOfBodies = len(lines[:-1])
    position = np.zeros((numOfBodies,2), dtype=object)
    index = 0
    for line in lines[:-1]:
        x1,x2 = line.split()
        position[index] = np.array([float(x1) , float(x2)])
        index +=1
    masses = lines[-1].split()
    masses = np.array([float(x) for x in masses])
    file.close()
    return [position , masses , numOfBodies]

def writeData(listOfValues,nameOfFile, folder):
    nameFile = nameOfFile+ folder
    file = open('data/'+ folder+'/' + nameFile, 'a' )
    if folder != 'time':
        for value in listOfValues:
            value = str(value)
            file.write( value + '\n')
    else:
        file.write(str(listOfValues) + '\n')
    file.close()
    


def Potential(index,masses, circle, position):
    if index==0:
        return 0
    U = 0
    for i in range(0,index):
        circle_i = circlePosition(i, numLines) 
        if circle == circle_i:
            m_i = masses[circle]
        else:
            m_i = masses[circle_i]
        U += masses[circle]*m_i/np.linalg.norm(position[i]-position[index])
    return U


def Hamiltonian(position, momentum, masses, numOfBodies, numLines):
    position = position.reshape(numOfBodies,2)
    momentum = momentum.reshape(numOfBodies, 2)
    J =  np.array([[0,1],[-1,0]])

    energyValue = 0
    for index in range(0, numOfBodies):
        circle = circlePosition(index,numLines)
        M_i_inverse =np.linalg.inv(matrixMasses(circle , masses))
        Kinectic = momentum[index].dot(M_i_inverse.dot(momentum[index]))/2
        MixedTerms = momentum[index].dot(J.dot(position[index]))
        functionU = Potential(index, masses, circle,position)
        energyValue += Kinectic + MixedTerms - functionU
    return energyValue

def testHamiltonian(listHamiltonian, nameFile , H_0):
    name = nameFile + '_test'
    file = open('data/'+'hamiltonianTest/'+ name , 'w')
    maxRelativeError =np.amax(np.absolute(np.diff(listHamiltonian) ))
    maxAbsoluteError =np.amax(np.absolute(listHamiltonian - H_0))
    file.write('RE'+ ' ' + str(maxRelativeError) + '\n')
    file.write('AE' + ' '+str(maxAbsoluteError))
    file.close()

        
def IntegrationProcess(file):
    global masses
    x, masses , numOfBodies= readData(file)
    #print(x)
    
    setNumOfLines(file)
    #print('number of bodies = ', numOfBodies, 'and number of lines = ', numLines)
    y = setInitialMomenta(x,masses)
    
    initialCondition = np.append(x,y,0).reshape(4*numOfBodies)
    
    H_0 = Hamiltonian(initialCondition[:2*numOfBodies], initialCondition[2*numOfBodies:], masses, numOfBodies, numLines)
    #print('initial value of Hamiltonian function = ' , H_0)
    listOfEnergyValues = np.array([])
    tMax = 300
    solution = integrate.DOP853(vectorField,0,initialCondition, t_bound = tMax, rtol = 1e-10, atol = 1e-12 , vectorized=True)
    time  = 0
    while time < tMax:
        solution.step()
        time = solution.t
        print('time = ', time)
        position = solution.y[:2*numOfBodies]
        momentum = solution.y[2*numOfBodies:]
        writeData(position, file, 'position')
        writeData(momentum, file , 'momentum')
        writeData(time, file, 'time')
        listOfEnergyValues = np.append(listOfEnergyValues , Hamiltonian(position, momentum,masses, numOfBodies,numLines))
    testHamiltonian(listOfEnergyValues, file, H_0)
    print('integration is finished')





def main():

    files = os.listdir('../data/')
    control = 1
    total = len(files)
    print('number of files = ',total)
    for file in files:
        print(file)
        
        if file[:3] == 'num':
            
            IntegrationProcess(file)
            print('remainder = ', total- control)
            control += 1
        else:
            total -=1
            print('new total of files = ', total)
    

        

    
if __name__=='__main__':

    #setNumOfLines('num_lines_2_and_num_circles_1')

    # #print('number of lines = ', numLines)
    #masses = [1.0 , 0.5]
    #q= np.array([[0 , 0] , [0.5, 0], [-0.5, 0]])
    #pq= setInitialMomenta(q, masses)
    #print(np.append(q,pq,0).reshape(4*3))
    
    #print(pq)
    # print(pq.shape , q.shape)
    # vector = np.append(q,pq , 0)
    
    # print('\n',vectorField(0 , vector), '\n')

    main()
    #print(readData('num_lines_2_and_num_circles_1'))
    #print(np.linalg.inv(matrixMasses(1,masses)))
    #U = gradU(0, 3, q,masses)
    #print('U= ' , U)
    
   