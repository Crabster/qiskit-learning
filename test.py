from qiskit import QuantumCircuit, QuantumRegister
from qiskit_common import create_bell_pair

def test_circuit():
    qr = QuantumRegister(2) 
    qc = QuantumCircuit(qr)

    qc.x(0)
    qc.x(1)
    create_bell_pair(qc, 0, 1)

    qc.measure_all()
    qc.draw(output='mpl')
    return qc


