def pypattern(n):

	asci_value = 65

	for i in range(0,n):
		for j in range(0,i+1):
			char = chr(asci_value)
			print(char, end = " ")
			asci_value +=1
		print("\r")

n = 5
pypattern(n)
