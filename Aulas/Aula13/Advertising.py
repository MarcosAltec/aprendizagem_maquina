import pandas as pd
import numpy as np
# from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("Advertising.csv")

X = df[['TV', 'radio', 'newspaper']]
y = df['sales']

kf = KFold(n_splits = 5, shuffle=True, random_state=42)

rmse_list = []

for train_index, test_index in kf.split(X, y):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = X.iloc[train_index], y.iloc[test_index]

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_train)

    print(f"Tamanho de y_test: {len(y_test)}")
    print(f"Tamanho de y_pred: {len(y_pred)}")

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    rmse_list.append(rmse)

rmse_mean = np.mean(rmse_list)

print(f"(RMSE) medio após K-Fold: {rmse_mean: .2f}")

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) 

# model = LinearRegression()
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# print(f"Root Mean Square Error (RMSE): {rmse: .2f}")