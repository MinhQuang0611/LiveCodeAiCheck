def compress_string(s):
    result = ''
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += str(count) + s[i - 1]
            count = 1
    result += str(count) + s[-1]
    return result

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(compress_string(s))
