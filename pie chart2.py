import matplotlib.pyplot as plt
import numpy as np

y = np.array([25, 55, 25, 25])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=mylabels)
plt.show()