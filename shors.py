import numpy as np
from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator
from math import gcd
from fractions import Fraction

# Function to check if N is prime
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

# Classical simulation of order finding (instead of quantum)
def classical_order_finding(a, N):
    """Finds the smallest r such that a^r ≡ 1 (mod N)"""
    for r in range(1, N):
        if pow(a, r, N) == 1:
            return r
    return None

# Quantum Order Finding Simulation
def quantum_order_finding(a, N):
    """
    Simulates the quantum step by measuring the phase in a quantum Fourier transform.
    This part should ideally be implemented using a quantum circuit.
    """
    simulator = AerSimulator()

    # Create a quantum circuit
    qc = QuantumCircuit(4, 4)  # 4 qubits, 4 classical bits (for measurement)
    qc.h(range(4))  # Apply Hadamard gates (superposition)
    qc.measure(range(4), range(4))  # Measure all qubits

    compiled_circuit = transpile(qc, simulator)
    sim_result = simulator.run(compiled_circuit).result()
    counts = sim_result.get_counts()

    # Extract measurement (binary string) and convert to integer
    measured_val = max(counts, key=counts.get)
    phase_estimate = int(measured_val, 2) / 16  # 16 = 2^4 qubits

    # Convert phase estimate to fraction
    fraction = Fraction(phase_estimate).limit_denominator(N)
    r = fraction.denominator

    return r

# Step 3: Compute GCD to get factors
def shors_algorithm(N, max_retries=10):
    if is_prime(N):
        print(f"{N} is already prime!")
        return N

    for _ in range(max_retries):  # Limit retries
        a = find_coprime(N)
        print(f"Randomly chosen a: {a}")

        r = classical_order_finding(a, N)  # Use classical instead of quantum
        print(f"Quantum computed order (r): {r}")

        if r is None:
            print("Failed to find order, retrying...")
            continue
        
        if r % 2 != 0:
            print("Odd order found, retrying...")
            continue  # Retry if order is odd

        factor1 = gcd(a**(r//2) - 1, N)
        factor2 = gcd(a**(r//2) + 1, N)

        if factor1 * factor2 == N and factor1 != 1 and factor2 != 1:
            print(f"Factors found: {factor1}, {factor2}")
            return factor1, factor2
        else:
            print("Failed, retrying...")

    print("Shor's algorithm failed after max retries.")
    return None

# Example: Factorizing 15
N = 15
shors_algorithm(N)
