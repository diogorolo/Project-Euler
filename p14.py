
def prob11():
	bestNum = -1
	maxCounter = -1
	numsSet = set()
	for num in range(1,1000000):
		initialNum = num
		counter = 1
		while num != 1:
			if num %2 == 0:
				num = num / 2
			else:
				num = 3*num + 1
			counter = counter + 1
		if counter > maxCounter:
			maxCounter = counter
			bestNum = initialNum
	return bestNum

print(prob11())
