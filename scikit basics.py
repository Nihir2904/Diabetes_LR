import sklearn
from sklearn import tree
features = [[2, 100], [3,50], [5,200], [4, 500], [7, 800]]
label = [1,2,1,2,2]
cld = tree.DecisionTreeClassifier()
cld = cld.fit(features, label)
print(cld.predict([[3, 50]]))
