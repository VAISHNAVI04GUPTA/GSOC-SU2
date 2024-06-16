#include <pybind11/pybind11.h>
class Calculation
{

public:
    
    int arithmetic(int x,int y,pybind11::function func);
};


