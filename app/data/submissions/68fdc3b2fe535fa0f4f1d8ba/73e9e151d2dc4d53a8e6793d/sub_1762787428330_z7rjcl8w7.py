def main():
    tong = 0
    s = input()
    for i in range(len(s)-1):
        tong += int(s[i])
        if abs(int(s[i]) - int(s[i+1])) != 2:
            print("NO")
            return
    tong += int(s[-1])
    if tong % 10 == 0:
        print("YES")
    else: 
        print("NO")
    return

t = int(input())
for _ in range(t):
    main()