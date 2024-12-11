import pandapower.networks as pn
import pandapower as pp

net = pn.case6ww()
#pp.runopp(net)
kwargs = {}
kwargs["QUANTUM_ALG"]=1
pp.runpp_quantum(net, **kwargs)
print(net.res_bus)
#pp.runopp_quantum(net, **kwargs)
#print(net.res_cost)