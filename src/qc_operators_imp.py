import numpy as np
from math import sqrt

# Define basic quantum gates
X = np.array([[0, 1], [1, 0]])
H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])
S = np.array([[1, 0], [0, (1j)]])
CNOT = np.array([[1, 0],
                 [0, 1]])


# Function to apply X gate to a quantum state
def apply_X(state):
    return np.dot(X, state)


# Function to apply Hadamard gate to a quantum state
def apply_H(state):
    return np.dot(H, state)


# Function to apply CNOT gate to a two-qubit quantum state
def apply_CNOT(state):
    return np.dot(CNOT, state)


def apply_S(state):
    return np.dot(S, state)


# Function to simulate a quantum measurement
def measure(state):
    # Calculate the probabilities (squared magnitudes of the amplitudes)
    probabilities = np.abs(state) ** 2
    # Perform measurement based on probabilities
    outcome = np.random.choice([0, 1], p=probabilities)
    return outcome

# Initial state |00⟩
state_0 = np.array([1 / sqrt(2), 1 / sqrt(2)])

# Apply Hadamard gate to the first qubit
state_after_H = apply_H(state_0[0:2])

# Apply CNOT gate (control qubit is qubit 0)
state_after_CNOT = apply_CNOT(state_0)

# Simulate measurement of the quantum state
measurement_result = measure(state_after_CNOT)

# Output the results
print("State after Hadamard and CNOT: ", state_after_CNOT)
print("Measurement result: ", measurement_result)

apply_S()
