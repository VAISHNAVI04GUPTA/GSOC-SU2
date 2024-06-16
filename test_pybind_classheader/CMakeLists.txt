cmake_minimum_required(VERSION 3.10)
project(calc_example)
set(CMAKE_PREFIX_PATH "~/.local/lib/python3.8/site-packages/pybind11/share/cmake/pybind11")

set(CMAKE_CXX_STANDARD 14)
include_directories(/usr/include/python3.8)
link_directories(/usr/lib/python3.8/config-3.8-x86_64-linux-gnu)

find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED)

include_directories(${pybind11_INCLUDE_DIRS})
include_directories(${Python3_INCLUDE_DIRS})

pybind11_add_module(calc bindings.cpp calculation.cpp)
set_target_properties(calc PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/..)