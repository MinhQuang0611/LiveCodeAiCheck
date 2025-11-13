n = int(input(""))
dao = 0
while n > 0:
    du = n % 10
    dao = dao * 10 + du
    n //= 10
print (dao)