import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("data/Student_Performance.csv")
print(df.head())
print(df.shape)
print(df.isnull().sum())
print(df.dtypes)
print(df.describe())
df.hist(figsize=(10,8))
plt.show()
numeric_df = df.select_dtypes(include=['number'])
sns.heatmap(numeric_df.corr(),annot=True)
plt.show()
print(df.columns)
df['Extracurricular Activities'] = df['Extracurricular Activities'].map({'Yes': 1,'No': 0})
X = df.drop('Performance Index', axis=1)
y = df['Performance Index']
print(X.head())
print(y.head())
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print(X_train.shape)
print(X_test.shape)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_pred[:5])

from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
print("R2 Score =", r2)
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
print("MSE =", mse)

rmse = np.sqrt(mse)
print("RMSE =", rmse)
sample_data = [[7, 85, 1, 7, 5]]
prediction = model.predict(sample_data)
print("Predicted Performance =", prediction)
import pickle
pickle.dump(model, open("model.pkl", "wb"))
print("Model Saved Successfully")
loaded_model = pickle.load(open("model.pkl", "rb"))

result = loaded_model.predict([[7, 85, 1, 7, 5]])

print("Loaded Model Prediction =", result)