from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()

clf.fit(X_train, y_train)

predictions = clf.predict(X_test)

from sklearn.metrics import accuracy_score
print (accuracy_score(y_test, predictions))
