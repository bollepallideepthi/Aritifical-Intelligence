# Feed Forward Neural Network Example

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Load digits dataset
digits = load_digits()

X = digits.data
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = MLPClassifier(hidden_layer_sizes=(10, 5),
                      activation='relu',
                      solver='adam',
                      random_state=1)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)


print("Feed Forward Neural Network Accuracy:", accuracy_score(y_test, y_pred))
