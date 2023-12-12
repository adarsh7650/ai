import pandas as pd 
from sklearn.svm    import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv("Iris.csv")

X= data.drop('Target' , axis=1)
Y = data['Target']

xtrain , xtest , ytrain , ytest = train_test_split( X , Y , random_state=42 , test_size=0.2)

s = SVC(kernel='linear')

s.fit(xtrain , ytrain)

pred = s.predict(xtest)

acc = accuracy_score(ytest , pred)

print("Accuracy is ", acc)