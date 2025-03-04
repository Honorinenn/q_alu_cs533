from qiskit import QuantumCircuit

# Define a quantum circuit with 4 qubits (2 for input, 1 for result, 1 for auxiliary)
qc = QuantumCircuit(4)

# Addition using Quantum Ripple-Carry Adder
from qiskit.circuit.library import QFT

qc.h(0)
qc.h(1)
qc.append(QFT(3), [0, 1, 2])  # Apply Quantum Fourier Transform
qc.draw('mpl')


# Subtraction using Quantum Circuits
qc.x(1)  # Negate the second operand
qc.append(QFT(3), [0, 1, 2])  # Perform addition
qc.draw('mpl')


# XOR and AND using Quantum gates

qc.cx(0, 1)
qc.draw('mpl')
