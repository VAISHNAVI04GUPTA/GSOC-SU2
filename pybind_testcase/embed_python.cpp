// embed_python.cpp

#include <pybind11/embed.h>
#include <iostream>

namespace py = pybind11;

int main() {
    py::scoped_interpreter guard{}; // Start the interpreter and keep it alive
    
    py::module sys = py::module::import("sys");
    sys.attr("path").attr("append")(".");
    
    try {
        
        py::module example = py::module::import("example"); // Import the Python module
        py::object result = example.attr("multiply")(2, 3); // Call the Python function
        std::cout << "Result: " << result.cast<int>() << std::endl; // Print the result
    } catch (const py::error_already_set& e) {
        std::cerr << "Python error: " << e.what() << std::endl;
    }

    return 0;
}

