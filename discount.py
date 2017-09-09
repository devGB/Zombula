price = float(input('Enter the purchase price: '))

if price <= 10:
	print("10% disount applied " + str(price*0.9))
if price > 10:
	print("20% discount applied " + str(price*0.8))
