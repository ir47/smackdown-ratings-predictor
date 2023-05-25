import plotly.express as px


def plotPredictedVsActual(predictions):
    predictions = predictions.reset_index()
    predictions.sort_values(by='date', inplace=True)

    fig = px.line(
        predictions,
        x='date',
        y=['actualRating', 'predictedRating'],
        markers=True,
        title='First Model Prediction Results',
    )
    fig.show()
