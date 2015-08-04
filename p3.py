from common import isPrime
from math import ceil,sqrt

def prob3():
	number = 600851475143
	
	primeList = set()
	primeFactors = set()
	for i in range(2,int(ceil(sqrt(number)))+1):
		if i in primeList or isPrime(i):
			primeList.add(i)
			if number % i == 0:
				primeFactors.add(i)
	return max(primeFactors)
	
print(prob3())
