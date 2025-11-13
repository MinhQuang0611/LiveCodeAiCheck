a = int(input())
n = list(map(int, input().split()))
b = []
for i in range(1, max(n)+1):
    if i not in n:
        b.append(i)
        print(i)
if len(b)==0:
    print("Excellent!")