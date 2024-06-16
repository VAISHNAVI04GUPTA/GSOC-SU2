#include <pybind11/pybind11.h>
#include "calculation.hpp"

namespace py = pybind11;
PYBIND11_MODULE(calc,m){
    py::class_<Calculation>(m, "Calculation")
        .def(py::init<>())
        .def("arithmetic",&Calculation::arithmetic,"A function performing arithmetic calculation",
             py::arg("x"),py::arg("y"),py::arg("func"));
}
