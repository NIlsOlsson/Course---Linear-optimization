import matplotlib.pyplot as plt

# Solve times for large data
T_int = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
times_int = [0.511, 0.888, 1.415, 2.648, 3.891, 9.833, 20.230, 64.477, 158.380, 48.967, ]

T_relax = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700]
times_relax = [0.0290, 0.039, 0.069, 0.162, 0.217, 0.329, 0.597, 0.774, 0.976, 0.917, 1.18, 1.32, 1.44, 2.16]

plt.figure()
plt.plot(T_int, times_int)
plt.yscale('log')
plt.title('Model 1 with binary variables')
plt.xlabel('T')
plt.ylabel('solve time (s)')
plt.show()

plt.figure()
plt.plot(T_relax, times_relax)
plt.yscale('log')
plt.title('Model 1 with relaxed variables')
plt.xlabel('T')
plt.ylabel('solve time (s)')
plt.show()