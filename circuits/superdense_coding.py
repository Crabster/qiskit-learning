from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.extensions import Initialize
from qiskit_common import create_bell_pair

import matplotlib.pyplot as plt

import random

def superdense_coding_circuit():
    # Encode message which represent 2 classical registers to one qubit
    def encode_message(qc, qubit, msg):
        if msg == "00":
            pass        # To send 00 we do nothing
        elif msg == "10":
            qc.x(qubit) # To send 10 we apply an X-gate
        elif msg == "01":
            qc.z(qubit) # To send 01 we apply a Z-gate
        elif msg == "11":
            qc.z(qubit) # To send 11, we apply a Z-gate
            qc.x(qubit) # followed by an X-gate
        else:
            print("Invalid Message: Sending '00'")

    def decode_message(qc, a, b):
        qc.cx(a,b)
        qc.h(a)

    qc = QuantumCircuit(2)

    # First, Charlie creates the entangled pair between Alice and Bob
    create_bell_pair(qc, 0, 1)
    qc.barrier() 
    # At this point, qubit 0 goes to Alice and qubit 1 goes to Bob

    # Next, Alice encodes her message onto qubit 0
    message = random.choice(["00", "01", "10", "11"])
    encode_message(qc, 0, message)
    qc.barrier()

    # Alice then sends her qubit to Bob
    # After recieving qubit 0, Bob applies the recovery protocol
    decode_message(qc, 0, 1)

    # Finally, Bob measures his qubits to read Alice's message
    qc.measure_all()

    return qc
