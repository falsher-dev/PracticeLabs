import pandas as pd

from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as LR
import joblib

data = pd.read_csv('sales.csv')
train_data, test_data = tts(data, test_size=0.3, random_state=42)

model = LR()

X_train = train_data.drop(["Sales"], axis=1)
Y_train = train_data["Sales"]
model.fit(X_train, Y_train)

X_test = test_data.drop(["Sales"], axis=1)
Y_test = test_data["Sales"]

score = model.score(X_test, Y_test)

joblib.dump(model,'sales.joblib')

new_data = pd.read_csv('sales_new.csv')

new_model = LR()
new_model = joblib.load('sales.joblib')

X_new = new_data.drop(['Sales'], axis=1)
y_pred = new_model.predict(X_new)

new_data['Sales'] = y_pred
new_data.to_csv("salex_export.csv", index=False)

print("Accuracy: %.3g%%" % (score * 100)) ## Accuracy: 95.6%