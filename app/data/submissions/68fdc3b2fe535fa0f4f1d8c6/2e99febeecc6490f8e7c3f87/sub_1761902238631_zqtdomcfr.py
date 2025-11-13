def incr_str(num_str):
    check = True
    for i in range(len(num_str)):
        if i > 0 and num_str[i] < num_str[i-1]:
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
        if incr_str(i):
            print("YES")
        else:
            print("NO")
