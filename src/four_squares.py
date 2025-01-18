from qiskit import QuantumCircuit
import json
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
# Load key
def load_key(filename):
    with open(filename) as f:
        data = json.load(f)
    return data['key']


key = load_key('../key.json')

num_qubits = 10
def plot_vectors_state_probs(classical_state: str, circuit: QuantumCircuit, num_samples: int) -> None:
    state = Statevector.from_label(classical_state)
    # Evolve the state through the quantum circuit
    measurement = state.evolve(circuit)

    #  Simulate measurement
    statistics = measurement.sample_counts(num_samples)
    print("Raw measurement results: ", statistics)

    # Convert counts to probabilities
    total_counts = sum(statistics.values())
    probabilities = {state: count / total_counts for state, count in statistics.items()}
    plot_histogram(probabilities)


# create the circuit

four_squares = QuantumCircuit(num_qubits, num_qubits)
four_squares.h([0, 1, 2, 3])
four_squares.barrier([4, 5])
four_squares.h([4, 5])
four_squares.barrier(range(4, 7))
four_squares.cx([1, 3], 6)
four_squares.barrier([6, 7])
four_squares.cx([2, 3], 7)
four_squares.barrier([6, 7])
four_squares.cx(4, 6)
four_squares.cx(5, 7)
four_squares.ccx(6, 7, 3)
four_squares.x(6)
four_squares.ccx(6, 7, 2)
four_squares.x(6)
four_squares.barrier([6, 7])

four_squares.x(7)
four_squares.ccx(6, 7, 1)
four_squares.x(7)
four_squares.barrier([6, 7])
four_squares.x(6)
four_squares.x(7)
four_squares.ccx(6, 7, 0)
four_squares.x(6)
four_squares.x(7)
four_squares.barrier([0, 9])
four_squares.cx([1, 3], 8)
four_squares.cx([2, 3], 8)

four_squares.draw('mpl')
print(four_squares)

# Run the circuit
classical_state = '1000000000'
plot_vectors_state_probs(classical_state, four_squares, 4000)
print("EOF")