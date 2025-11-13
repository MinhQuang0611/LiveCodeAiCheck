t = int(input())
for _ in range(t):
    s = input()
    a = 1
    b = 0
    has_nonzezo = False 
    for index, char in enumerate(s):
        digit = int(char)
        position = index + 1
        if position % 2 != 0:
            if digit != 0:
                a *= digit 
                has_nonzezo = True
        else: 
            b += digit 
    if not has_nonzezo:
        a = 0
    print(f"{a} {b}")