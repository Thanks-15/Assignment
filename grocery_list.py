

Budget = int(input("Enter Your Budget: "))
products = []
quantits = []
prices = [] 
c=1

while (True):
	print("1.Add an item ")
	print("2.Exit")
	Choice = int(input("Enter Your Choice : "))
	print()
	if (Choice==1):
		product = input("Enter  Product : ")
		products.append(product)
		quantity = (input("Enter  Quantity : "))
		quantits.append(float(quantity[0]))
		price = int(input("Enter  Price : "))
		print()
		prices.append(price)
		if ((price)<=Budget):
			print(f"Amount Left : {Budget-(price)}")
			print()
		else:
			print(f"Can't buy the product {product} because budget Left is {Budget}")
			print()
		Budget = Budget-(price)
	elif (Choice==2):
			for i in range(len(prices)):
				if (prices[i]<=Budget and c==1):
					print(f"Budget of {Budget} can buy you {products[i]}")
					print()
					c+=1
			print("GROCERY LIST is: ")
			print("Product name  Quantity  Price")
			for i in range(len(prices)):  
				print(products[i] ,"\t\t", quantits[i], "kg", "\t" , prices[i])
			break

   