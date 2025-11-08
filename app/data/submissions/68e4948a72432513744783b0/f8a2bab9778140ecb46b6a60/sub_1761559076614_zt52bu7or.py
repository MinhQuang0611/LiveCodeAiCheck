def ham1(n):
    a = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
            a.append(n)
        elif n % 2 != 0:
            n = (n * 3) + 1
            a.append(n)
    b = ' '.join(map(str, a))
    return b
if __name__ == '__main__':
    n = int(input())
    print(ham1(n))