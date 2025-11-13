def main():
    s = input()
    for i in range(len(s)):
        if s[i] == "4" or s[i] == "7":
            continue
        else:
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    print(main())