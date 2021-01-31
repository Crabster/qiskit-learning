import qiskit

from .common_gates import *

def test_circuit():
    qr = qiskit.QuantumRegister(1)   
    cr = qiskit.ClassicalRegister(1)    
    qc = qiskit.QuantumCircuit(qr, cr)

    rand_state = random_state_gate()
    qc.append(rand_state, [0])
    qc.append(rand_state.inverse(), [0])
    qc.measure([0], [0])
    return qc


