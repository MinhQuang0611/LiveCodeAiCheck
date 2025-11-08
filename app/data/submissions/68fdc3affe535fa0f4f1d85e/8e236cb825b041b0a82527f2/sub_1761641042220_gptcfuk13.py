def is_lucky(s):
    if s[0] != "6":
        return False

    eight_cnt = 0
    for c in s:
        if c != "6" and c != "8":
            return False
        
        if c == "8":
            if eight_cnt == 2:
                return False
            else:
                eight_cnt += 1
        else:
            eight_cnt = 0
    return True

print("YES" if is_lucky(input()) else "NO")