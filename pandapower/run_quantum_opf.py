import pandapower.networks as pn
import pandapower.run as pp
from enum import Enum

class quantum_algorithm(Enum):
    HHL = 1
    VQLS = 2


net = pn.case6ww()
kwargs = {}
kwargs["QUANTUM_ALG"]=quantum_algorithm.VQLS.value  # QUANTUM_ALG = 1 for HHL and QUANTUM_ALG = 2 for VQLS
pp.runopp_quantum(net, **kwargs)
# Check if OPF was successful
if net["OPF_converged"]:
    print("Optimal Power Flow Results:")

    # Print results for generators
    print("\nCost:")
    print(net.res_cost)

    # Print results for generators
    print("\nGenerator Results:")
    print(net.res_gen)

    # Print results for loads
    print("\nLoad Results:")
    print(net.res_load)

    # Print results for buses
    print("\nBus Voltage Results:")
    print(net.res_bus)

    # Print results for branches (lines)
    print("\nLine Loading Results:")
    print(net.res_line)
else:
    print("OPF did not converge.")

