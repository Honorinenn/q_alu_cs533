import numpy as np
from qiskit_aer import Aer, AerSimulator
from qiskit.circuit import QuantumCircuit, Parameter
from qiskit import transpile
from qiskit_algorithms.minimum_eigensolvers import VQE
from qiskit_algorithms.optimizers import COBYLA
from qiskit.primitives import Estimator  # Using Estimator instead of Sampler
from qiskit.quantum_info import SparsePauliOp

# Define the quantum circuit (a simple single qubit rotation)
theta = Parameter('θ')
qc = QuantumCircuit(1)
qc.rx(theta, 0)  # Apply a single RX gate with parameter θ

# For execution and testing
test_circuit = qc.copy()
test_circuit.measure_all()  # Add measurement for testing

# Run a test with a fixed parameter
simulator = AerSimulator()
bound_qc = test_circuit.assign_parameters({theta: 0.5})
compiled_circuit = transpile(bound_qc, simulator)
sim_result = simulator.run(compiled_circuit).result()
counts = sim_result.get_counts()
print("Counts:", counts)

# Define the Hamiltonian to optimize (Z operator using updated syntax)
hamiltonian = SparsePauliOp('Z')

# Define the classical optimizer
optimizer = COBYLA(maxiter=100)

# Set up the VQE with proper Estimator primitive
estimator = Estimator()  # This is the correct primitive for VQE

# Define the VQE algorithm using the new API
vqe = VQE(
    estimator=estimator,
    ansatz=qc,  # Using the circuit without measurements
    optimizer=optimizer,
    initial_point=np.array([0.5])
)

# Run VQE to minimize the energy (loss)
result = vqe.compute_minimum_eigenvalue(hamiltonian)

print(f"Optimal energy (approximating sine wave): {result.eigenvalue}")
print(f"Optimal parameters: {result.optimal_parameters}")