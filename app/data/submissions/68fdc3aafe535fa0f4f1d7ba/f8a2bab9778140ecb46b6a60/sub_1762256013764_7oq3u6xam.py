m = int(input())
for _ in range(m):
    n = input()
    a = []
    for i in range(2,len(n)):
        if n[i] == n[i-2]: 
            print("YES")
            break
        else:
            print("NO")
            break