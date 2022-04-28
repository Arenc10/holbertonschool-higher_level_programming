#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    
    length = len(argv)
    opera = ["+", "-", "*", "/"]

    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in opera:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    op1 = int(argv[1])
    opera = argv[2]
    op2 = int(argv[3])
    if opera == "+":
        print(f"{op1} {opera} {op2} = {add(op1, op2)}")
    if opera == "-":
        print(f"{op1} {opera} {op2} = {sub(op1, op2)}")
    if opera == "*":
        print(f"{op1} {opera} {op2} = {mul(op1, op2)}")
    if opera == "/":
        print(f"{op1} {opera} {op2} = {div(op1, op2)}")
    
