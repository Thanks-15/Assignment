
def pystar(num):
	count = 2*num -2 
	for i in range(0,num):
		for j in range(0,count):
			print(end=" ")
		count -=2

		for x in range(0,i+1):
			print("*", end = " ")
		print("\r")

num = 5
pystar(num)


