import pandapower.networks as pn
import pandapower as pp
import pandapower.run as ppr
from enum import Enum
import pandapower.converter as pc
import os

class quantum_algorithm(Enum):
    HHL = 1
    VQLS = 2

matpower_testcase_dir = os.path.join(pp.pp_dir, "matpowertestcases")
case3 = os.path.join(matpower_testcase_dir, 'case3.m')
net = pc.from_mpc(case3)
net = pn.case6ww()
kwargs = {}
kwargs["QUANTUM_ALG"]=quantum_algorithm.VQLS.value  # QUANTUM_ALG = 1 for HHL and QUANTUM_ALG = 2 for VQLS
#ppr.rundcopp_quantum(net, **kwargs)
ppr.runopp_quantum(net, **kwargs)
#ppr.runopp(net)
#ppr.rundcopp(net)
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

