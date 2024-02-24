from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

X, y = make_classification(
  n_features=6,
  n_classes=3,
  n_samples=800,
  n_informative=2,
  random_state=1,
  n_clusters_per_class=1
)

plt.scatter(X[:, 0], X[:, 1], c=y, marker="*")
plt.show()