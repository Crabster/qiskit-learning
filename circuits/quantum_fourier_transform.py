import qiskit

from .common_gates import *
from math import pi

import random

def qft_iteration(n):
    qc = qiskit.QuantumCircuit(n)

    qc.h(n - 1)
    for i in range(n - 1):
        qc.cp(pi / 2**(n - i - 1), i, n - 1)

    gate = qc.to_gate()
    gate.name = f"QFT_{n}"
    return gate


def qft_gate(n):
    qc = qiskit.QuantumCircuit(n)

    for i in range(n, 0, -1): 
        qc.append(qft_iteration(i), range(i))

    for i in range(n // 2):
        qc.swap(i, n - i - 1)

    gate = qc.to_gate()
    gate.name = "QFT"
    return gate

def qft_example():
    n = 5
    qc = qiskit.QuantumCircuit(n, n)

    qft = qft_gate(n)

    qc.append(qft, range(n))

    qc.measure(range(n), range(n))

    return qc
