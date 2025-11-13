a = int(input())
b = int(input())
c = int(input())
if a <= b and a <= c:
    ln = a
elif b <= a and b <= c:
    ln = b
else:
    ln = c
print (ln)