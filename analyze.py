import numpy as np
import matplotlib.pyplot as plt

x = np.load("data/motorValuesTorso BackLeg.npy")
y = np.load("data/motorValuesTorso FrontLeg.npy")
plt.plot(x)
plt.show()
plt.plot(y)
plt.show()