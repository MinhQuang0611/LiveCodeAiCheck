t = int(input())
for _ in range(t):
    s = input()
    if len(s) % 2 == 0:
        for i in range(2, len(s)):
            if s[i] != s[i - 2]:
                print("NO")
                break
        else:
            print("YES")
    else:
        print("NO")
