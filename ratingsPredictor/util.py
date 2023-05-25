import os

import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


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


def setDisplayMaxColumns(maxColumns=None):
    pd.set_option('display.max_columns', maxColumns)


def runFeatureSelection(df, featureColumns, targetColumn, indexesRequired=True):
    print('Running Feature Selection')

    if indexesRequired:
        featureColumns = df.columns.get_indexer(featureColumns)
        targetColumn = df.columns.get_indexer(targetColumn)

    X = df.iloc[:, featureColumns]
    Y = df.iloc[:, targetColumn]

    best_features = SelectKBest(score_func=chi2, k=3)
    fit = best_features.fit(X, Y)

    df_scores = pd.DataFrame(fit.scores_)
    df_columns = pd.DataFrame(X.columns)

    features_scores = pd.concat([df_columns, df_scores], axis=1)
    features_scores.columns = ['Features', 'Score']
    features_scores.sort_values(by='Score')

    print(features_scores.head())


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
        'date': 'datetime64[ns]',
        'prelim8PM': 'int32',
        'prelim9PM': 'int32',
        'prelimAvg': 'int32',
        'finalNumber': 'int32',
    }


def getModelColumnInputs():
    return {
        'featureColumns': ['prelim8PM', 'prelim9PM', 'prelimAvg', 'prelimToFinalDifference'],
        'targetColumn': ['finalNumber']
    }
