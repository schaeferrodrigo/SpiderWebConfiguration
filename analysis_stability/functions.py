import pandas as pd
import os


def createDataFrame(fileData):
    dataFrame = pd.read_csv(fileData, sep= " " , header= None, names= ["Type", "Stability","NumBodies" , "NumLines" , "NumCircles"])
    return dataFrame

def unstableConfigurations( dataFrame ):
    df = dataFrame[dataFrame["Stability"] == "unstable"]
    return [df, df.shape[0]]

def dataFrameNumBodies(numberOfBodies, dataFrame):
    df = dataFrame[dataFrame['NumBodies']==numberOfBodies]
    return [df,df.shape[0]]

def dataFrameNumCircles(numberOfCircles,dataFrame):
    df = dataFrame[dataFrame['NumCircles']==numberOfCircles]
    return [df,df.shape[0]]

def dataFrameNumLines(numberOfLines,dataFrame):
    df = dataFrame[dataFrame['NumLines']==numberOfLines]
    return [df,df.shape[0]]
    

def getUnstableConfigByNumOfBodies( numberOfBodies, dataFrame):
    df , size = dataFrameNumBodies(numberOfBodies, dataFrame)
    dfUnstable , sizeUnstable = unstableConfigurations(df)
    percent = sizeUnstable/size
    return [dfUnstable, sizeUnstable, size , percent]       


def getUnstableConfigByNumOfLines( numberOfLines,dataFrame):
    df , size = dataFrameNumLines(numberOfLines, dataFrame)
    dfUnstable , sizeUnstable = unstableConfigurations(df)
    percent = sizeUnstable/size
    return [dfUnstable, sizeUnstable, size , percent] 

def getUnstableConfigByNumOfCircles(numberOfCircles, dataFrame):
    df , size = dataFrameNumCircles(numberOfCircles, dataFrame)
    dfUnstable , sizeUnstable = unstableConfigurations(df)
    percent = sizeUnstable/size
    return [dfUnstable, sizeUnstable, size , percent] 


def RegisterByNumOfBodies(dataFrame):
    namefile = 'RegisterByNumberOfBodies'
    file = open(namefile, "w")
    listOfNumBodies = dataFrame['NumBodies'].unique()
    for numberOfBodies in listOfNumBodies:
        unstable , total, percent = getUnstableConfigByNumOfBodies(numberOfBodies, dataFrame)[1:]
        file.write(str(numberOfBodies) +" "+ str(unstable) +  " " +  str(total)+ " " + str(percent)+ "\n")
    file.close()

def RegisterByNumOfCircles(dataFrame):
    namefile = 'RegisterByNumberOfCircles'
    file = open(namefile, "w")
    listOfNumCircles = dataFrame['NumCircles'].unique()
    for numberOfCircles in listOfNumCircles:
        unstable , total, percent = getUnstableConfigByNumOfCircles(numberOfCircles, dataFrame)[1:]
        file.write(str(numberOfCircles) +" "+ str(unstable) +  " " +  str(total)+ " " + str(percent)+ "\n")
    file.close()

def RegisterByNumOfLines(dataFrame):
    namefile = 'RegisterByNumberOfLines'
    file = open(namefile, "w")
    listOfNumLines = dataFrame['NumLines'].unique()
    for numberOfLines in listOfNumLines:
        unstable , total, percent = getUnstableConfigByNumOfLines(numberOfLines, dataFrame)[1:]
        file.write(str(numberOfLines) +" "+ str(unstable) +  " " +  str(total)+ " " + str(percent)+ "\n")
    file.close()

def generateSeparateData():

    #os.chdir('./')

    #print(os.listdir())

    fileData = '../data/linear_no_23'
    originalDataFrame = createDataFrame(fileData)
    totalSize = originalDataFrame.shape[0]
    print(originalDataFrame.tail())
    print("total data = ", totalSize)

    dfUnstable ,numberUnstableConfigurations = unstableConfigurations(originalDataFrame)
    
    print("number of unstable configurations = ", numberUnstableConfigurations, '\n') 

    percUnstable = numberUnstableConfigurations/totalSize
    print("percentual of unstable configurations = " , percUnstable)

    RegisterByNumOfBodies(originalDataFrame)
    RegisterByNumOfLines(originalDataFrame)
    RegisterByNumOfCircles(originalDataFrame)

    return 0

if __name__=='__main__':
    generateSeparateData()
    