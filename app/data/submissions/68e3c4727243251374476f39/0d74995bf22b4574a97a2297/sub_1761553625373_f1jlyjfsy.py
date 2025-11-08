s = input()
so = s.strip('[]').split(',')
f = [int(i) for i in so]
f = [x ** 2 for x in f]
s = str(f).replace(" ", "")
print(s)