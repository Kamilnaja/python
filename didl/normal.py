import math
import numpy as np


def normal(x, mu, sigma):
  p = 1/ math.sqrt(2 * math.pi * sigma ** 2)
  return p * np.exp(-0.5 * (x - mu) ** 2 / sigma ** 2)