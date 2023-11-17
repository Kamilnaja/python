import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf

data = pd.read_csv('obl2.csv', index_col=0, parse_dates=['date'])
data['amount'] = data['amount'].replace('(\,...zł)', '', regex=True)
data['amount'] = data['amount'].replace('\s+', '', regex=True)
print(data.tail())
