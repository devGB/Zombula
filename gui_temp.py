import easygui

easygui.msgbox("This program converts Fahrenheit to Celsies ")

#print("This program converts Fahrenheit to Celsies")

fahrenheit = easygui.integerbox("Type in a temperature in Fahrenheit:  ", lowerbound = -9999999, 
        upperbound = 999999999)

#print("Type in a temperature in Fahrenheit: ",end="")
#fahrenheit = float(input() )
celsius = (fahrenheit - 32) * 5.0 / 9
easygui.msgbox("That is "+ str("{0:.2f}".format(round(celsius,2)))+ " degrees Celsius")
#print("That is", celsius, "degrees Celsius")

#for i in range(-60,140):
#    fahrenheit = i
#    celsius = (fahrenheit - 32) * 5.0 / 9
#    print(i, " fahrenheit ", celsius, " celsius")
      
