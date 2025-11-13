import sys

def compress(s: str) -> str:
    if not s:
        return ""
    res = []
    cnt = 1
    prev = s[0]
    for ch in s[1:]:
        if ch == prev:
            cnt += 1
        else:
            res.append(f"{cnt}{prev}")
            prev = ch
            cnt = 1
    res.append(f"{cnt}{prev}")
    return "".join(res)

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    t = int(data[0].strip())
    lines = data[1:]
    # nếu có ít dòng hơn t, bỏ phần thiếu
    for i in range(min(t, len(lines))):
        s = lines[i].strip()
        print(compress(s))

if __name__ == "__main__":
    main()