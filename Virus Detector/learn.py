import pandas as pd 
import numpy as np
import pickle
import sklearn.ensemble as ensem
from sklearn.feature_selection import SelectFromModel
from sklearn import cross_validation, tree
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib

data = pd.read_csv('data.csv', sep='|')
X = data.drop(['Name', 'md5', 'legitimate'], axis=1).values
Y = data['legitimate'].values

# Selecting important Features using Tree Classifier
fsel = ensem.ExtraTreesClassifier().fit(X,Y)
X_new = SelectFromModel(fsel,prefit=True).transform(X)
features_new = X_new.shape[1]

X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X_new,Y,test_size=0.2)

# Correcting the ordering of features_new
features = []
for f in sorted(np.argsort(fsel.feature_importances_)[::-1][:features_new]):
	features.append(data.columns[2+f])

# Choosing the best algorithm
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
	clf.fit(X_train,Y_train)
	score = clf.score(X_test,Y_test)
	results[algo]=score

best_algo = max(results, key=results.get)
print results[best_algo]
# Saving the algorithm and feature list for future use
joblib.dump(algos[best_algo], 'classifier/classifier.pkl')
open('classifier/features.pkl','w').write(pickle.dumps(features))

print '...........Learning Completed..........'
