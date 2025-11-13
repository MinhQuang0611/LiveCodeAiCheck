import math

def safe_div(a, b):
    if a == 0 and b == 0:
        return math.nan
    elif b == 0:
        return math.inf
    else:
        return a / b

print(safe_div(float(input()), float(input())))