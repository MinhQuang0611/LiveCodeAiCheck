a = int(input())
a = str(a)
b = []
if len(a)<2:
    print('0')
else:
    for i in range(len(a)):
        c = int(a[i-1])*int(a[i])
        b.append(c)
    print(max(b))