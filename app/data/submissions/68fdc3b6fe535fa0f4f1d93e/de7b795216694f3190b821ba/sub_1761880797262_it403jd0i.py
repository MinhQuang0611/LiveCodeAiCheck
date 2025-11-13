from functools import reduce
b=int(input())
a=list(input().split())
a.sort()
daylucsau=a[1:-1:1]
h=len(daylucsau)
#print(daylucsau)
tongcacsotrongday = reduce(lambda x, y: int(x) + int(y) , daylucsau)  # Tính tổng các phần tử trong List
print(tongcacsotrongday/h)  # Tính trung bình cộng các phần tử trong List)