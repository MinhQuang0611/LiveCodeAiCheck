def is_valid(arr):
    parts = arr.split('.')
    if len(parts) != 4:
        return False
    for i in parts:
        if not i.isdigit():
            return False 
        if not (0 <= int(i) <= 255):
            return False
    return True
t = int(input())
for _ in range(t):
    arr = input()
    if is_valid(arr):
        print("YES")
    else:
        print("NO")

