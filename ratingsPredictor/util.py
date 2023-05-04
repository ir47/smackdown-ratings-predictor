import os

import pandas as pd


def getDataDirectoryPath():
    cwd = os.getcwd()
    parentDir = os.path.dirname(cwd)

    dataDir = parentDir + '/data'

    print('Data Directory: ', dataDir)

    return dataDir


def readCSVDataFile(filePath=None):
    print('Reading CSV Data at:', filePath)

    df = pd.read_csv(filePath)

    return df
