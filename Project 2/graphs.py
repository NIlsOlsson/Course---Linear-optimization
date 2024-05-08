import matplotlib.pyplot as plt

# Solve times for large data
T_int = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
times_int = [0.0200, 0.0530, 0.0460, 0.194, 0.453, 5.05, 4.73, 5.07, 24.8, 34.4, 178.5, 126.6, 460.3, 498.3, 1631.4, 2720.5]

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