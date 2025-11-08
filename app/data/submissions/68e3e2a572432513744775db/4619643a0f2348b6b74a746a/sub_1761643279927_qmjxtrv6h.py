try:
 n = int(input())
 m = list(map(float,input().split()))
 if n == len(m):
  total = sum(m)
  average = total/n
  print(average)
 elif n!= len(m):
  print("Số lượng số thực không khớp với n.")
except ValueError:
  print("Đã xảy ra lỗi: Vui lòng nhập số nguyên cho n và n số thực cho danh sách.")