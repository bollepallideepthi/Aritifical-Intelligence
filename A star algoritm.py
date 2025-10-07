# Simple Decision Tree Example in Python

from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier, export_text


iris = datasets.load_iris()

X = iris.data
y = iris.target

model = DecisionTreeClassifier(criterion='entropy', random_state=0)

model.fit(X, y)

tree_rules = export_text(model, feature_names=iris.feature_names)
print("Decision Tree Rules:\n")
print(tree_rules)

sample = [[5.0, 3.4, 1.5, 0.2]]
prediction = model.predict(sample)
print("\nPredicted class for sample", sample, "is:", iris.target_names[prediction][0])
