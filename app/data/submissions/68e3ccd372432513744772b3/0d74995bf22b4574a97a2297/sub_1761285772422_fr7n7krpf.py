a, b = map(int, input().split())
f0 = 1
f1 = 1
sum = 0
while f0 <= b:
    if f0 >= a and f0 % 2 == 0:
        sum += f0
    f0, f1 = f1, f0 + f1
print(sum)