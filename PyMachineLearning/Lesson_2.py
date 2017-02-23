import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()

test_idx = [0, 50, 100]

#training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

#classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data, train_target)

print (test_target)
print (clf.predict(test_data))
print (test_target == clf.predict(test_data))

from sklearn.externals.six import StringIO
import pydotplus

dot_data = StringIO()
tree.export_graphviz(clf,
                        out_file = dot_data,
                        feature_names = iris.feature_names,
                        class_names = iris.target_names,
                        filled = True, rounded = True,
                        impurity = False)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris_viz.pdf")
