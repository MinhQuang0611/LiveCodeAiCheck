n = int(input("Nhập số lượng số nguyên: "))
numbers = [int(x) for x in input(f"Nhập {n} số nguyên cách nhau bởi dấu cách: ").split()] 
gtnn=min(numbers)
while gtnn in numbers:
    numbers. remove(gtnn)
gtln=max(numbers)
while gtln in numbers:
    numbers . remove(gtln)
if len(numbers)!=0:
    trungbinh= sum(numbers)/len(numbers )
print(trungbinh)
