def prob1():
	val = 0
	for i in range(1000):
		if i%3 == 0 or i%5 == 0:
			val = val + i
			
	return val

print(prob1())