import string
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import zipfile
import pymorphy2
f = open('review.txt', "r", encoding="utf8")
text = f.read()
f.close()
morph = pymorphy2.MorphAnalyzer()
text = text.lower()
string.punctuation  # переведём символы в единый регистр
spec_chars = string.punctuation + '\n\xa0«»\t—…'  # Набор специальных символов, которые будут удалены из текста
text = "".join([ch for ch in text if ch not in spec_chars])  # Для удаления символов используем поэлементную обработку строки
                                                             # разделим исходную строку text на символы, оставим только символы,
                                                             # не входящие в набор spec_chars и снова объединим список символов в строку
text_tokens = word_tokenize(text)   # text_tokens представляет собой список слов (токенов)
print(text_tokens, type(text_tokens), len(text_tokens))

text = nltk.Text(text_tokens)  # Для применения инструментов частотного анализа библиотеки NLTK необходимо список токенов преобразовать к классу Text

print(type(text))

russian_stopwords = stopwords.words("russian")  # Получим список стоп-слов для русского языка
russian_stopwords.extend(['это', 'и', 'нем'])
text_tokens = [token.strip() for token in text_tokens if token not in russian_stopwords]

print(text_tokens, type(text_tokens), len(text_tokens))

bag = list()

for text_token in text_tokens:
    p = morph.parse(text_token)[0]
    bag.append(p.normal_form)
print(bag)


with open('edit_review.txt', 'w') as filehandle:
    filehandle.writelines("%s   " % place for place in bag)




