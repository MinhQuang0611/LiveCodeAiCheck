def a(n):
    total=0
    for i in str(abs(n)):
        total+=int(i)
    return total
num=int(input())
print(a(num))