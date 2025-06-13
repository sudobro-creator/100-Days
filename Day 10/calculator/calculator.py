from ctypes import HRESULT
from difflib import restore

from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

adding = add
# print(adding(4, 3))


def subtract(n1, n2):
    return n1 - n2

subtracting = subtract

def multiply(n1, n2):
    return n1 * n2

multiplication = multiply

def divide(n1, n2):
    return n1 / n2

division = divide

first_num = int(input("What is the first number: "))
signs = {"+", "-", "*", "/"}

print(signs)
math_sign = input("Pick an operator: ")
next_num = int(input("What is the next number: "))

restart = True
while restart:
    if math_sign == "+":
        result = adding(n1=first_num, n2=next_num)
        print(result)
    elif math_sign == "-":
        result = subtracting(first_num, next_num)
        print(result)
    elif math_sign == "*":
        result = multiplication(first_num, next_num)
        print(result)
    elif math_sign == "/":
        result = division(first_num, next_num)
        print(result)

    stop = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or 'x' to stop calculation").lower()
    if stop == "n":
        print("\n" * 100)
    elif stop == "x":
        restart = False