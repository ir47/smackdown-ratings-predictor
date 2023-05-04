import pandas as pd


def runProcessingSuite(df):
    print('Running Processing Suit')

    keepCols = getColumnsToBeKept()
    columnTypes = getColumnTypes()

    reducedDf = removeExtraColumns(df, keepCols)

    processedDf = performDataFrameProcessing(reducedDf, columnTypes)

    ratingsColumns = getRatingsColumns()

    fullyProcessedDf = performRatingsProcessing(processedDf, ratingsColumns)

    return fullyProcessedDf


def performRatingsProcessing(df, ratingsColumns):
    df[ratingsColumns] = df[ratingsColumns].apply(addMillions)

    return df.assign(prelimToFinalDifference=lambda x: x.finalNumber - x.prelimAvg)


def addMillions(rating):
    return rating * 1000


def removeExtraColumns(df, keepColumns):
    return df[keepColumns]


def performDataFrameProcessing(df, columnTypes):
    return (
        df
        .rename(columns=getRenamedColumnNames())
        .replace(to_replace='-', value=None)
        .replace(to_replace=',', value='', regex=True)
        .dropna()
        .astype(columnTypes)
    )


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
