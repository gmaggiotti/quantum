from numpy import array, matmul, round

ket0 = array([1, 0])
ket1 = array([0, 1])
print(ket0/2 + ket1/2)


from math import sqrt

z = 1j
# Hadamard Matrix
H = array([[1 / sqrt(2), 1 / sqrt(2)], [1 / sqrt(2), -1 / sqrt(2)]])

# Phase pi/2 matrix
S = array([[1, 0], [0, z]])

# (HSH)^2 = R^2 = X
SH = matmul(S, H)
R = matmul(H, SH)
print("R: \n", R)

X = matmul(R, R)
# NOT matrix
print("R^2: \n", round(X, 0))

from qiskit.quantum_info import Statevector

u = Statevector([1 / sqrt(2), 1 / sqrt(2)])
v = Statevector([(1 + 2.0j) / 3, -2 / 3])
w = Statevector([1 / 3, 2 / 3])

print("State vectors u, v, and w have been defined.")

from IPython.display import display
display(v.draw("text"))
# check if a given vector is a valid quantum state
print("w is valid state:", w.is_valid())


# Simulating measurements using Statevector
print("u.measure():", u.measure())    # u.measure() outputs the mesured state simulating the probability. On this example, it is 1/2 each
print("v.measure():", v.measure())

norm_squared = abs(v[0])**2 + abs(v[1])**2
print("Probability of vector v with norm:", norm_squared)
print("|0>", abs(v[0]) ** 2)
print("|1>", abs(v[1]) ** 2)

# Plotting the probability distribution
from qiskit.visualization import plot_histogram

statistics = v.sample_counts(1000)
display(statistics)
plot_histogram(statistics)

print("EOF")
