a = int(input())
for i in range(a):
    b = input()
    kq = ""
    dem = 1
    for j in range(1, len(b)):
        if s[j] == s[j-1]:
            dem += 1
        else:
            kq += str(dem) + s[-1]
            print(kq)
