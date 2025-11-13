def main():
    digits = list(map(int, input().split()))
    digits[-1] += 1
    print(*digits)
    pass

if __name__ == "__main__":
    main()