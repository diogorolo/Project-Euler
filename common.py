from math import sqrt,ceil

def isPrime(num):
	for i in range(2,int(ceil(sqrt(num)))+1):
		if num % i == 0:
			return False
	return True
	
	