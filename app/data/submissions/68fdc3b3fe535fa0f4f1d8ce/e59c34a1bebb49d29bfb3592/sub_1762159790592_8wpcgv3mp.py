n = int(input())
arr = []
x = 0
for _ in range(n):
    t = input()
    if t not in arr and t != 0:
        arr.append(t)
        x += 1
print(x)
