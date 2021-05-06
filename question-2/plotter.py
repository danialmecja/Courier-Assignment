from plotly.offline import plot
import plotly.express as px

sentiment_table = {'courier': ['DHL', 'PosLaju', 'NinjaVan', 'DHL', 'PosLaju', 'NinjaVan', 'DHL', 'PosLaju', 'NinjaVan'],
            'sentiment': ['Positive', 'Positive', 'Positive', 'Negative', 'Negative', 'Negative', 'Neutral', 'Neutral', 'Neutral'],
            'count': [7, 9, 3, 3, 2, 0, 10, 12,7]
            }
fig = px.bar(sentiment_table, title='Sentiment Graph', x="courier", y="count", color="sentiment")
#data_or_figure = [{"x": DHL_Sentiment}]
plot(
    fig, False, "", True, filename='file.html')
