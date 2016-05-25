def brent(f, x0):
	power = lam = 1
	tortoise = x0
	hare = f(x0)
	while tortoise != hare:
		if power == lam:
			tortoise = hare
			power *= 2
			lam = 0
		hare = f(hare)
		lam += 1

	mu = 0
	tortoise = hare = x0
	for i in range(lam):
		hare = f(hare)

	while tortoise != hare:
		totoise = f(tortoise)
		hare = f(hare)
		mu += 1

	return lam, mu
