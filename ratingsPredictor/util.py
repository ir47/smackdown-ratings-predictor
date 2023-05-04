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


def getRatingsColumns():
    return ['prelim8PM', 'prelim9PM', 'prelimAvg', 'finalNumber']


def getColumnsToBeKept():
    return ['Date', 'Prelim: 8pm', 'Prelim: 9pm', 'Prelim: Avg', 'Final']


def getRenamedColumnNames():
    return {
        'Date': 'date',
        'Prelim: 8pm': 'prelim8PM',
        'Prelim: 9pm': 'prelim9PM',
        'Prelim: Avg': 'prelimAvg',
        'Final': 'finalNumber',
    }


def getColumnTypes():
    return {
        'date': 'datetime64',
        'prelim8PM': 'int32',
        'prelim9PM': 'int32',
        'prelimAvg': 'int32',
        'finalNumber': 'int32',
    }

