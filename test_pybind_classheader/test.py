# test.py

import calc 


def factorial(a):
    l=[]
    if not isinstance(a, int):
        raise TypeError("Expected an integer input")
    f=1
    for i in range(1,a):
        if(a%i==0):
            l.append(i)


    
    return l[-1]

ins3 = calc.Calculation()
result=ins3.arithmetic(4,6,factorial)
print("Highest factor:",result)
