a = input().strip()
total = [a[i:i+2] for i in range(0,len(a),2)]
b = sorted(set(total))
print(*b)