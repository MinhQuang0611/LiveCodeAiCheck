n = input()
st = n[::-1]

arr = [st[i:i+3] for i in range(0, len(st), 3)]
kq = ','.join(arr)
print(kq[::-1])



