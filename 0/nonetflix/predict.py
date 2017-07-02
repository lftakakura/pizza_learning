import sys
from enum import Enum
from sklearn import tree
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.multiclass import OneVsRestClassifier
import numpy as np
import pandas as pd


class Category(Enum):
    Acao = 1
    Documentario = 2
    Romance = 3
    Drama = 4
    Terror = 5
    Comedia = 6
    Suspense = 7

DATA_FILE = 'test.csv'

data = pd.read_csv(DATA_FILE, sep=',')

# shuffle data
data = data.sample(frac=1)
data = data.applymap(str)

data_unique = data.drop_duplicates(subset=['description'])

print(data.shape)

descriptions = data.sort_values(['description', 'category']).drop_duplicates(subset=['description']).iloc[:, 1]
categories_dict = data.sort_values(['description', 'category']).groupby('description', sort=False).category.apply(','.join)
categories = list()

for categ in categories_dict:
    categ = categ.split(',')
    categories.append(categ)

# train_data, test_data = data.iloc[:2700, :], data.iloc[2700:, :]

# train data
df = data

features = list(descriptions)
labels = MultiLabelBinarizer().fit_transform(categories)

count_vect = CountVectorizer()
X_news_counts = count_vect.fit_transform(features)

tfidf_transformer = TfidfTransformer()
X_news_tfidf = tfidf_transformer.fit_transform(X_news_counts)

print(X_news_tfidf)
print(labels)

clf = MultinomialNB().fit(X_news_tfidf, labels)

# # test data
# df = pd.read_csv(test_data, header=None)
#
# features = list(df.iloc[:, 1] + '\n' + df.iloc[:, 2])
# labels = list(df.iloc[:, 0])

while True:
    print('Write some text: ')
    text = input()

    X_news_counts = count_vect.transform([text])
    X_news_tfidf = tfidf_transformer.transform(X_news_counts)

    predicted = clf.predict(X_news_tfidf)

    print(predicted)
    # print(Category(predicted).name)

#
# for text, category in zip(features[:1], predicted):
#     print('%r => %s' % (text, Category(category).name))



# print(TextType(labels[0]).name)
# print(features[0])
