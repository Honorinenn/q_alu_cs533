# Quantum Arithmetic Operations
This project demonstrates how to implement basic arithmetic operations such as addition, subtraction, multiplication, XOR, AND, and division using quantum circuits built with Qiskit.

# 1) Requirements
Install the required Python packages using:
%pip install qiskit
%pip install pylatexenc
Note: These commands are designed for Jupyter or IPython environments (e.g., Google Colab, Jupyter Notebooks). Use pip install directly in terminal if running locally.

# 2) Operations Covered
➕ Quantum Addition (Ripple-Carry Adder)
Uses the Quantum Fourier Transform (QFT) to simulate the addition of two qubits. The result is stored in a third qubit.
➖ Quantum Subtraction
Negates the second operand and applies QFT addition, simulating subtraction.
❌ XOR Operation
Implements bitwise XOR using a CNOT (CX) gate.
✅ AND Operation
Implements logical AND using a Toffoli (CCX) gate, storing the result in a third qubit.
✖️ Quantum Multiplication
Multiplies two qubits using Hadamard gates for superposition, QFT for transformation, and Toffoli gate for controlled multiplication.
➗ Quantum Division
Simulates division using Inverse QFT and Toffoli gates as a placeholder for controlled subtraction-based division logic.

# 3) Qubit Layout
The circuits typically use 4 qubits:
•	q0, q1: Input qubits
•	q2: Result qubit
•	q3: Auxiliary (if required)

# 4) Circuit Visualization

•	Circuits are visualized using:
qc.draw('mpl')

•	Make sure pylatexenc and matplotlib are installed for graphical rendering. Alternatively, use:
qc.draw('text')





