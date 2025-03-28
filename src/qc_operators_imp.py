import numpy as np
from math import sqrt

from qiskit.visualization import plot_histogram

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

def apply_CZ(state):
    """
    Apply the Controlled-Z (CZ) gate to a two-qubit quantum state.

    Parameters:
    state (numpy.ndarray): A numpy array representing the quantum state vector.

    Returns:
    numpy.ndarray: The resulting quantum state after applying the CZ gate.
    """
    # Define the Controlled-Z gate
    CZ = np.array([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, -1]])
    
    # Apply the CZ gate to the state
    return np.dot(CZ, state)

# Function to simulate a quantum measurement
def measure(state):
    """
    Measure a quantum state.

    This function calculates the probabilities of the quantum state by taking 
    the squared magnitudes of the amplitudes. It then performs a measurement 
    based on these probabilities and returns the outcome.

    Parameters:
    state (numpy.ndarray): A numpy array representing the quantum state vector.

    Returns:
    int: The outcome of the measurement, either 0 or 1.
    """
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

#  Performing operations with Operator and Statevector
from qiskit.quantum_info import Operator, Statevector

X = Operator([[0, 1], [1, 0]])
Y = Operator([[0, -1.0j], [1.0j, 0]])
Z = Operator([[1, 0], [0, -1]])
H = Operator([[1 / sqrt(2), 1 / sqrt(2)], [1 / sqrt(2), -1 / sqrt(2)]])
S = Operator([[1, 0], [0, 1.0j]])
T = Operator([[1, 0], [0, (1 + 1.0j) / sqrt(2)]])

v = Statevector([1, 0])

v = v.evolve(H)
v = v.evolve(T)
v = v.evolve(H)
v = v.evolve(T)
v = v.evolve(Z)

print(v.draw("text"))

from qiskit import QuantumCircuit

circuit = QuantumCircuit(1)

circuit.h(0)
circuit.t(0)
circuit.h(0)
circuit.t(0)
circuit.z(0)

circuit.draw()

# simulate the result of running this circuit
ket0 =Statevector([1, 0])
v = ket0.evolve(circuit)
statistics = v.sample_counts(4000)
plot_histogram(statistics)

# simulate same result using matrix multiplication
ket0 = np.array([1, 0])
aux = np.matmul(H, ket0)
aux = np.matmul(T, aux)
aux = np.matmul(H, aux)
aux = np.matmul(T, aux)
aux = np.matmul(Z, aux)

print("state probabilities", aux)
print("colapsed into a classical state",measure(aux))
print("EOL")

