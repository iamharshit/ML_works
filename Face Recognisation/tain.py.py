from sklearn.datasets import fetch_lfw_people
from sklearn.cross_validation  import train_test_split
from sklearn.decomposition import RandomizedPCA
from sklearn.grid_search import  GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import pylab as pl

# Downloading the data
lfw_people = fetch_lfw_people(min_faces_per_person=70)
X = lfw_people.data
n_samples, height, width = lfw_people.images.shape
n_features = X.shape[1]
Y = lfw_people.target
n_classes = lfw_people.target_names.shape[0]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# Reducing the No. of features
pca = RandomizedPCA(n_components=150, whiten=True).fit(X_train)
eigenfaces = pca.n_components_.reshape((150, height, width) )
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

# Training SVM classifier
para = {
         'C': [1e3, 5e3, 1e4, 5e4, 1e5],
          'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1],
  	}
clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), para).fit(X_test_pca, Y_train)

# Testing clf on test set
Y_pred = clf.predict(X_test_pca)
acc = confusion_matrix(Y_test, Y_pred, labels=range(n_classes))

# Plotting the predictions on a portion of test set

def title(i):
	pred_name = target_names[Y_pred[i]].rsplit(' ')[-1]
	true_name = target_names[Y_pred[i]].rsplit(' ')[-1]
	return 'predicted: %s\ntrue: %s' % (pred_name, true_name)	

def plot_gallery(images, prediction_titles, n_row=3, n_col=4):
	pl.figure(figsize=(1.8*n_col, 2.4*n_row) )
	pl.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)
	for i in range(n_row*n_col):
		pl.subplot(n_row, n_col, i+1)
		pl.imshow(images[i], cmap=pl.cm.gray)
		pl.title(prediction_titles[i], size=12)
		pl.x_ticks(())
		pl.y_ticks(())
	pl.show()

prediction_titles = [title(i) for i in range(Y_pred.shape[0])]

plot_gallery(X_test_pca, prediction_titles)