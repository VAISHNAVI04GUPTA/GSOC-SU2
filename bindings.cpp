#include <pybind11/pybind11.h>
#include "testfluidmodel.hpp"

namespace py = pybind11;
PYBIND11_MODULE(density,m){
    py::class_<TestFluidModel>(m, "TestFluidModel")
        .def(py::init<>())
        .def("SetTDState_Custom",&TestFluidModel::SetTDState_Custom,"A function performing arithmetic calculation to find the density.",
             py::arg("P_in"),py::arg("T_in"),py::arg("func"));
}