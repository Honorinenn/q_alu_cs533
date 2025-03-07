import numpy as np
from qiskit_aer import Aer
from qiskit_aer import AerSimulator
from qiskit.circuit import QuantumCircuit, Parameter
from qiskit_algorithms import VQE
from qiskit_algorithms.optimizers import COBYLA
from qiskit.primitives import Sampler

sampler = Sampler()

# Define the quantum circuit (a simple single qubit rotation)
theta = Parameter('θ')
qc = QuantumCircuit(1)
qc.rx(theta, 0)  # Apply a single RX gate with parameter θ

# For execution
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
sim_result = simulator.run(compiled_circuit).result()
counts = sim_result.get_counts()

# Define the Hamiltonian to optimize (for simplicity, just the Z operator here)
from qiskit.opflow import Z
hamiltonian = Z

# Define the classical optimizer
optimizer = COBYLA()

# Define the quantum instance (simulator backend)
#backend = Aer.get_backend('statevector_simulator')
#quantum_instance = QuantumInstance(backend)

# Define the VQE algorithm
vqe = VQE(ansatz=qc, optimizer=optimizer, quantum_instance=quantum_instance)

# Initial guess for the parameter θ
initial_params = np.array([0.5])

# Run VQE to minimize the energy (loss)
result = vqe.compute_minimum_eigenvalue(hamiltonian)

print(f"Optimal energy (approximating sine wave): {result.eigenvalue}")
