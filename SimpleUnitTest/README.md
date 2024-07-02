# Compile C++ function to python class

The files in this folder can be used to compile C++ code files into python modules. 
You can use this to experiment with linking python functions to C++.

Before you begin, make sure you have ```swig``` installed.

The C++ code describes a simple fluid model which uses the ideal gas law to compute the pressure, temperature, and density.
This code is compiled to a ```TestFluidModel``` class which can be accessed in python, similarly to the ```Driver``` class 
in the SU2 python wrapper. 

The goal is to find a way to define the ```SetTDState_Custom``` function which can be called in the python environment.
This function should calculate the density based on temperature and pressure using a *python function*. 


You can modify the ```TestFluidModel.cpp``` and ```TestFluidModel.hpp``` files according to your ideas. Then, run 
the follwing commands in order to convert the C++ source code into a python module:
```
swig -c++ -python Test_Function.i
g++ -O2 -fPIC -c TestFluidModel.cpp
g++ -O2 -fPIC -c Test_Function_wrap.cxx -I/usr/include/python3.8
g++ -shared Test_Function.o Test_Function_wrap.o -o _Test_Function.so
g++ -shared TestFluidModel.o Test_Function_wrap.o -o _Test_Function.so
```

It could be that the ```/usr/include/python3.8``` path is not present on your machine. In that case, locate the 
```Python.h``` file on your machine and use the path to this file instead.

Now the python class should be ready to use. The ```run_python_test.py``` script describes a routine within the python
environment that would be similar to what would be used within the SU2 python wrapper. The goal is to get a version of the 
commented section (lines 18-20) to work, where you pass the ```customPTfunction``` to the ```TestFluidModel```, where it's 
used to compute the density based on pressure and temperature.

Good luck!