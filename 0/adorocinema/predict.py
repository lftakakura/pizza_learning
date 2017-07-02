import sys
from enum import Enum
from sklearn import tree
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.multiclass import OneVsRestClassifier
import numpy as np
import pandas as pd
import pickle


class Category(Enum):
    Outros = 0
    Acao = 1
    Animacao = 2
    Aventura = 3
    Biografia = 4
    Comedia = 5
    Comedia_dramatica = 6
    Drama = 7
    Documentario = 8
    Familia = 9
    Fantasia = 10
    Ficcao_cientifica = 11
    Guerra = 12
    Policial = 13
    Romance = 14
    Terror = 15

DATA_FILE = 'movies_test.csv'

data = pd.read_csv(DATA_FILE, sep=',')

# shuffle data
data = data.sample(frac=1)
data = data.applymap(str)

# data = data.drop_duplicates(subset=['description'])

# print(data.shape)
# print(data)

features = data.iloc[:, 3]
labels = data.iloc[:, 0]

# print(descriptions)
# print(categories)

# for categ in categories_dict:
#     categ = categ.split(',')
#     categories.append(categ)

# train_data, test_data = data.iloc[:2700, :], data.iloc[2700:, :]

# train data
df = data

# features = list()
# labels = list(['13', '7', '10'])

print(features)
print(labels)

count_vect = CountVectorizer()
X_counts = count_vect.fit_transform(features)

tfidf_transformer = TfidfTransformer()
X_tfidf = tfidf_transformer.fit_transform(X_counts)

print(X_tfidf)
print(labels)

clf = pickle.load(open('model.pkl', 'rb'))
# clf = MultinomialNB(alpha=0.01).fit(X_tfidf, labels)
# clf = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=5, random_state=42).fit(X_tfidf, labels)
pickle.dump(clf, open('model.pkl', 'wb'))


# # test data
# df = pd.read_csv(test_data, header=None)
#
# features = list(df.iloc[:, 1] + '\n' + df.iloc[:, 2])
# labels = list(df.iloc[:, 0])

while True:
    print('Escreva uma descrição de um filme: ')
    text = input()

    X_counts = count_vect.transform([text])
    X_tfidf = tfidf_transformer.transform(X_counts)

    predicted = clf.predict(X_tfidf)
    predicted_proba = clf.predict_proba(X_tfidf)

    print(predicted)
    # print(predicted_proba)
    print('------------------------------')
    print('O gênero deste filme é %s' % Category(int(predicted[0])).name)
    print('------------------------------')

#
# for text, category in zip(features[:1], predicted):
#     print('%r => %s' % (text, Category(category).name))



# print(TextType(labels[0]).name)
# print(features[0])
