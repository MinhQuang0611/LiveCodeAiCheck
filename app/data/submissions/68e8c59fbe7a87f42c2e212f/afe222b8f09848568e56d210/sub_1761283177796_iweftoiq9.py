n = int(input())
score = [x for x in input().split()]
avg = 0
for i in score:
    avg += float(i)
avg /= n
print("%.2f" % avg)
if avg < 4:
    print("Yeu")
elif avg < 5.5:
    print("Trung binh")
elif avg < 7:
    print("Kha")
elif avg < 8.5:
    print("Gioi")
else:
    print("Xuat sac")