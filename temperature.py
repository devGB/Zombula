print("This program converts Fahrenheit to Celsies")
#print("Type in a temperature in Fahrenheit: ",end="")
#fahrenheit = float(input() )

#print("That is", celsius, "degrees Celsius")
for i in range(-60,140):
    fahrenheit = i
    celsius = (fahrenheit - 32) * 5.0 / 9
    print(i, " fahrenheit ", celsius, " celsius")
      
