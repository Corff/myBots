import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/backLegSensorValues.npy")

plt.plot(backLegSensorValues,linewidth=2)
plt.legend()
plt.show()
plt.plot(frontLegSensorValues,linewidth=2)
plt.legend()
plt.show()