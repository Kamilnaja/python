import matplotlib.pyplot as plt
# year = [2015, 2016, 2017, 2018, 2019, 2020, 1999]
# pop = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
# year.sort()
# plt.plot(year, pop)
# plt.show()


values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
plt.hist(values, bins=3)
plt.show()
