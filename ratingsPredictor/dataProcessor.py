import pandas as pd


def runProcessingSuite(df):
    print('Running Processing Suit')

    keepCols = columnsToBeKept()

    reducedDf = removeExtraColumns(df, keepCols)

    processedDf = (
        reducedDf
        .rename(columns=renamedColumnNames())
        .replace(to_replace='-', value=None)
        .dropna()
    )
    return processedDf


def readCSVDataFile(filePath=None):
    print('Reading CSV Data at:', filePath)

    df = pd.read_csv(filePath)

    return df


def removeExtraColumns(df, keepColumns):
    return df[keepColumns]


def columnsToBeKept():
    return ['Date', 'Prelim: 8pm', 'Prelim: 9pm', 'Prelim: Avg', 'Final', 'Prelim to final adjustment']


def renamedColumnNames():
    return {'Date': 'date',
            'Prelim: 8pm': 'prelim8PM',
            'Prelim: 9pm': 'prelim9PM',
            'Prelim: Avg': 'prelimAvg',
            'Final': 'finalNumber',
            'Prelim to final adjustment': 'prelimToFinalAdjustment'}
