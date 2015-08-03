def prob4():
	num1 = 999
	num2 = 999
	maxVal = -1
	while True:
		curVal = num1*num2
		if str(curVal) == str(curVal)[::-1]:
			if curVal > maxVal:
				maxVal = curVal
				
		if(num1 == 100):
			num1 = 999
			num2 = num2-1
		else:
			num1 = num1-1
			
		if num1 == 100 and num2 == 100:
			break
			
	return maxVal
	
print(prob4())