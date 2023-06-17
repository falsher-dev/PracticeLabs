from sklearn.datasets import load_breast_cancer
import pandas as pd

from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import StandardScaler as SS
from sklearn.linear_model import LogisticRegression as LR
from sklearn.metrics import accuracy_score as acc_sc

data = load_breast_cancer(as_frame=True)
X = data.data
y = data.target
X_train, X_test, y_train, y_test = tts(X, y, test_size=0.2, random_state=42)
X_train, X_val, y_train, y_val = tts(X_train, y_train, test_size=0.1, random_state=42)

scaler = SS()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

lr = LR(multi_class='ovr') ## созд модели

lr.fit(X_train, y_train) ## обучение модели
y_pred = lr.predict(X_test) ## предсказания

accuracy = acc_sc(y_test, y_pred)
print("Accuracy: %.3g%%" % (accuracy * 100)) ## Accuracy: 97.4%