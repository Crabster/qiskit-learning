import qiskit 

from .common_gates import *

def quantum_teleportation_circuit():
    qr = qiskit.QuantumRegister(3)   
    crz = qiskit.ClassicalRegister(1, name="cbz")    
    crx = qiskit.ClassicalRegister(1, name="cbx")    
    qc = qiskit.QuantumCircuit(qr)

    phi_plus = phi_plus_gate()
    qc.append(phi_plus, [1, 2])
    qc.append(phi_plus.inverse(), [0, 1])

    qc.barrier()

    qc.cx(1, 2)
    qc.cz(0, 2)

    qc.name = "TP"
    return qc

def quantum_teleportation_example():
    qr = qiskit.QuantumRegister(3)   
    cr = qiskit.ClassicalRegister(1)    
    qc = qiskit.QuantumCircuit(qr, cr)

    rand_state = random_state_gate()
    qc.append(rand_state, [0])

    tp_qc = quantum_teleportation_circuit()
    qc.append(tp_qc, [0, 1, 2])

    qc.append(rand_state.inverse(), [2])
    qc.measure([2], [0])

    return qc
