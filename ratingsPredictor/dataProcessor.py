from ratingsPredictor.util import getRenamedColumnNames, getColumnsToBeKept, getColumnTypes, getRatingsColumns


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

    return df.assign(prelimToFinalDifference=lambda x: abs(x.finalNumber - x.prelimAvg))


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


