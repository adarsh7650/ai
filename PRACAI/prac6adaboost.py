import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

col_names = ['Reservation', 'Raining', 'Bad Service', 'Saturday', 'Result']
feature_cols =  ['Reservation', 'Raining', 'Bad Service', 'Saturday']

hoteldata = pd.read_csv("dtree.csv", names=col_names)

X= hoteldata[feature_cols]
Y= hoteldata.Result


x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

a = AdaBoostClassifier(n_estimators=6, learning_rate=2)
a.fit(x_train, y_train)

y_pred = a.predict(x_test)

acc = accuracy_score(y_test , y_pred)


print(f"y_test=\n{y_test}  \ny_pred= {y_pred}")
print(f"Accuracy:", acc)


"""OUTPUT:-
   y_test=
   6     leave
   3      wait
   13    leave
   2     leave
   14    leave
   7      wait
   Name: Result, dtype: object
   y_pred= ['leave' 'leave' 'leave' 'leave' 'leave' 'wait']
   Accuracy: 0.8333333333333334
"""
