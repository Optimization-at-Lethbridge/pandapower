## Pandapower-Quantum

**A Quantum-Enhanced Power System Analysis Toolbox**

This repository extends the capabilities of the original Pandapower toolbox by integrating quantum computing algorithms to address complex power system problems.

### Key Features

* **Quantum-Accelerated Linear Equation Solvers (HHL):**

> Leverages the power of quantum computation to efficiently solve large-scale linear systems of equations, a crucial step in power flow and optimal power flow calculations. HHL utilizes quantum superposition and interference to achieve potential exponential speedups compared to classical methods.

* **Variational Quantum Linear Solver (VQLS):**

> This hybrid quantum-classical algorithm combines the strengths of both worlds. VQLS tackles problems that are challenging to express using traditional quantum algorithms by working in conjunction with classical optimization techniques. The systems of linears equations can be effectively solved by VQLS. It would help to find the search direction in the convergence for both power flow (PF) and optimal power flow (OPF). The PF used Newton-Raphson (NR) method and OPF uses Primal Dual Interior Point Method (PDIPM).



### Usage

**Solving Power Flow (PF) using HHL or VQLS**

```python

import pandapower.networks as pn
import pandapower as pp
import pandapower.run as ppr
from enum import Enum
import pandapower.converter as pc
import os

class quantum_algorithm(Enum):
    HHL = 1
    VQLS = 2

#matpower_testcase_dir = os.path.join(pp.pp_dir, "matpowertestcases")
#matpower_testcase_dir = os.path.join(os.getcwd(), "matpowertestcases")
#case3 = os.path.join(matpower_testcase_dir, 'case3.m')
#net = pc.from_mpc(case3)
net = pn.case5()
kwargs = {}
# QUANTUM_ALG = 1 for HHL and QUANTUM_ALG = 2 for VQLS
kwargs["QUANTUM_ALG"]=quantum_algorithm.VQLS.value  
ppr.runpp_quantum(net, **kwargs)

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

```



**Solving Optimal Power Flow (OPF) using HHL or VQLS**

```python
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
#matpower_testcase_dir = os.path.join(os.getcwd(), "matpowertestcases")
case3 = os.path.join(matpower_testcase_dir, 'case3.m')
net = pc.from_mpc(case3)
#net = pn.case6ww()
kwargs = {}

# QUANTUM_ALG = 1 for HHL and QUANTUM_ALG = 2 for VQLS
kwargs["QUANTUM_ALG"]=quantum_algorithm.VQLS.value  
ppr.runopp_quantum(net, **kwargs)
#ppr.rundcopp_quantum(net, **kwargs)

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
```



   <html>
   <a href="https://www.pandapower.org">
      <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://www.pandapower.org/images/pp_light.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://www.pandapower.org/images/pp.svg">
      <img alt="logo" src="//www.pandapower.org/images/pp.svg">
      </picture>
   </a>
   </html>


   <html>
   <img alt="PyPI" src="https://badge.fury.io/py/pandapower.svg">
   <a href="https://pypi.python.org/pypi/pandapower" target="_blank">

   <img alt="versions" src="https://img.shields.io/pypi/pyversions/pandapower.svg">
   <a href="https://pypi.python.org/pypi/pandapower" target="_blank">

   <img alt="docs" src="https://readthedocs.org/projects/pandapower/badge/">
   <a href="http://pandapower.readthedocs.io/" target="_blank">

   <img alt="codecov" src="https://codecov.io/github/e2nIEE/pandapower/coverage.svg?branch=master">
   <a href="https://app.codecov.io/github/e2nIEE/pandapower?branch=master" target="_blank">

   <img alt="codacy" src="https://api.codacy.com/project/badge/Grade/e2ce960935fd4f96b4be4dff9a0c76e3">
   <a href="https://app.codacy.com/gh/e2nIEE/pandapower?branch=master" target="_blank">

   <img alt="BSD" src="https://img.shields.io/badge/License-BSD%203--Clause-blue.svg">
   <a href="https://github.com/e2nIEE/pandapower/blob/master/LICENSE" target="_blank">

   <img alt="pepy" src="https://pepy.tech/badge/pandapower">
   <a href="https://pepy.tech/project/pandapower" target="_blank">

   <img alt="PyPI" src="https://mybinder.org/badge_logo.svg">
   <a href="https://mybinder.org/v2/gh/e2nIEE/pandapower/master?filepath=tutorials" target="_blank">

   </html>

