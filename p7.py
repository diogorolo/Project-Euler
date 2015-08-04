from common import isPrime

def prob7():
	primeList = set()
	i = 2
	while len(primeList) < 10000:
		if isPrime(i):
			primeList.add(i)
		i = i+1

	return max(primeList)

print(prob7())
