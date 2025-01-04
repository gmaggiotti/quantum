from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
import json

def plot_vectors_state_probs(classical_state: str, circuit: QuantumCircuit, num_samples: int) -> None:
    state = Statevector.from_label(classical_state)
    measurement = state.evolve(circuit)
    statistics = measurement.sample_counts(num_samples)
    print(statistics)
    plot_histogram(statistics)


# Load key
def load_key(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['key']


key = load_key('../key.json')

num_doors = 3

# create the circuit

treasure_door = QuantumCircuit(num_doors, num_doors)
treasure_door.h([0, 2])
# Apply CNOT gates to entangle qubits 0 and 1, and qubits 2 and 1
treasure_door.cx([0, 2], 1)
treasure_door.x(2)
treasure_door.cx(2, 0)
treasure_door.x(2)
treasure_door.barrier(range(3))
treasure_door.swap(0, 1)
treasure_door.x([0, 1])
treasure_door.cx(2, 1)
treasure_door.x(2)
treasure_door.cx(2, 0)
treasure_door.x(2)
# treasure_door.measure([0, 1, 2], [0, 1, 2])
treasure_door.draw(output="mpl", idle_wires=False, style="iqp")
print(treasure_door)

# Run the circuit
classical_state = '100'
plot_vectors_state_probs(classical_state, treasure_door, 4000)


print("EOF")


