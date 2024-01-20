import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('obl2.csv')

data['amount'] = data['amount'].replace('(\,...zł)', '', regex=True)
data['amount'] = data['amount'].replace('\s+', '', regex=True)
data['amount'] = data['amount'].astype(int)
data['date'] = pd.to_datetime(data['date'])


# Create random data with numpy, and plot it with matplotlib:
rnstate = np.random.RandomState(1)
y = data['amount']
x = data['date']
plt.scatter(x, y)
plt.show()
# Create a linear regression model based the positioning of the data and Intercept, and predict a Best Fit:
model = LinearRegression()
model.fit(x[:, np.newaxis], y)
xfit = np.linspace(0, 10, 1000)
yfit = model.predict(xfit[:, np.newaxis])
# Plot the estimated linear regression line with matplotlib:
plt.scatter(x, y)
plt.plot(xfit, yfit)
plt.show()
