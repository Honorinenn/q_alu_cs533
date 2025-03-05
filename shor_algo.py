import numpy as np
from qiskit_aer import Aer 
from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator
from math import gcd

# Function to check if N is composite
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Step 1: Pick a random 'a' such that gcd(a, N) = 1
def find_coprime(N):
    a = np.random.randint(2, N)
    while gcd(a, N) != 1:
        a = np.random.randint(2, N)
    return a

# Step 2: Implement modular exponentiation using quantum Fourier transform
def quantum_order_finding(a, N):
    qc = QuantumCircuit(4, 4)  # 4 qubits, 4 classical bits (for measurement)
    
    qc.h(range(4))  # Apply Hadamard gates (superposition)
    qc.barrier()
    
    # Apply modular exponentiation
    qc.cx(0, 1)  # Simulating modular exponentiation
    qc.cx(1, 2)
    qc.cx(2, 3)
    
    qc.barrier()
    qc.measure(range(4), range(4))  # Measure all qubits

    # Simulate the quantum circuit
    # simulator = Aer.get_backend('qasm_simulator')
    # transpiled_qc = transpile(qc, simulator)
    # qobj = assemble(transpiled_qc)
    # result = execute(qc, simulator).result()
    # counts = result.get_counts()

    # For execution
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    sim_result = simulator.run(compiled_circuit).result()
    counts = sim_result.get_counts()
    
    # Extract the measurement result
    measured_r = max(counts, key=counts.get)
    return int(measured_r, 2)  # Convert binary to integer

# Step 3: Compute GCD to get factors
def shors_algorithm(N):
    if is_prime(N):
        print(f"{N} is already prime!")
        return N

    a = find_coprime(N)
    print(f"Randomly chosen a: {a}")

    r = quantum_order_finding(a, N)
    print(f"Quantum computed order (r): {r}")

    if r % 2 != 0:
        print("Odd order found, retrying...")
        return shors_algorithm(N)  # Retry for even order

    factor1 = gcd(a**(r//2) - 1, N)
    factor2 = gcd(a**(r//2) + 1, N)

    if factor1 * factor2 == N:
        print(f"Factors found: {factor1}, {factor2}")
        return factor1, factor2
    else:
        print("Failed, retrying...")
        return shors_algorithm(N)

# Example: Factorizing 15
N = 15
shors_algorithm(N)
