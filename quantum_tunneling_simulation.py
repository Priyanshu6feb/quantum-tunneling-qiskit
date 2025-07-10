from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Initialize a single qubit quantum circuit
qc = QuantumCircuit(1, 1)

# Apply Hadamard to simulate superposition (wave behavior)
qc.h(0)

# Simulate a simple 'barrier': with 50% chance, measure directly
qc.measure(0, 0)

# Run simulation on Qiskit Aer simulator
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1000)
result = job.result()
counts = result.get_counts()

# Plot result
plot_histogram(counts)
plt.title("Quantum Tunneling Analogy: Single Qubit Measurement")
plt.show()
