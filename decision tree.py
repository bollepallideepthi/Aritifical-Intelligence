from sklearn import tree

X = [[180, 80], [170, 70], [160, 60], [155, 45], [165, 55]]

Y = [1, 1, 1, 0, 0]


model = tree.DecisionTreeClassifier()
model = model.fit(X, Y)

pred = model.predict([[172, 65]])

print("Predicted Class:", "Male" if pred[0] == 1 else "Female")
