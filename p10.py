from common import isPrime

def prob10():
	maxNumber = 2000000
	primeList = set()
	for i in range(2,maxNumber+1):
		if isPrime(i):
			primeList.add(i)

	return sum(primeList)

print(prob10())
