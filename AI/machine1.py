from sklearn.datasets import  load_iris
import numpy as np
from  sklearn.model_selection import  train_test_split
from  sklearn.tree import  DecisionTreeClassifier
iris_dataset=load_iris()
X_train,X_test,y_train,y_test=train_test_split(iris_dataset.data,iris_dataset.target,random_state=1)
model=DecisionTreeClassifier()
mymodel=model.fit(X_train,y_train)
X_New=np.array([[1.0,3.23,6.5,2.0]])
print(mymodel.predict(X_New))
print(mymodel.score(X_test,y_test))
