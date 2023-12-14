import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv('obl3.csv')

# Separate features (amount) and target (date)
X = df['amount'].to_numpy().reshape(-1, 1)  # Reshape to 2D array for LinearRegression
y = df['date'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = linear_model.LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test.reshape(-1, 1))

print("Coefficients: \n", model.coef_)

print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))


# Plot outputs
plt.scatter(X_test, y_test, color="black")
plt.plot(X_test, y_pred, color="red", linewidth=1)
plt.yticks(())

plt.show()