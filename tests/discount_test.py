import pytest


def calculate_discount(price: float, discount: float):

    if  not (0 <= discount <= 1):
        raise ValueError

    final_price = price * ( 1- discount)
    return final_price

try:
     print(calculate_discount(100, 0.2))
     print(calculate_discount(50, 0))
     print(calculate_discount(200, 1))
     print(calculate_discount(100, -0.1))
     print(calculate_discount(100, 1.5))
except ValueError as e:
    
    print("Value Error")





