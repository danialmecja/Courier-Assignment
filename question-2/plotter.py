from plotly.offline import plot
import plotly.express as px

#DHL SENTIMENT WORDS
DHL_positive = open("question-2/Sentiment/Positive Words DHL.txt", "r")
DHL_negative = open("question-2/Sentiment/Negative Words DHL.txt", "r")
DHL_neutral = open("question-2/Sentiment/Neutral Words DHL.txt", "r")

#GDEX SENTIMENT WORDS
GDex_positive = open("question-2/Sentiment/Positive Words GDex.txt", "r")
GDex_negative = open("question-2/Sentiment/Negative Words GDex.txt", "r")
GDex_neutral = open("question-2/Sentiment/Neutral Words GDex.txt", "r")

#JNT SENTIMENT WORDS
JNT_positive = open("question-2/Sentiment/Positive Words JNT.txt", "r")
JNT_negative = open("question-2/Sentiment/Negative Words JNT.txt", "r")
JNT_neutral = open("question-2/Sentiment/Neutral Words JNT.txt", "r")

#NINJAVAN SENTIMENT WORDS
NinjaVan_positive = open("question-2/Sentiment/Positive Words NinjaVan.txt", "r")
NinjaVan_negative = open("question-2/Sentiment/Negative Words NinjaVan.txt", "r")
NinjaVan_neutral = open("question-2/Sentiment/Neutral Words NinjaVan.txt", "r")

#POSLAJU SENTIMENT WORDS
PosLaju_positive = open("question-2/Sentiment/Positive Words PosLaju.txt", "r")
PosLaju_negative = open("question-2/Sentiment/Negative Words PosLaju.txt", "r")
PosLaju_neutral = open("question-2/Sentiment/Neutral Words PosLaju.txt", "r")

try:
    #creating a list of those words
    DHL_positive_words = DHL_positive.read().split('\n')
    DHL_negative_words = DHL_negative.read().split('\n')
    DHL_neutral_words = DHL_neutral.read().split('\n')

    GDex_positive_words = GDex_positive.read().split('\n')
    GDex_negative_words = GDex_negative.read().split('\n')
    GDex_neutral_words = GDex_neutral.read().split('\n')

    JNT_positive_words = JNT_positive.read().split('\n')
    JNT_negative_words = JNT_negative.read().split('\n')
    JNT_neutral_words = JNT_neutral.read().split('\n')

    NinjaVan_positive_words = NinjaVan_positive.read().split('\n')
    NinjaVan_negative_words = NinjaVan_negative.read().split('\n')
    NinjaVan_neutral_words = NinjaVan_neutral.read().split('\n')

    PosLaju_positive_words = PosLaju_positive.read().split('\n')
    PosLaju_negative_words = PosLaju_negative.read().split('\n')
    PosLaju_neutral = PosLaju_neutral.read().split('\n')

finally:
    #closing resources opened to read from the files
    DHL_positive.close()
    DHL_negative.close()
    DHL_neutral.close()

    GDex_positive.close()
    GDex_negative.close()
    GDex_neutral.close()

    JNT_positive.close()
    JNT_negative.close()
    JNT_neutral.close()

    NinjaVan_positive.close()
    NinjaVan_negative.close()
    NinjaVan_neutral.close()

    PosLaju_positive.close()
    PosLaju_negative.close()
    PosLaju_neutral.close()

sentiment_table = {'courier': ['DHL', 'GDex', 'JNT', 'NinjaVan', 'PosLaju'],  #these are just dummy data, need to replace with actual ones which we webscrapped
            'positive': [len(DHL_positive_words), len(GDex_positive_words), len(JNT_positive_words), len(NinjaVan_positive_words), len(PosLaju_positive_words)],    # first numbers refer to the total number of sentiment words for first courier and so on
            'negative': [len(DHL_negative_words), len(GDex_negative_words), len(JNT_negative_words), len(NinjaVan_negative_words), len(PosLaju_negative_words)], 
            }

def plot_sentiment_graph(sentiment_table):

    # plotting the graph 
    fig = px.bar(sentiment_table, title='Positive & Negative Sentiment Graph', x="courier", y=["positive", "negative"])
    
    # display the graph in file.html
    plot(fig, False, "", True, filename="question-2/sentiment-graph.html")  

# plot_sentiment_graph(sentiment_table)

print(len(DHL_negative_words))
print(len(DHL_neutral_words))