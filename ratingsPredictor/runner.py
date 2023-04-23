from dataProcessor import readCSVDataFile, runProcessingSuite
from ratingsPredictor.util import getDataDirectoryPath


def main():
    print('Running Predictor')

    csvPath = getDataDirectoryPath() + '/SmackdownRatingsRaw.csv'
    df = readCSVDataFile(csvPath)

    processedDf = runProcessingSuite(df)

    print(processedDf.to_string())


if __name__ == "__main__":
    main()
