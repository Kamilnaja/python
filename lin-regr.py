import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import pandas as pd


def generate_correlated_data(num_points, mean_correlation):
    # Generowanie dwóch zestawów danych losowych
    data1 = np.random.rand(num_points)
    data2 = np.random.rand(num_points)

    # Obliczanie korelacji między danymi
    actual_correlation = np.corrcoef(data1, data2)[0, 1]

    # Korekta korelacji do zadanej średniej
    correlation_correction = mean_correlation - actual_correlation
    data2 = data2 + correlation_correction * data1

    return data1, data2


def plot_scatter_with_correlation(data1, data2):
    plt.scatter(data1, data2)
    plt.title('Zbiór punktów z korelacją')
    plt.xlabel('Dane 1')
    plt.ylabel('Dane 2')
    plt.grid(True)
    plt.show()


# Ustawienia
num_points = 100
mean_correlation = 1.6

# Generowanie danych
data1, data2 = generate_correlated_data(num_points, mean_correlation)

# wizualizacja danych w sns
numpy_array = np.array([data1, data2])
# data = np.array([1, 2, 3, 4])
data = pd.DataFrame(numpy_array)
# sns.scatterplot(x='X', y='Y', data=data)
plt.show()
# sns.lmplot(x='data1', y='data2', data=data, fit_reg=True)

# sns.lmplot(x='data1', y='data2', data=data1[0], fit_reg=True)
# print(data1)
# print(data2)
# sns.lmplot(x='data1', y='data2', data=data1, fit_reg=True)
