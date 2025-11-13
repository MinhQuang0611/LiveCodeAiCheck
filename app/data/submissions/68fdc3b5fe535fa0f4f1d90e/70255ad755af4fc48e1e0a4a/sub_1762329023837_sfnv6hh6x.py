t = int(input())

for i in range (0, t):
	n = int(input())
	n_str = str(n)
	t = len(n_str)
	tich = 1
	tong = 0
	if t % 2 == 0:
		while t != 0:
			if t % 2 == 0: tong += n % 10
			else: tich *= n % 10
			n //= 10
			t -= 1
	elif t % 2 != 0:
		while t != 0:
			if t % 2 != 0: tich *= n % 10
			else: tong += n % 10
			n //= 10
			t -= 1
	print(tich, tong)