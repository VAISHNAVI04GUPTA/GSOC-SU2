// calculation.cpp
#include "calculation.hpp"
#include <pybind11/embed.h>
#include <iostream>

namespace py = pybind11;


int Calculation::arithmetic(int x,int y, pybind11::function func){
    int prod=x*y;
    // Ensure that the function is called and cast properly
    try {
        int result = func(prod).cast<int>();  // Ensure the Python function returns an int
        return result;
    } catch (pybind11::cast_error &e) {
        // Handle the cast error
        throw std::runtime_error("Unable to cast Python function return to int: " + std::string(e.what()));
    }
}


