# Sets
Components = 1:2 # 2 components

# Parameters
T = 4     #number of timesteps
I = [(s, t) for s in 0:T for t in (s + 1):(T + 1)] # time intervals
d = [10 10 1 10]      #cost of a maintenance occasion
c =   [1 1   2   1;
       1 100 100 1]     #costs of new components
U = [3 4]     #lives of new components
