n=int(input())
for _ in range (n):
    s=input()
    if s[0]==s[len(s)-1]:
        print("YES")
    else:
        print("NO")