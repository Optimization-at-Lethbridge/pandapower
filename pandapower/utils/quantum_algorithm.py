from enum import Enum

class quantum_algorithm(Enum):
    HHL = 1
    VQLS = 2



print(quantum_algorithm.HHL)
print(quantum_algorithm.HHL.name)
print(quantum_algorithm.HHL.value)
print(type(quantum_algorithm.HHL))
print(repr(quantum_algorithm.HHL))
print(list(quantum_algorithm))