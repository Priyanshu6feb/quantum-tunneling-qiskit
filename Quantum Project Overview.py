# Quantum Tunneling Simulation Using Qiskit

This repository contains a simple simulation of quantum tunneling behavior using Qiskit. The project demonstrates the use of quantum circuits to model probabilistic outcomes, akin to a quantum particle interacting with a potential barrier.

---

## 🧠 Project Overview
This project uses a single-qubit quantum circuit to:
- Create superposition using a Hadamard gate
- Simulate a quantum measurement as an analogy to tunneling
- Visualize results using Qiskit's histogram plot

Though simplified, the model provides intuitive insights into quantum mechanics principles like superposition and probabilistic collapse.

---

## 📁 Files Included
- `quantum_project.py` — Qiskit code to run the simulation
- `project_summary.txt` — Written summary for applications or resumes

---

## 🚀 How to Run
1. Install Qiskit:
```bash
pip install qiskit matplotlib
```
2. Run the Python script:
```bash
python quantum_project.py
```
3. View the histogram output and review the summary file.

Quick Start
python3 -m pip install --upgrade pip
python3 -m pip install qiskit qiskit-aer matplotlib
python3 quantum_project.py

---

Code Snippet

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

sim = AerSimulator()
result = sim.run(transpile(qc, sim), shots=1000).result()
counts = result.get_counts()

print(counts)
plot_histogram(counts)
plt.title("Single-Qubit Superposition: Measurement Outcomes")
plt.show()

## 📌 Author
Priyanshu Singh — High school student interested in physics and quantum computing. Created as an independent initiative to explore the interface of quantum mechanics and computer science.
