

def prob9():
	
	for a in range(1,999):
		for b in range(1,999):
			for c in range(1,999):
				if a+b+c > 1000:
					break
					
				if a*a + b*b == c*c and a+b+c == 1000 :
					return a*b*c
					

print(prob9())