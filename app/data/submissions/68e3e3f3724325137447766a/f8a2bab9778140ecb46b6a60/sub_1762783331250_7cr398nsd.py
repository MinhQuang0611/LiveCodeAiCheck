n = input()
c = int(n)
ngc = 0
for i in range(len(n)):
    ngc = ngc*10 + c%10
    c //= 10
print(ngc) 