a = input()
chuoi = [a[i:i+2] for i in range(0, len(a), 2)]
sapxep = sorted(set(chuoi))
print(sapxep)