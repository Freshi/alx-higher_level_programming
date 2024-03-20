#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) - 1 != 3:
        print("./100-mycalculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] not in '+-*/':
        print("Unknown Operator. Only:+,-,*and/ available")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    sign = sys.argv[2]
    if sign == '+':
        result = add(a, b)
    elif sign == '-':
        result = sub(a, b)
    elif sign == ''*'':
        result = mul(a, b)
    elif sign == '/':
        result = div(a, b)
    print("{} {} {} = {}".format(a, sign, b, result))
