def main():
    digits = list(map(int, input().split()))
    digits[-1] += 1
    if digits[-1] == 0:
        print(0)
    elif digits[-1] == 10:
        print(1)
    print(*digits)
    pass

if __name__ == "__main__":
    main()