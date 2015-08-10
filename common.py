from math import sqrt,ceil

def isPrime(num):
	if num == 1: # 1 is not prime
		return False
	if num < 4: # 2 and 3 are prime
		return True
	if num % 2 == 0: # even numbers bigger than 2 are not prime
		return False
	if num % 3 == 0: # if the number is divisible by 3 is not prime
		return False
	f = 5 # we've already test up to #4
	r = int(ceil(sqrt(num))) # a prime number can be checked by trial test up to sqrt(n)
	while f <= r:
		if num % f == 0:
			return False
		if num % (f+2) == 0:
			return False
		f += 6 # a prime is always is the form 6k +- 1
	return True
	
	