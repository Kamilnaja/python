import math
import numpy as np
from d2l import tensorflow as d2l
from matplotlib import pyplot as plt

def normal(x, mu, sigma):
  # mu - średnia
  # sigma - odchylenie standardowe
  p = 1/ math.sqrt(2 * math.pi * sigma ** 2)
  return p * np.exp(-0.5 * (x - mu) ** 2 / sigma ** 2)

x = np.arange(-7, 7, 0.01)
params = [(0, 1), (0, 2), (3, 1)]

d2l.plot(x, [normal(x, mu, sigma) for mu, sigma in params], xlabel='x',
         ylabel='p(x)', figsize=(4.5, 2.5),
         legend=[f'mean {mu}, std {sigma}' for mu, sigma in params])

plt.show()