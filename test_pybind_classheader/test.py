# test.py

import calc 


def factorial(a):
    if not isinstance(a, int):
        raise TypeError("Expected an integer input")
    f=1
    for i in range(1,a):
        f=f*i


    return f

ins3 = calc.Calculation()
result=ins3.arithmetic(4,6,factorial)
print("Factors are :",result)
