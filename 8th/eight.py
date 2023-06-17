from sklearn.datasets import load_breast_cancer
import pandas as pd

from sklearn.model_selection import train_test_split as tts
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.metrics import accuracy_score as acc_sc

data = load_breast_cancer(as_frame=True)
X = data.data
y = data.target

X_train, X_test, y_train, y_test = tts(X, y, test_size=0.3, random_state=42)

dtc = DTC(max_depth=3)

dtc.fit(X_train, y_train)
y_pred = dtc.predict(X_test)

accuracy = acc_sc(y_test, y_pred)
print("Accuracy: %.3g%%" % (accuracy * 100)) ## Accuracy: 95.9%