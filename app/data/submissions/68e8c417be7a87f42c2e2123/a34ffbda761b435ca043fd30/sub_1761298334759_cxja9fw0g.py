a, b, c = map(int, input().split())
if a == b and c>b:
    print(c)
elif  a == c and c < b:
    print(b)
elif b == c and a > c:
    print(a)
elif a>b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif  c > a and c > b:
    print(c)
else :
    print('Không có gí trị lớn nhất')