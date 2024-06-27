# Using Pybind11 for calling a class method defined in C++ file using Python code
* created a class(Calculation) in the header file
* defined function arithmetic which has a function body in the cpp file wherein we are using a python function also.
* A Python file has a function definition where we are taking an integer as an input argument, which is the output from multiply fxn in the cpp file, and calculating its factorial.
* The whole binding is done through a module named calc, which has to be defined in a separate cpp file (bindings.cpp)

## In order to run and compile this test case, run the following commands:
* mkdir build
* cd build
* cmake ..
* make
* cd ..
* python3 test.py
