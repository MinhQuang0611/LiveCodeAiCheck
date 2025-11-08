n = int(input())
b = input()
c=b.split(' ')
d = [float(num) for num in c]
average=sum(d)/n
averagestring = f"{average:.2f}"
print(averagestring)
if average>=8.5 and average <=10:
    print("Xuat sac")
if 7<=average<8.5:
    print("Gioi")
if 5.5<=average<7:
    print("Kha")
if 4<=average<5.5:
    print("Trung binh")
if 0<average<4:
    print("Yeu")