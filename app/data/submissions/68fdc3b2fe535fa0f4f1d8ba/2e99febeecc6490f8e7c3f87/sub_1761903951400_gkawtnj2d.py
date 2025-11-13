def check_sum(num_str):
    s = 0
    for i in range(len(num_str)):
        s += int(num_str[i])
    return s
def check_nature(num_str):
    if len(num_str)<2:
        return False
    check = True
    for i in range(len(num_str)):
        if i>0 and abs(int(num_str[i]) - int(num_str[i-1])) != 2:
            check = False
            break
    return check


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        line = input()
        arr.append(line)
    for i in arr:
        if check_sum(i) %10 == 0 and check_nature(i):
            print("YES")
        else:
            print("NO")


