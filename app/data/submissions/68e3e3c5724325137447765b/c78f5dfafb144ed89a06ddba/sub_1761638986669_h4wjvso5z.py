n = str(input())
if n.find("-") != -1:
    n = n.lstrip("-")
a= list(n)
b = [int(item) for item in a]
total = 0
for i in range(0, len(b)):
    total += b[i]
print(total)