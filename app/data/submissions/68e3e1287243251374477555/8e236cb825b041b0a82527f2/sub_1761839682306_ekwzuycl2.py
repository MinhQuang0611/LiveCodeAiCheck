import math

def safe_division(a, b):
    if a == 0 and b == 0:
        return math.nan
    elif b == 0:
        return math.inf if a > 0 else -math.inf
    else:
        return a / b

print(safe_division(float(input()), float(input())))