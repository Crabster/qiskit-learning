from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.extensions import Initialize
from qiskit_textbook.tools import random_state
from qiskit_common import create_bell_pair

def quantum_teleportation_circuit():
    qr = QuantumRegister(3)    # Protocol uses 3 qubits
    qc = QuantumCircuit(qr)

    def alice_gates(qc, psi, a):
        qc.cx(psi, a) # CNOT with control qubit (Alice to be teleported) on qubit (Eve)
        qc.h(psi) # H on Alice qubit

    def bob_gates(qc, a, e, b):
        qc.cz(a, b) # CZ with control qubit (Alice) on qubit (Bob)
        qc.cx(e, b) # CNOT with control qubit (Eve) on qubit (Bob)

    psi = random_state(1)
    init_gate = Initialize(psi) # Creates gate to transform Alice qubit to psi state
    init_gate.label = "init"
    qc.append(init_gate, [0])

    qc.barrier()
    create_bell_pair(qc, 1, 2) # Entangles Eve with Bob

    qc.barrier() 
    alice_gates(qc, 0, 1)

    qc.barrier() 
    bob_gates(qc, 0, 1, 2)

    inverse_init_gate = init_gate.gates_to_uncompute() # Reverse gate from psi to |0>
    qc.append(inverse_init_gate, [2])
    cr_result = ClassicalRegister(1)
    qc.add_register(cr_result)
    qc.measure(2, 0)

    return qc
