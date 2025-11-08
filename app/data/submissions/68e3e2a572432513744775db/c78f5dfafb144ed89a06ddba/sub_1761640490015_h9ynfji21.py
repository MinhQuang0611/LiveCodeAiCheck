n = input().split()
if n == []:
    print(float(0))
else:
    m=[int(item) for item in n]
    total = sum(m)
    average = total/len(m)
    print(average)