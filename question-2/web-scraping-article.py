# Importing packages
import requests
import string
from bs4 import BeautifulSoup

# Importing Trie
from trie import Trie

# Importing Stop Words
#stopW = open("question-2\stopwords.txt", "r")
# Importing Stop Words - MacOS
stopW = open("question-2/stopwords.txt", "r")
try:
    content = stopW.read()
    stop_words = content.split(",")
finally:
    stopW.close()

#  Importing Positive Words - MacOS
positive_words = open("question-2/positivewords.txt").read().splitlines()

# Importing Negative Words - MacOS
negative_words = open("question-2/negativewords.txt").read().splitlines()


# Functions for counting the word frequency as well as sorting them
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))
def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux


companies = ["DHL","PosLaju","NinjaVan","JNT","GDex"]

urls_DHL = ["https://www.thestar.com.my/aseanplus/aseanplus-news/2021/05/17/dhl-express-dedicates-direct-flights-to-penang-and-vietnam039s-ho-chi-minh-city",
            "https://www.theedgemarkets.com/article/tech-digitalisation-way-forward-dhl-express",
            "https://www.suasnews.com/2020/12/dhl-express-malaysia-partners-aerodyne-group-on-drone-delivery-services/"]

urls_PosLaju = ["https://www.thestar.com.my/news/nation/2020/09/08/pos-malaysias-sendparcel-to-hit-record-breaking-two-million-parcels-monthly",
                "https://www.thestar.com.my/news/nation/2018/11/14/wild-animals-for-sale-via-mail-unusual-but-not-new",
                "https://www.thestar.com.my/opinion/letters/2019/04/17/delivery-by---poslaju-needs-to-be-improved/"]

urls_NinjaVan = ["https://www.theedgemarkets.com/article/ninja-van-capitalising-opportunities-presented-pandemic",
                 "https://themalaysianreserve.com/2020/10/26/ninja-van-malaysia-sees-shift-in-demand-as-e-commerce-grows/",
                 "https://www.theedgemarkets.com/article/ninja-van-use-funds-raised-boost-malaysian-ops"]

urls_JNT = ["https://www.thestar.com.my/news/nation/2021/02/07/courier-company-says-sorry-over-039violent-sorting-of-packages039",
            "https://www.malaymail.com/news/malaysia/2021/02/07/courier-company-jt-express-explains-staffs-violent-handling-of-parcels-caug/1947791",
            "https://www.therakyatpost.com/2021/02/07/jt-express-protests-whats-going-on-how-to-claim-your-money-back/"]

urls_GDex = ["https://www.theedgemarkets.com/article/gdex-partners-tasco-improve-logistics-delivery-services",
             "https://www.theedgemarkets.com/article/gdex-stands-benefit-pickup-ecommerce-activities-says-kenanga-research",
             "https://www.theedgemarkets.com/article/gdex-look-creating-industrial-reit-part-next-growth-phase"]

def article_sentiment_comparison(positive_word_list, negative_word_list, counter, company):
    
    if(len(positive_word_list) > len(negative_word_list) ):
        print('Article ' + str(counter) + ' of courier ' + company +' is positive!')    
    else:
        print('Article ' + str(counter) + ' of courier ' + company + ' is negative.')

