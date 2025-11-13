n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if i != max(a) and i != min(a):
        b.append(i)
print(int(sum(b)/len(b)))
