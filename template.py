from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import sklearn.ensemble as ensem
from sklearn.feature_selection import SelectFromModel
from sklearn import tree
from sklearn.naive_bayes import GaussianNB

features = np.genfromtxt('features.csv', delimiter=',')[1:]
labels = np.genfromtxt('labels.csv', delimiter=',')[1:]


x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.3)

algos = {
    'DecisionTree': tree.DecisionTreeClassifier(),
    'RandomForest': ensem.RandomForestClassifier(),
    'GradientBoosting': ensem.AdaBoostClassifier(),
    'AdaBoost': ensem.AdaBoostClassifier(),
    'GNB': GaussianNB()
}
results={}
for algo in algos:
    clf = algos[algo]
    clf.fit(x_train,y_train)
    score = clf.score(x_test,y_test)
    results[algo]=score

best_algo = max(results, key=results.get)
print 'accuracy= ',results[best_algo]*100
