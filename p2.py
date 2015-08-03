
def fibProb2(maxNumber):
	i = 1
	iminus1 = 1
	iminus2 = 0
	val = 0

	while i < maxNumber:
		if i % 2 == 0 and i > 1:
			val = val + i
		
		i = iminus1 + iminus2
		iminus2 = iminus1
		iminus1 = i
	return val

def prob2():
	return fibProb2(4000000)
	
print(prob2())