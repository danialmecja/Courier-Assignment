# Importing packages
import requests
import string
from bs4 import BeautifulSoup




def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux


# Request the url using python request library
# and save the page inside a variable
URL = "https://www.thestar.com.my/news/nation/2020/09/08/pos-malaysias-sendparcel-to-hit-record-breaking-two-million-parcels-monthly"
page = requests.get(URL)

# Using beautiful soup library
# We parse the content of the page using the html5lib
soup = BeautifulSoup(page.content, 'html5lib')

# Inside the parsed content of the page we find the section of the page with specific element,id or class
# and save it inside a variable
tags = soup.find(id="story-body")

# Next we parse the saved section to only accept text and delete all html markup
article = tags.text

# Removing Punctionations off the article/string/text
article = article.lower()
words = article.split()
# added some more punctionation not added in the string library
punctuation = str(string.punctuation + "”" + "“" + "’" + "–")
# filter the list by the punctuation
table = str.maketrans("", "", punctuation)
stripped = [w.translate(table) for w in words]
# filter empty list ''
word_list = list(filter(None, stripped))


# Counting the frequencies and sort them of of word-frequency pairs by descending frequency.
dictionary = wordListToFreqDict(word_list)
word_freq_list = sortFreqDict(dictionary)
# for s in word_freq_list: print(str(s))





















