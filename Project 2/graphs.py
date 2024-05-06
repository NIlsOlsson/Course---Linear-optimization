import matplotlib.pyplot as plt
import numpy as np

# Solve times for large data
T = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
times = [0.0200, 0.0530, 0.0460, 0.194, 0.453, 5.05, 4.73, 5.07, 24.8, 34.4, 178.5, 126.6, 460.3, 498.3, 1631.4, 2720.5]

plt.figure()
plt.plot(T, np.log(times))
plt.show()