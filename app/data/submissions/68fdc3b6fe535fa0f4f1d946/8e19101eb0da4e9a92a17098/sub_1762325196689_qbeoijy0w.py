def chuan_hoa(line):
    n = ""
    for ch in line:
        if ch.isalpha() or ch.isdigit() or ch in [' ', ',', ':']:
            n += ch
    result = ""
    check = True
    for ch in n:
        if ch.isalpha():
            if check:
                result += ch.upper()
                check = False
            else:
                result += ch.lower()
        else:
            result += ch
            if ch in [' ', ',', ':']:
                check = True
    return result
while True:
    try:
        line = input()
        print(chuan_hoa(line))
    except EOFError:
        break