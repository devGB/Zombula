
mpg = float(input("how many miles per gallon does your car get?: "))
tanksize = float(input("how big is your gas tank, in gallons?: "))
percentFull = float(input("how full is your gas tank, in percent?: "))
distance = float(input("how many miles till the next gas station?: "))

maxdist = (percentFull*tanksize)*mpg

print("size of tank : "+ str(tanksize))
print("percent of full : "+ str(percentFull))
print("miles per gallon : "+ str(mpg))
print("distance till next gas station : "+ str(distance))
print("The maximun distance you can travel : "+ str(maxdist))
if maxdist>distance:
	print("Keep going yaaaaaah")
else:
	print("Boooooo hoooooo, gas up gassy")
