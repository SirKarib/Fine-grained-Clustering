import csv
import string
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import zipfile
import pymorphy2


with open('export_file.csv', encoding="UTF-8", newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)
