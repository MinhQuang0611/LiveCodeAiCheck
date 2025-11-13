s = input().strip()
lan = 0
while len(s)>1:
    total = sum(int(digit) for digit in s)
    s = str(total)
    lan+=1
print(lan)