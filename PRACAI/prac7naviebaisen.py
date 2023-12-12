import pandas as pd 

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv("data.csv")

#one hot 
encoder = OneHotEncoder()

x = encoder.fit_transform(data.drop('result', axis=1)).toarray()

y = data['result']

xtrain , xtest , ytrain , ytest = train_test_split(x, y , test_size=0.4)

g = GaussianNB()

g.fit(xtrain, ytrain)

pred = g.predict(xtest)

acc = accuracy_score(ytest, pred)

print("acc : ", acc)
print("ytest : ", ytest)
print("pred : ", pred)
