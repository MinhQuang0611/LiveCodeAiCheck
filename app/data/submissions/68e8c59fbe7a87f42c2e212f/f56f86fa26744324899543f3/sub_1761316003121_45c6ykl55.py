n=int(input())
a=list(map(float,input().split()))
b=sum(a)/n
print(f"{b:.2f}")
if b>=8.5:print("Xuat sac")
elif b>=7:print("Gioi")
elif b>=5.5:print("Kha")
elif b>=4:print("Trung binh")
else:print("Yeu")