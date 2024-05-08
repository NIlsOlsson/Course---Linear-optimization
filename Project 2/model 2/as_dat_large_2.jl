# Sets
Components = 1:10 # 10 components

# Parameters
T = 80    #number of timesteps
I = [(s, t) for s in 0:T for t in (s + 1):(T + 1)] # time intervals
d = ones(1,T)*20      #cost of a maintenance occasion
c = [begin
        matrix = fill(r, T+1, T+1)  # Create a T x T matrix filled with the value r
        padded_matrix = zeros(T + 2, T + 2)  # Create a larger matrix with padding
        padded_matrix[1:(T+1), 1:(T+1)] = matrix  # Copy the smaller matrix into the center of the padded matrix
        padded_matrix
    end
    for r in [34 25 14 21 16  3 10  5  7 10]]
U = [42 18 90 94 49 49 34 90 37 11]     #lives of new components

print(I[418])
#print(c[2][1,19])