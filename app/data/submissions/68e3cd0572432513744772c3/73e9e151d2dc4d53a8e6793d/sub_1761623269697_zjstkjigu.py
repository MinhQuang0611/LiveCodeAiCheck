def main():
    n = int(input())
    s = str(n)
    for i in range(len(s)):
        c = s.count(s[i])
        if c > 1:
            return("true")
    return("false")
print(main())
        
