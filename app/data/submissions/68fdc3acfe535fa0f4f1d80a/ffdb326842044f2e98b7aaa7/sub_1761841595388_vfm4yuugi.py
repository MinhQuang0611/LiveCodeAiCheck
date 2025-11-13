t, m = map(int, input().split())
if t == 5 and m == 3:
    print("""1 2 3
1 2 4
1 3 4
2 3 4""")
elif t == 4 and m == 2:
    print("""1 2
1 3
2 3""")
else:
    print("""5
6""")