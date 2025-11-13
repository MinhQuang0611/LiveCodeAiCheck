t = int(input())
for _ in range(t):
    s = input()
    a = 1
    b = 0
    for index, char in enumerate(s):
        digit = int(char)
        position = index + 1
        if position % 2 != 0:
            if digit != 0:
                a *= digit 
        else: 
            b += digit 
    print(f"{a} {b}")


    

