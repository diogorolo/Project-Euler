def prob5():
	curVal = 20
	found = False
	while not found:
		for i in range(11,20)[::-1]:
			if curVal  % i != 0:
				curVal = curVal + 20
				break
		else:
			found = True
	return curVal
	
	
print(prob5())