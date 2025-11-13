def daonguoc(s: str) -> str:
    return " ".join(s.split()[::-1])
s = input()
print(daonguoc(s))