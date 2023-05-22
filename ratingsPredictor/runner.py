from dataProcessor import runProcessingSuite
from ratingsPredictor.predictionModel import runPredictionModel
from ratingsPredictor.util import getDataDirectoryPath, readCSVDataFile, runFeatureSelection, getModelColumnInputs, \
    setDisplayMaxColumns


def main():
    print('Running Predictor')
    setDisplayMaxColumns(None)
    csvPath = getDataDirectoryPath() + '/SmackdownRatingsRaw.csv'
    df = readCSVDataFile(csvPath)

    modelInputs = getModelColumnInputs()
    featureColumns = modelInputs.get('featureColumns')

    targetColumn = modelInputs.get('targetColumn')

    processedDf = runProcessingSuite(df)

    runFeatureSelection(processedDf, featureColumns, targetColumn)

    runPredictionModel(processedDf)


if __name__ == "__main__":
    main()
