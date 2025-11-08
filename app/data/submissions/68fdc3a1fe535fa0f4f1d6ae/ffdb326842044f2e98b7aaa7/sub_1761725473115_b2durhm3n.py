t = int(input())

while t > 0:
    nums = int(input())

    while nums % 7 != 0:
        string = str(nums)

        new_nums = int(string[::-1])

        nums += new_nums

    print(nums)
    t -= 1