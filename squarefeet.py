l = input("What is the length? ")
w = input("What is the width? ")
a = float(l) * float(w)
priceSqYrd = float(input("What is the price per square yard? "))
print ("Total square feet = "+str(a))
print("Total square yards = "+str(a/9))
print("Total price $" + str(a/9*priceSqYrd))
