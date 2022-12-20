import pandas as pd


def createDataFrame(fileData):

    dataFrame = pd.read_csv(fileData, sep= " " , header= None, names= ["Type", "Stability","NumBodies" , "NumLines" , "NumCircles"])
    return dataFrame

def unstableConfigurations( dataFrame ):
    df = dataFrame[dataFrame["Stability"] == "unstable"]
    return [df, df.shape[0]]

def dataFrameNumBodies(numberOfBodies, dataFrame):
    df = dataFrame[dataFrame['NumBodies']==numberOfBodies]
    return [df,df.shape[0]]

def getUnstableConfigByNumOfBodies( numberOfBodies, dataFrame):
    df , size = dataFrameNumBodies(numberOfBodies, dataFrame)
    dfUnstable , sizeUnstable = unstableConfigurations(df)
    percent = sizeUnstable/size
    return [dfUnstable, sizeUnstable, size , percent]       

def RegisterByNumOfBodies(dataFrame):
    namefile = 'RegisterByNumberOfFiles'
    file = open(namefile, "w")
    listOfNumBodies = dataFrame['NumBodies'].unique()
    for numberOfBodies in listOfNumBodies:
        unstable , total, percent = getUnstableConfigByNumOfBodies(numberOfBodies, dataFrame)[1:]
        file.write(str(numberOfBodies) +" "+ str(unstable) +  " " +  str(total)+ " " + str(percent)+ "\n")
    file.close()        


def main():

    fileData = "./data/linear_stability"
    originalDataFrame = createDataFrame(fileData)
    totalSize = originalDataFrame.size
    print(originalDataFrame.head())
    print("total data = ", totalSize)



    dfUnstable ,numberUnstableConfigurations = unstableConfigurations(originalDataFrame)
    
    print("number of unstable configurations = ", numberUnstableConfigurations, '\n') 

    percUnstable = numberUnstableConfigurations/totalSize
    print("percentual of unstable configurations = " , percUnstable)

    RegisterByNumOfBodies(originalDataFrame)

    return 0

if __name__=='__main__':
    main()
    