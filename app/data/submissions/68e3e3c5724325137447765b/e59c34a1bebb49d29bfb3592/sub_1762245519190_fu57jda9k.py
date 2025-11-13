n = input().strip()
if n[0] == "-":
    n = n[1:]
total = sum(int(ch) for ch in n)    
print(total)