### About pandapower

<html>
<p>pandapower is an easy to use network calculation program aimed to automate the analysis and optimization of power
systems. It uses the data analysis library <a href="http://pandas.pydata.org">pandas</a> and is compatible with the commonly used MATPOWER / PYPOWER case format. pandapower allows using different solvers including an improved Newton-Raphson power flow implementation, all <a href="https://pypi.python.org/pypi/PYPOWER">PYPOWER</a> solvers, the C++ library solvers for fast steady-state distribution power system analysis of <a href="https://github.com/PowerGridModel/power-grid-model">PowerGridModel</a>, the Newton-Raphson power flow solvers in the C++ library <a href="https://github.com/BDonnot/lightsim2grid/">lightsim2grid</a>, and the <a href="https://github.com/lanl-ansi/PowerModels.jl/">PowerModels.jl</a> library.</p>

<p>
More information about pandapower can be found on <a href="https://www.pandapower.org/">www.pandapower.org</a>:
</p>
</html>

### Citing pandapower:

<html>
<p>
-<a href="https://www.pandapower.org/about/#modeling">Power System Modeling</a>
</p>
<p>
-<a href="https://www.pandapower.org/about/#analysis">Power System Analysis</a>
</p>
<p>
-<a href="https://www.pandapower.org/references/">Citing pandapower</a>
</p>
</html>

### Getting Started:

<html>
<p>
-<a href="https://www.pandapower.org/start/">Installation Notes</a>
</p>
<p>
-<a href="<https://www.pandapower.org/start/#intro">Minimal Example</a>
</p>
<p>
-<a href="https://www.pandapower.org/start/#tutorials">Interactive Tutorials</a>
</p>
<p>
-<a href="https://pandapower.readthedocs.io/">Documentation</a>
</p>
</html>


<html>
If you are interested in the latest pandapower developments, subscribe to our <a href="https://www.pandapower.org/contact/#list">mailing list</a>!
</html>


 <html>
   <a href="https://www.simbench.net">
      <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://simbench.de/wp-content/uploads/2019/01/logo.png">
      <source media="(prefers-color-scheme: light)" srcset="https://simbench.de/wp-content/uploads/2019/01/logo.png">
      <img alt="SimBench_logo" src="https://simbench.de/wp-content/uploads/2019/01/logo.png">
      </picture>
   </a>
 </html>


<html>
To get realistic load profile data and grid models across all voltage levels that are ready to
be used in pandapower, have a look at the *SimBench* <a href="https://www.simbench.net">project website</a> or <a href="https://github.com/e2nIEE/simbench">on GitHub</a>.
</html>

 <html>
   <a href="https://www.pandapipes.org">
      <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://www.pandapipes.org/images/pp.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://www.pandapipes.org/images/pp.svg">
      <img alt="pandapipes_logo" src="https://www.pandapipes.org/images/pp.svg">
      </picture>
   </a>
 </html>


<html>
If you want to model pipe networks (heat, gas or water) as well, we recommend
pandapower's sibling project *pandapipes* (<a href="https://www.pandapipes.org">website</a>, <a href="https://github.com/e2nIEE/pandapipes">GitHub repository</a>).
</html>


pandapower is a joint development of the research group Energy Management and Power System Operation, University of Kassel and the Department for Distribution System
Operation at the Fraunhofer Institute for Energy Economics and Energy System Technology (IEE), Kassel.

   <html>
   <img alt="PyPI" src="http://www.pandapower.org/images/contact/Logo_e2n.png">
   <a href="https://www.uni-kassel.de/eecs/en/sections/energiemanagement-und-betrieb-elektrischer-netze/home" target="_blank">

   </html>



   <html>
    <a href="https://www.iee.fraunhofer.de/en.html">
       <picture>
         <source media="(prefers-color-scheme: dark)" srcset="https://www.pandapower.org/images/contact/Logo_Fraunhofer_IEE_negativ.png">
         <source media="(prefers-color-scheme: light)" srcset="https://www.pandapower.org/images/contact/Logo_Fraunhofer_IEE.png">
         <img alt="logo" src="https://www.pandapower.org/images/contact/Logo_Fraunhofer_IEE.png" width=500 >
       </picture>
    </a>
    </html>



<html>

We welcome contributions to pandapower of any kind. If you want to contribute, please check out the <a href="https://github.com/e2nIEE/pandapower/blob/develop/CONTRIBUTING.rst">pandapower contribution guidelines</a>.

</html>
