def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

def seed_exp(a, b):
	acc = 1
	for i in str((bin(b))):
		if i == '1':
			acc = acc ** 2 * a
		else:
			acc = acc ** 2
	return acc

def seed_exp_mod(a, b, M):
	acc = 1
	for i in str((bin(b))):
		if i == '1':
			acc = acc ** 2 * a % M
		else:
			acc = acc ** 2 % M
	return acc

def phi(n):
	amount = 0
	for k in range(1, n + 1):
		if gcd(n, k) == 1:
			amount += 1

	return amount

def xgcd(b, n):
	x0, x1, y0, y1 = 1, 0, 0, 1
	while n != 0:
		q, b, n = b // n, n, b % n
		x0, x1 = x1, x0 - q * x1
		y0, y1 = y1, y0 - q * y1
	return b, x0, y0


if __name__ == '__main__':
	print(gcd(72138538, 7382798457394))
	print(seed_exp(7, 103))
	print(seed_exp_mod(7, 103, 53))
	p = 89
	q = 113
	n = phi(p * q)
	d = 299
	print(gcd(d, phi(n)))
	_, e, _ = xgcd(d, phi(n))
	enc = seed_exp_mod(1337, e, n)
	print(seed_exp_mod(enc, d, n))

