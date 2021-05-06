from plotly.offline import plot
import plotly.express as px

sentiment_table = {'courier': ['DHL', 'PosLaju', 'NinjaVan', 'GDex', 'JNT'],  #these are just dummy data, need to replace with actual ones which we webscrapped
            'positive': [7, 8, 5, 6, 3],    # first numbers refer to the total number of sentiment words for first courier and so on
            'negative': [6, 3, 1, 5, 2], 
            'neutral': [10, 13, 9, 12, 9]
            }
fig = px.bar(sentiment_table, title='Sentiment Graph', x="courier", y=["positive", "negative", "neutral"])   #plotting the graph 
plot(fig, False, "", True, filename='file.html')  #display the graph in file.html
