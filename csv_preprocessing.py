import csv
import string

from nltk import word_tokenize
from nltk.corpus import stopwords
import pymorphy2

with open('export_file.csv', encoding="UTF-8", newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)
