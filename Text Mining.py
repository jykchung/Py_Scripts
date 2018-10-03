# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 13:40:00 2018

@author: Jack Chung
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from pandas import plotting
from scipy import stats

import PyPDF2 # PyPDF2 is installed from Anaconda Command Windo using "pip install PyPDF2"
import textract  # Cannot install into Windows 10, lots of ppl have problems ding it

from wordcloud import WordCloud
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#================================================================
#****************************************************************

# Check pdf properties and see settings to see whether "extraction" is set to allowed
# Cannot just copy and paste text from pdf into notepad and then save as .txt
# Need to use the following code to extract text as binary, and then convert binary 
# to a string object, so it can be further used for WordCloud for example

# Alternatively, need to copy text from pdf and paste into MS Word, then in Word
# save as .txt.  And then apply analysis (i.e. WordClould) to this newly formed string.

import PyPDF2

pdf_file = open('sample.pdf', 'rb') # format should be C:\\Users...\\name.pdf 
read_pdf = PyPDF2.PdfFileReader(pdf_file) # as binary
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
BinaryText = page_content.encode('utf-8')
print(BinaryText)
type(BinaryText)  # type is binary

# Convert binary to string object
Str_Text = BinaryText.decode('ascii')
type(Str_Text)   # should return "str"

# Now, Str_Text can be used for WordCloud generation

#================================================================
#****************************************************************

# WordCloud (pip install wordcloud)
from wordcloud import WordCloud
# Read the .txt file.
text = open('C:\\Users\\user\\Desktop\\TextMiningFiles\\sensorviaword.txt').read()
# Generate a word cloud image from string object "text"
# can simply apply to a text string extracted from pdf using method above
wordcloud = WordCloud(background_color='white').generate(text string object)
# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
_=plt.imshow(wordcloud.recolor(random_state=2017)), plt.title('Most Frequent Words'), plt.axis("off"), plt.show()

#================================================================
#****************************************************************

# Creating document term matrix from corpus of sample documents stored in a folder
# for example there are 5 name.txt files in a folder, the code will generate a dataframe 
# with words as index and name.txt as col names and the elements are frequency of 
# words in each name.txt 

import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
# Function to create a dictionary with key as file names and values as text
# for all files in a given folder
def CorpusFromDir(dir_path):
    result = dict(docs = [open(os.path.join(dir_path,f)).read() for f in
                          os.listdir(dir_path)], ColNames = map(lambda x: x, os.listdir(dir_path)))
    return result

docs = CorpusFromDir('C:\\Users\\user\\Desktop\\TextMiningFiles')
# Initialize
vectorizer = CountVectorizer()
doc_vec = vectorizer.fit_transform(docs.get('docs'))
#create dataFrame
df = pd.DataFrame(doc_vec.toarray().transpose(), index = vectorizer.get_feature_names())
# Change column headers to be file names
df.columns = docs.get('ColNames')
print(df)

#================================================================
#****************************************************************

# PerceptronTagger

# Need to import and download averaged_perceptron_tagger
import nltk
nltk.download('averaged_perceptron_tagger')

# Process the text data
from nltk.tag.perceptron import PerceptronTagger
PT = PerceptronTagger()
print(PT.tag('This is a sample English sentence'.split()))
#----output----
[('This', 'DT'), ('is', 'VBZ'), ('a', 'DT'), ('sample', 'JJ'), ('English', 'JJ'),
('sentence', 'NN')]

# To get help about tags
nltk.help.upenn_tagset('NNP')  # can run this in IPython Console

# Alternatively, use this method involving tokenizer 
import nltk
nltk.download('punkt') # can run this in IPython Console

from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

Percept_list = pos_tag(word_tokenize("John's big idea isn't all that bad."))
# or if you have a string object 
Percept_list = pos_tag(word_tokenize(string object name))

print(Percept_list)

# Now here comes the useful part!!  We can convert the Percept-list to a dataframe 
# object and then analyse to get more information, e.g. find sum of nouns (NN), 
# the count of certain words etc.

df = pd.DataFrame(list)   # e.g.  df_percept = pd.DataFrame(Percept_list)



