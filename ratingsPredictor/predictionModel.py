from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from ratingsPredictor.util import getModelColumnInputs


def runPredictionModel(df):
    print('Running Prediction Model')

    df.index = df['date']

    columnInputs = getModelColumnInputs()
    featureColumns = columnInputs.get('featureColumns')
    targetColumn = columnInputs.get('targetColumn')

    X = df[featureColumns]
    Y = df[targetColumn]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=1000)

    logreg = LogisticRegression(max_iter=3000, solver='liblinear')
    logreg.fit(X_train, y_train.values.ravel())

    y_pred = logreg.predict(X_test)

    X_test['actualRating'] = y_test['finalNumber'].tolist()
    X_test['predictedRating'] = y_pred.tolist()

    print(X_test)
