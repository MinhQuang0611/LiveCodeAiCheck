a=[]
for i in range(3):
    a.append(float(input()))
largest=max(a)
if largest.is_integer():
    print(int(largest))
else:
    print(largest)
