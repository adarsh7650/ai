import pandas as pd 
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


data = pd.read_csv('dtree.csv')
x= data.drop('Result', axis=1)
y = data['Result']
xtrain , xtest ,ytrain , ytest = train_test_split( x , y , random_state=33 , test_size=0.3)

a = AdaBoostClassifier()

a.fit(xtrain ,ytrain)
pred = a.predict(xtest)
acc = accuracy_score(ytest, pred)


print(" ytest : ", ytest)
print('pred :', pred)
print( " Accucarya : ", acc)