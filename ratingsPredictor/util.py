import os


def getDataDirectoryPath():
    cwd = os.getcwd()
    parentDir = os.path.dirname(cwd)

    dataDir = parentDir + '/data'

    print('Data Directory: ', dataDir)

    return dataDir


