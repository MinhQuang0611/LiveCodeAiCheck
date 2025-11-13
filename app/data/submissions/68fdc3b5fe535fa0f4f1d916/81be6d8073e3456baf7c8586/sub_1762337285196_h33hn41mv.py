import sys
def solve_aria_compression():    
    try:
        t_str = sys.stdin.readline().strip()
        if not t_str:
            return
        t = int(t_str)
    except:
        return
    for _ in range(t):
        s = sys.stdin.readline().strip()
        result = ""
        count = 1
        if len(s) == 0:
            print("")
            continue
        current_char = s[0]
        for i in range(1, len(s)):
            if s[i] == current_char:
                count += 1
            else:
                result += str(count) + current_char
                current_char = s[i]
                count = 1
        result += str(count) + current_char
        print(result)
solve_aria_compression()