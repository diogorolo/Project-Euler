
def fibProb25(numDigits):
	i = 1
	iminus1 = 1
	iminus2 = 0
	counter = 1
	while len(str(i)) != numDigits :	
		i = iminus1 + iminus2
		iminus2 = iminus1
		iminus1 = i
		counter += 1
	return counter

def prob25():
	return fibProb25(1000)
	
print(prob25())