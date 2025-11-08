def chuoi_(string):
    dem = 0
    for _ in range(0, len(string) + 1):
        if string[_:_ + 1] == 'u' or string[_:_ + 1] == 'U':
            dem += 1
        elif string[_:_ + 1] == 'i' or string[_:_ + 1] == 'I':
            dem += 1
        elif string[_:_ + 1] == 'o' or string[_:_ + 1] == 'O':
            dem += 1
        elif string[_:_ + 1] == 'a' or string[_:_ + 1] == 'A':
            dem += 1
        elif string[_:_ + 1] == 'e' or string[_:_ + 1] == 'E':
            dem += 1
    return dem

if __name__ == '__main__':
    string = input()
    print(chuoi_(string))