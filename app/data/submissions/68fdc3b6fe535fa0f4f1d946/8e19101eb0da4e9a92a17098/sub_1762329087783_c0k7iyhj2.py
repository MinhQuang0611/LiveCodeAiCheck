def chuan_hoa(line):
    n = ""
    for ch in line:
        if ch.isalpha() or ch.isdigit() or ch in [' ', ',', ':']:
            n += ch
        else:
            if len(n) > 0 and n[-1] != ' ':
                n += ' '
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
    result = ' '.join(result.split())
    return result
while True:
    try:
        line = input()
        print(chuan_hoa(line))
    except EOFError:
        break
