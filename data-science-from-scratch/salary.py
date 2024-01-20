import matplotlib.pyplot as plt

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5), (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

salaries = [salary for salary, tenure in salaries_and_tenures]
tenures = [tenure for salary, tenure in salaries_and_tenures]
plt.xlabel("Years Experience")
plt.ylabel("Salary")
plt.ylim(40_000, 100_000)
plt.scatter(tenures, salaries)
plt.show()
