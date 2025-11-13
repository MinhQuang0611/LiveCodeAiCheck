n = int(input())
m = list(map(int , input().split()))
m = sorted(set(m))
for i in range(len(m)-1):
    if m[i] + 1 != m[i+1]:
        print(m[i]+1)
        exit()
print("Excellent!")