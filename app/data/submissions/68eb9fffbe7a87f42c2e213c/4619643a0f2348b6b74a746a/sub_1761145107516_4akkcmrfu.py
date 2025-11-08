try:
 a,b = map(int,input().split())
 tong = a + b
 print(tong)
except ValueError:
    pritn("Vui lòng chỉ nhập số nguyên!")