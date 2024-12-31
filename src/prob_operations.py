import math
import numpy as np


# M = ∑ ∣f(a)⟩⟨a∣
#     a∈Σ

f_a = np.array([[1 / 2, 1 / 2]]).T
a = np.array([[0, 1]])
result = np.matmul(f_a, a)
print(result)

# The example of a qubit state vector above is very commonly encountered —
# it is called the plus state and is denoted as follows:
# |+⟩ = √2/2 |0⟩ + √2/2 |1⟩
plus_state = np.array([1 / math.sqrt(2), 1 / math.sqrt(2)])
print(plus_state[0])
minus_state = np.array([1 / math.sqrt(2), -1 / math.sqrt(2)])

print(np.dot(plus_state, minus_state))

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
print(R)

X = matmul(R, R)
# NOT matrix
print(round(X, 0))
