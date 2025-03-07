import numpy as np
from qiskit_aer import AerSimulator
from qiskit.circuit import QuantumCircuit, Parameter
from qiskit import transpile
from qiskit_algorithms.minimum_eigensolvers import NumPyMinimumEigensolver
from qiskit_algorithms.optimizers import COBYLA
from qiskit.quantum_info import SparsePauliOp
from qiskit.primitives import BackendEstimator

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

# Create a BackendEstimator using AerSimulator
backend = AerSimulator()
estimator = BackendEstimator(backend)

# Define the classical optimizer
optimizer = COBYLA(maxiter=100)

# Define the VQE algorithm using the new API
from qiskit_algorithms.minimum_eigensolvers import VQE

vqe = VQE(
    estimator=estimator,
    ansatz=qc,
    optimizer=optimizer,
    initial_point=np.array([0.5])
)

# Run VQE to minimize the energy (loss)
result = vqe.compute_minimum_eigenvalue(hamiltonian)

print(f"Optimal energy (approximating sine wave): {result.eigenvalue}")
print(f"Optimal parameters: {result.optimal_parameters}")

# As a comparison, run an exact (classical) eigensolver
numpy_solver = NumPyMinimumEigensolver()
result_exact = numpy_solver.compute_minimum_eigenvalue(hamiltonian)
print(f"Exact energy: {result_exact.eigenvalue}")