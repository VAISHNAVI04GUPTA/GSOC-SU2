# CMakeLists.txt

cmake_minimum_required(VERSION 3.4...3.18)
project(embed_python)


set(CMAKE_PREFIX_PATH "~/.local/lib/python3.8/site-packages/pybind11/share/cmake/pybind11")

find_package(pybind11 REQUIRED) # Find pybind11

add_executable(embed_python embed_python.cpp) # Create executable

target_link_libraries(embed_python PRIVATE pybind11::embed) # Link pybind11
