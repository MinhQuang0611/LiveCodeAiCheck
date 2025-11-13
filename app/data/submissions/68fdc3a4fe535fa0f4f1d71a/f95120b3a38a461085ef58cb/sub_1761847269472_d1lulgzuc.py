a = input().strip()
b = input().strip()
p = int(input().strip())
index = p - 1
new = a[:index] + b + a[index:]
print(new)