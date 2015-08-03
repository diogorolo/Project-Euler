def sumN(N):
	return N*(N+1)/2
	
def prob6():
	N = 100
	totalN = sumN(N)
	totalNSquared = totalN*totalN
	squareN = 0
	for i in range(1,N+1):
		squareN = squareN + i*i
	return totalNSquared - squareN
	
print(prob6())