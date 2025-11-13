m = input()
i = list(map(int,input().split()))
a = max(i)
b = min(i)
while a in i:
    i.remove(a)
while b in i:
    i.remove(b)

tb= int(sum(i)/len(i))
print(tb)