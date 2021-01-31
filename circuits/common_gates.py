import qiskit

from math import pi
from random import random

def random_state_gate():
    theta = 2*pi*random()
    phi = 2*pi*random()
    lam = 2*pi*random()

    qr = qiskit.QuantumRegister(1)
    qc = qiskit.QuantumCircuit(qr)
    qc.u3(theta, phi, lam, 0)
    gate = qc.to_gate()
    gate.name = f"$U_3$ {theta:.2f},{phi:.2f},{lam:.2f}"
    return gate

def phi_plus_gate():
    qr = qiskit.QuantumRegister(2)
    qc = qiskit.QuantumCircuit(qr)
    qc.h(0)
    qc.cx(0, 1)
    gate = qc.to_gate()
    gate.name = "$\phi^{+}$"
    return gate

def phi_minus_gate():
    qr = qiskit.QuantumRegister(2)
    qc = qiskit.QuantumCircuit(qr)
    qc.h(0)
    qc.cx(0, 1)
    qc.x(0)
    qc.z(0)
    gate = qc.to_gate()
    gate.name = "$\phi^{-}$"
    return gate

def psi_plus_gate():
    qr = qiskit.QuantumRegister(2)
    qc = qiskit.QuantumCircuit(qr)
    qc.h(0)
    qc.cx(0, 1)
    qc.x(0)
    gate = qc.to_gate()
    gate.name = "$\psi^{+}$"
    return gate

def psi_minus_gate():
    qr = qiskit.QuantumRegister(2)
    qc = qiskit.QuantumCircuit(qr)
    qc.h(0)
    qc.cx(0, 1)
    qc.z(0)
    gate = qc.to_gate()
    gate.name = "$\psi^{-}$"
    return qc
