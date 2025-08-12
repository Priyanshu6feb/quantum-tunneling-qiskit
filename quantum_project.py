from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Single-qubit circuit with 1 classical bit
qc = QuantumCircuit(1, 1)

# Put qubit 0 into superposition (50/50)
qc.h(0)

# Measure into classical bit 0
qc.measure(0, 0)

# Use Aer simulator
sim = AerSimulator()

# Transpile for the simulator and run
tqc = transpile(qc, sim)
result = sim.run(tqc, shots=1000).result()

# Get counts and plot
counts = result.get_counts()
print(counts)
plot_histogram(counts)
plt.title("Single-Qubit Superposition: Measurement Outcomes")
plt.show()
