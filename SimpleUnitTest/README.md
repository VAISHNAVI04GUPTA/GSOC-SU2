# Using Pybind11 to embed a Python function in C++ code 

The files in this folder can be used to compile C++ code files into Python modules. 

Before you begin, ensure you have ```Pybind11``` installed.

The C++ code describes a simple fluid model that uses the ideal gas law to compute the pressure, temperature, and density.
This code is compiled to a ```TestFluidModel``` class, which can be accessed in Python, similarly to the ```Driver``` class 
in the SU2 python wrapper. 

The goal is to find a way to define the ```SetTDState_Custom``` function, which can be called in the Python environment.
This function should calculate the density based on temperature and pressure using a *python function*. This has been achieved by creating a module named '''density''' , importing that module in a Python file and using it to utilize the defined functions.


Run the following commands to convert the C++ source code into a Python module:
```
mkdir build
cd build
cmake ..
make 
cd ..
python3 run_python_test.py
```

It could be that the ```/usr/include/python3.8``` path is not present on your machine. In that case, locate the 
```Python.h``` file on your machine and use the path to this file instead.

Now, the Python class should be ready to use. The ```run_python_test.py``` script describes a routine within the Python
environment that would be similar to what would be used within the SU2 python wrapper. The goal was to get a version of the 
commented section (lines 18-20) to work, where we pass the ```function``` to the ```TestFluidModel```, where it's 
used to compute the density based on pressure and temperature.

Thank you!
