from dataProcessor import readCSVDataFile
from ratingsPredictor.util import getDataDirectoryPath


def main():
    print('Running Predictor')

    csvPath = getDataDirectoryPath() + '/SmackdownRatingsRaw.csv'
    readCSVDataFile(csvPath)


if __name__ == "__main__":
    main()
