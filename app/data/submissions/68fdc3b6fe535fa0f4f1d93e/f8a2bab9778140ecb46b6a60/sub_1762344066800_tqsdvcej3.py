m = int(input())
n = list(map(int, input().split()))
b = max(n)
c = min(n)
while b in n :
    n.remove(b)
while c in n :
    n.remove(c)

avg = sum(n)/len(n)
print(int(avg))