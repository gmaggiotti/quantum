# General
# https://learning.quantum.ibm.com/tutorial/chsh-inequality

import numpy as np

# Qiskit imports
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.quantum_info import SparsePauliOp

# Qiskit Runtime imports
from qiskit_ibm_runtime import QiskitRuntimeService, Estimator, Batch

# Plotting routines
import matplotlib.pyplot as plt
import matplotlib.ticker as tck