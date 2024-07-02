#include <pybind11/pybind11.h>
class TestFluidModel 
{
private:
    double P; // pressure value
    double T; // temperature value
    double rho; // density value

    double R_gas; // fluid gas constant
public:

    
    //TestFluidModel(double P_in, double T_in, double rho_in) ;
    TestFluidModel() = default;

    void SetTDState_PT(double P, double T);

    void SetTDState_Prho(double P, double rho);

    void SetTDState_Trho(double T, double rho);

    double SetTDState_Custom(double P, double T, pybind11::function func);
    
    double GetTemperature() const {return T;}
    double GetPressure() const {return P;}
    double GetDensity() const {return rho;}
    
};