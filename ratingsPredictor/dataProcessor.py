import pandas as pd
from util import getDataDirectoryPath


def readCSVDataFile(filePath=None):
    print('Reading CSV Data at:', filePath)

    df = pd.read_csv(filePath)

    print(df.to_string())

    return df
