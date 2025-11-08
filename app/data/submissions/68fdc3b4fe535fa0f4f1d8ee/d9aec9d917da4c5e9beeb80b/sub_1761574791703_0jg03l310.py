t = int(input())  
for i in range(t):
    s = input().strip()
    hople = True
    for a in s:
        if a not in ["4", "7"]:
            hople = False
            break
    if hople:
        print("YES")
    else:
        print("NO")



