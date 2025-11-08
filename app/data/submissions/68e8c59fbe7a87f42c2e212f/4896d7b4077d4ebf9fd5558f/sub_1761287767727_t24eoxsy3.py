n=float(input())
scores=list(map(float,input().split()))
def trungBinh(scores,n):
    tong=sum(scores)
    trungbinh=tong/n
    return (round(trungbinh,2))
tb=trungBinh(scores,n)
if (tb)>=8.5:
  print(Xuất sắc)
else if 7<=(tb)<8.5:
 print(Giỏi)
else if 5.5<=(tb)<7:
 print(Trung bình)
else:
    print(Yeu)