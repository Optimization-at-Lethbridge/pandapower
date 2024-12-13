import pandapower.networks as pn
import pandapower as pp
import pandapower.run as ppr
from enum import Enum
import pandapower.converter as pc
import os

class quantum_algorithm(Enum):
    HHL = 1
    VQLS = 2

        
#pp_net = cv.from_mpc('case9.mat', f_hz=60)
matpower_testcase_dir = os.path.join(pp.pp_dir, "matpowertestcases")
#matpower_testcase_dir = os.path.join(os.getcwd(), "matpowertestcases")
case3 = os.path.join(matpower_testcase_dir, 'case3.m')
net = pc.from_mpc(case3)

#net = pn.case5()
kwargs = {}
kwargs["QUANTUM_ALG"]=quantum_algorithm.VQLS.value  # QUANTUM_ALG = 1 for HHL and QUANTUM_ALG = 2 for VQLS
ppr.runpp_quantum(net, **kwargs)
#ppr.runpp(net)
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