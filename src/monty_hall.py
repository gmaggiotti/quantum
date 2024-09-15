from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Define the number of doors (qubits)
num_doors = 3

# Create a quantum circuit with 3 qubits and 3 classical bits
qc = QuantumCircuit(num_doors, num_doors)

# Initialize the doors (qubits) in a superposition state
qc.h(range(num_doors))

# Contestant's initial choice (e.g., door 0)
qc.x(0)
qc.barrier()

# Monty Hall opens a door (e.g., door 1)
qc.x(1)
qc.measure(1, 1)

# Contestant switches or doesn't switch
switch = True  # Set to False for no switch

if switch:
    qc.x(0)
    qc.x(2)
qc.barrier()

# Measure the outcome
qc.measure(range(num_doors), range(num_doors))

# Run the circuit
simulator = AerSimulator()
qc_compiled = transpile(qc, simulator)
job = simulator.run(qc_compiled, shots=1024)
result = job.result()

# Print the probabilities
print(result.get_counts(qc_compiled))