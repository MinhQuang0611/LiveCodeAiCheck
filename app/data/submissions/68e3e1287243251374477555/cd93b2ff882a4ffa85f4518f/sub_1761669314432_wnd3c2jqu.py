a =input()
b = input()
a = float(a)
b = float(b)
if b == 0:
    print("Division by zero")
else:
    r = a / b
    if r == float('inf'):
        print("inf")
    elif r == float('-inf'):
        print("-inf")
    elif r != r:
        print("nan")
    else:
        print(float(r))