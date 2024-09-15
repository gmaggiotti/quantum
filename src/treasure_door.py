from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import json


# Load key
def load_key(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['key']


key = load_key('../key.json')

num_doors = 3

# create the circuit

treasure_door = QuantumCircuit(num_doors, num_doors)
treasure_door.h(0)
treasure_door.h(2)
# Apply CNOT gates to entangle qubits 0 and 1, and qubits 2 and 1
treasure_door.cx([0, 2], 1)
treasure_door.x(2)
treasure_door.cx(2, 0)
treasure_door.x(2)
treasure_door.barrier(range(3))
treasure_door.swap(0, 1)
treasure_door.x([0,1])
treasure_door.cx(2, 1)
treasure_door.x(2)
treasure_door.cx(2, 0)
treasure_door.x(2)
treasure_door.measure([0, 1, 2], [0, 1, 2])
treasure_door.draw(output="mpl", idle_wires=False, style="iqp")
print(treasure_door)

# Run the circuit
simulator = AerSimulator()
qc_compiled = transpile(treasure_door, simulator)
job = simulator.run(qc_compiled, shots=1024)
result = job.result()

# Print the probabilities
print(result.get_counts(qc_compiled))


