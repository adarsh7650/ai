from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pandas as pd 

dataset = [
    ['milk' ,'bread' , 'nuts'],
    ['milk' ,'bread'],
    ['milk','eggs', 'nuts'],
    ['milk', 'bread' ,'eggs'],
    ['bread' , 'nuts']
]

dataframe = pd.DataFrame(dataset) #convert the dataset to dataframe

#converts items to columns
dataframe_encoded = pd.get_dummies(dataframe , prefix='', prefix_sep='')

#find the frequent itemsets
frequent_itemsets = apriori(dataframe_encoded , min_support=0.5 , use_colnames=True)
print("Frequent itemsets : ,", frequent_itemsets)

#generates association rules 
rules = association_rules(frequent_itemsets , metric="lift" ,min_threshold=1.0)
print ( "\n Association rules : ")
print(rules)



