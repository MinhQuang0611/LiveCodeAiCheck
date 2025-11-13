n = input().strip()
if n[0] != "6":
    print("NO")
elif not all(ch in "68" for ch in n):
    print("NO")
elif "888" in n:
    print("NO")
else:
    print("YES")