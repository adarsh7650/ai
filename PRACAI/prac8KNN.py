import pandas as pd 

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv("Iris.csv")

x = data.drop('Target', axis=1)
y = data['Target']

xtrain , xtest , ytrain , ytest = train_test_split(x , y , test_size=0.3 , random_state=42)

k = KNeighborsClassifier(3)

k.fit(xtrain , ytrain)

pred = k.predict(xtest)

acc = accuracy_score(ytest , pred)

print("Accuracy : ", acc)