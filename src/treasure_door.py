from qiskit import QuantumCircuit
import json
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler


# Load key
def load_key(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['key']


key = load_key('../key.json')

# create the service
service = QiskitRuntimeService(channel="ibm_quantum", token=key)
backend = service.least_busy(operational=True, simulator=False)
print(backend.name)

sampler = Sampler(backend)

# create the circuit

treasure_door = QuantumCircuit(3)
treasure_door.h(0)
treasure_door.h(2)
treasure_door.cx(0, 1)
treasure_door.cx(2, 1)
treasure_door.x(2)
treasure_door.cx(2, 0)
treasure_door.x(2)
treasure_door.barrier(range(3))
treasure_door.swap(0, 1)
treasure_door.x(0)
treasure_door.x(1)
treasure_door.cx(2, 1)
treasure_door.x(2)
treasure_door.cx(2, 0)
treasure_door.x(2)
treasure_door.measure_all()
treasure_door.draw(output="mpl", idle_wires=False, style="iqp")
print(treasure_door)

# TODO: make this call as batch
job = sampler.run([treasure_door])
print(f"job id: {job.job_id()}")
result = job.result()
print(result)
