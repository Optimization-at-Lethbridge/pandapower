import pandapower.networks as pn
import pandapower.run as pp
from enum import Enum

class quantum_algorithm(Enum):
    HHL = 1
    VQLS = 2


net = pn.case5()
kwargs = {}
kwargs["QUANTUM_ALG"]=quantum_algorithm.VQLS.value  # QUANTUM_ALG = 1 for HHL and QUANTUM_ALG = 2 for VQLS
pp.runpp_quantum(net, **kwargs)
# Check if the power flow converged
if net.converged:
    print("Power Flow Converged!")

    # Print Results
    print("\n=== Bus Results ===")
    print(net.res_bus)  # Voltage magnitudes and angles at buses

    print("\n=== Line Results ===")
    print(net.res_line)  # Line loading, losses, and power flow

    print("\n=== Load Results ===")
    print(net.res_load)  # Load power consumption

    print("\n=== External Grid Results ===")
    print(net.res_ext_grid)  # Power injected by the external grid
else:
    print("Power Flow did not converge. Check your input data or constraints.")

#pp.runopp_quantum(net, **kwargs)
#print(net.res_cost)