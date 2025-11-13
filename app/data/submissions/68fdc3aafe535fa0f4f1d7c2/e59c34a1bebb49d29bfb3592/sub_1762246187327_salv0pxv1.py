n = input().strip()
total = [n[i:i+2] for i in range(0,len(n),2)]
t = sorted(set(total))
print(' '.join(t))