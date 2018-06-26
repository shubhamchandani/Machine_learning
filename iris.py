#!usr/bin/pyhton3
from sklearn.datasets import load_iris
from sklearn import  tree
from  sklearn.model_selection  import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sb
iris = load_iris()
train_iris,test_iris,train_target,test_target = train_test_split(iris.data,iris.target,test_size=0.9)
clf=tree.DecisionTreeClassifier()
trained = clf.fit(train_iris,train_target)
output = trained.predict(test_iris)
print (output)
print (test_target)
score = accuracy_score(test_target,output)
print (score)
plt.plot(test_target)
plt.show()

