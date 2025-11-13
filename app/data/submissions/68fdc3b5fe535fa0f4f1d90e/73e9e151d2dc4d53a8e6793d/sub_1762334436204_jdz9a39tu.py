t = int(input())
for _ in range(t):
    s = input()
    _sum = 0
    _mul = 1
    kt = False
    for i in range(len(s)):
        number = int(s[i])
        if (i + 1) % 2 != 0:
            if number != 0:
                _mul *= number
                kt = True
        else:
            _sum += number
    if _mul == 1 and not kt and len(s) > 0:
        _mul = 0
    print(f"{_mul} {_sum}")