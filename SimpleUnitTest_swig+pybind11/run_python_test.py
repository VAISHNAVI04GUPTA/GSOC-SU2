import _testfluidmodel
import bindings
from math import sin

# Ensure the SWIG module has the TestFluidModel class
if hasattr(_testfluidmodel, 'TestFluidModel'):
    # Initiate test fluid model using SWIG-wrapped class
    fluid_model_test = _testfluidmodel.TestFluidModel()
    x = bindings.TestFluidModel()

    # Example calculation, computing the density based on pressure and temperature
    fluid_model_test.SetTDState_PT(2e5, 400)
    print(fluid_model_test.GetDensity())

    # Custom function to compute density based on pressure and temperature
    def customPTfunction(P_in, T_in):
        rho = P_in / (200 * sin(T_in) * T_in)
        return float(rho)

    # Goal: pass the customPTfunction to the fluid_model_test to compute the density
    result = x.SetTDState_Custom(101325, 300, customPTfunction)
    print("Custom density calculation value: %.3e" % result)
else:
    print("Error: _testfluidmodel does not have the TestFluidModel class")
