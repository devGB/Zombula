P = input("How many Pennies? ")
N = input("How many Nickels? ")
D = input("How many Dimes? ")
Q = input("How many Quarters? ")

pTot = int(P) * (1/100)
nTot = int(N) * (5/100)
dTot = int(D) * (10/100)
qTot = int(Q) * (25/100)

total = pTot+nTot+dTot+qTot

print("You have $"+str(total))
