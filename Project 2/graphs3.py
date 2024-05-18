import matplotlib.pyplot as plt

# Solve times for large data
T_int = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
times_int_1 = [0.0200, 0.0530, 0.0460, 0.194, 0.453, 5.05, 4.73, 5.07, 24.8, 34.4, 178.5, 126.6, 460.3, 498.3, 1631.4, 2720.5]
times_int_2 = [0.0660, 0.231, 0.172, 0.597, 1.431, 0.821, 4.902, 3.713, 32.608, 7.758, 152.647, 90.437, 502.479, 444.187, 1732.893, 2093.696]

T_relax = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700]
times_relax_1 = [0.0290, 0.039, 0.069, 0.162, 0.217, 0.329, 0.597, 0.774, 0.976, 0.917, 1.18, 1.32, 1.44, 2.16]
times_relax_2 = [0.039, 0.465, 1.520, 4.382, 9.160, 13.886, 25.0, 28.872, 47.428, 58.362, 73.008, 96.767, 127.777, 143.861]

plt.figure()
plt.plot(T_int, times_int_1, label='Model 1 binary')
plt.plot(T_int, times_int_2, label='Model 2 binary')
plt.plot(T_relax, times_relax_1, label='Model 1 relaxed')
plt.plot(T_relax, times_relax_2, label='Model 2 relaxed')
plt.yscale('log')
plt.xlabel('T')
plt.ylabel('solve time (s)')
plt.legend()
plt.show()

