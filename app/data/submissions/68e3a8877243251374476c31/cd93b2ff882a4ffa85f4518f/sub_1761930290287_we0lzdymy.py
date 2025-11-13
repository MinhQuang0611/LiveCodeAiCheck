s = input()
s = s.replace(',', ' ')
parts = s.split()
nums = []
for x in parts:
    if x.isdigit() or (x[0] == '-' and x[1:].isdigit()):
        nums.append(int(x))
if len(nums) == 0:
    print("[]")
else:
    check = [0] * 1000001
    for n in nums:
        if n > 0 and n < 1000000:
            check[n] = check[n] + 1

    kq = []
    if len(nums) > 1:            
        for i in range(1, max(nums) + 1):
            if check[i] == 2:
                kq.append(i)
    if len(kq) == 0:
        print("[]")
    else:
        print('[', end='')
        for i in range(len(kq)):
            if i == len(kq) - 1:
                print(kq[i], end='')
            else:
                print(kq[i], end=',')
        print(']', end='')
