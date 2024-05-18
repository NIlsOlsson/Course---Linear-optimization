import matplotlib.pyplot as plt

# Solve times for large data
T_int = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
times_int = [0.0660, 0.231, 0.172, 0.597, 1.431, 0.821, 4.902, 3.713, 32.608, 7.758, 152.647, 90.437, 502.479, 444.187, 1732.893, 2093.696]

T_relax = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700]
times_relax = [0.039, 0.465, 1.520, 4.382, 9.160, 13.886, 25.0, 28.872, 47.428, 58.362, 73.008, 96.767, 127.777, 143.861]

plt.figure()
plt.plot(T_int, times_int)
plt.yscale('log')
plt.title('Model 2 with binary variables')
plt.xlabel('T')
plt.ylabel('solve time (s)')
plt.show()

plt.figure()
plt.plot(T_relax, times_relax)
plt.yscale('log')
plt.title('Model 2 with relaxed variables')
plt.xlabel('T')
plt.ylabel('solve time (s)')
plt.show()