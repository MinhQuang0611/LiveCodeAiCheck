def main():
    s = input()
    for i in range(len(s)-1):
        if s[i+1] < s[i]:
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    print(main())