# To analyse the articles of courier companies in Malaysia
# Printing its 
def article_analysis(company):
    
    counter = 0
    if(company == "DHL"):
        urls = urls_DHL
    elif(company == "PosLaju"):
        urls = urls_PosLaju
    elif(company == "NinjaVan"):
        urls = urls_NinjaVan
    elif(company == "JNT"):
        urls = urls_JNT
    elif(company == "GDex"):
        urls = urls_GDex   

    for url in urls:
        # Request the url using python request library
        # and save the page inside a variable
        URL = url
        page = requests.get(URL)
        url_check = url.split("/")
        url_uses_class = False

        # Using beautiful soup library
        # We parse the content of the page using the html5lib
        soup = BeautifulSoup(page.content, 'html5lib')

        # Inside the parsed content of the page we find the section of the page with specific element,id or class
        # and save it inside a variable
        if ("www.thestar.com.my" in url_check):
            tags = soup.find(id="story-body")
        elif("www.theedgemarkets.com" in url_check):
            tags = ""
            url_uses_class = True
            for div in soup.find_all('div', class_='field-item'):
                for p in div.find_all('p'):
                    tags += p.text
        elif("www.suasnews.com" in url_check):
            tags = ""
            url_uses_class = True
            for div in soup.find_all('div', class_='tdb-block-inner'):
                for p in div.find_all('p'):
                    tags += p.text
        elif("www.freemalaysiatoday.com" in url_check):
            tags = ""
            url_uses_class = True
            for div in soup.find_all('div', class_='td-post-content'):
                for p in div.find_all('p'):
                    tags += p.text
        elif("themalaysianreserve.com" in url_check):
            tags = ""
            url_uses_class = True
            for div in soup.find_all('section', class_='single-post-content'):
                for p in div.find_all('p'):
                    tags += p.text
        elif("www.therakyatpost.com" in url_check):
            tags = ""
            url_uses_class = True
            for div in soup.find_all('div', class_='post-content'):
                for p in div.find_all('p'):
                    tags += p.text
        elif("www.malaymail.com" in url_check):
            tags = ""
            url_uses_class = True
            for div in soup.find_all('article'):
                for p in div.find_all('p'):
                    tags += p.text

        # Next we parse the saved section to only accept text and delete all html markup
        if(url_uses_class):
            article = tags
        else:
            article = tags.text
        article = article.lower()
        words = article.split()

        # Removing Punctionations off the article/string/text
        # added some more punctionation not added in the string library
        punctuation = str(string.punctuation + "”" + "“" + "’" + "–" + "—")
        # filter the list by the punctuation
        table = str.maketrans("", "", punctuation)
        stripped = [w.translate(table) for w in words]
        # filter empty list ''
        word_list = list(filter(None, stripped))

        # Removing Stop words using Trie algorithm
        stopWordTrie = Trie()
        for stop_word in stop_words:
            stopWordTrie.insert(stop_word)
        for word in word_list:
            for word in word_list:
                if stopWordTrie.search(word):
                    word_list.remove(word)

        neutral_word_list = word_list.copy()


        # Filtering The Positive Words using Trie algorithm and storing it in positive_word_list
        positive_word_list = []
        positiveWordTrie = Trie()
        for positive_word in positive_words:
            positiveWordTrie.insert(positive_word)
        for word in word_list:
            if positiveWordTrie.search(word):
                neutral_word_list.remove(word)
                positive_word_list.append(word)


        #  Filtering the Negative Words using Trie algorithm aand storing it in negative_word_list
        negative_word_list = []
        negWordTrie = Trie()
        for negative_word in negative_words:
            negWordTrie.insert(negative_word)
        for word in word_list:
            if negWordTrie.search(word):
                neutral_word_list.remove(word)
                negative_word_list.append(word)
        counter += 1
        
        
        
        #Printing the sentiments in .txt files for positive, neutral, and negative words
        """
        filename_positive = "Positive words "+str(company)+".txt"
        file_positive = open(filename_positive, 'a')
        filename_negative = "Negative words "+str(company)+".txt"
        file_negative = open(filename_negative, 'a')
        filename_neutral = "Neutral words "+str(company)+".txt"
        file_neutral = open(filename_neutral, 'a')

        file_positive.writelines("% s\n" % lines for lines in positive_word_list)
        file_negative.writelines("% s\n" % lines for lines in negative_word_list)
        file_neutral.writelines("% s\n" % lines for lines in neutral_word_list)

        file_positive.close()
        file_negative.close()
        file_neutral.close()
        """

        # Counting the frequencies and sort them of of word-frequency pairs by descending frequency.
        dictionary = wordListToFreqDict(word_list)
        word_freq_list = sortFreqDict(dictionary)
        
        # for s in word_freq_list: print(str(s))
        print("\n\n\n")
        print("------------------------------------------------------------------",end="\n")
        print("Article " + str(counter) + " of " + str(company), end="\n")
        print("The word List: ")
        print(word_list , end="\n \n")
        print("The Frequency Word List: ")
        print(word_freq_list , end="\n \n")
        print("The Positive Word List: ")
        print(positive_word_list , end="\n \n")
        print("The Negative Word List: ")
        print(negative_word_list , end="\n \n")
        print("The Neutral Word List: ")
        print(neutral_word_list , end="\n \n")
        print("------------------------------------------------------------------",end="\n")
        article_sentiment_comparison(positive_word_list, negative_word_list, counter, company)


article_analysis('DHL')

# article_analysis('NinjaVan')
# article_analysis('PosLaju')
# article_analysis('JNT')
# article_analysis('GDex')

article_analysis('GDex')
