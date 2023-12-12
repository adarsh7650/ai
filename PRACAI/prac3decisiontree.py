import pandas as pd 
from sklearn.tree import DecisionTreeClassifier  , plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

data = pd.read_csv("Iris.csv")

X= data.drop('Target', axis=1)
Y = data['Target']

xtrain , xtest , ytrain , ytest = train_test_split(X  , Y , random_state=42 , test_size=0.2)

clf = DecisionTreeClassifier()

clf.fit(xtrain,ytrain)

pred = clf.predict(xtest)

acc = accuracy_score(ytest , pred)

print("accuracy , ", acc)

#plotting tree
plt.figure(figsize=(12,8))
plot_tree(clf , filled=True , feature_names=X.columns , class_names=Y.unique().astype(str))
plt.title("Decision Tree Classifier")
plt.show()
