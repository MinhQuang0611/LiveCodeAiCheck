a = input().strip()
b = [a[i:i+2] for i in range(0,len(a),2)]
c = sorted(set(b))
print(*c)