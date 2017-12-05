import random, easygui

secret = random.randint(1, 99)
guess = 0
tries = 0

easygui.msgbox("""AHOY! I'm the dread pirate Roberts, and I have a secret!
It is a number from 1 to 99. I,ll give you 6 tries. """)

while guess !=secret and tries<10:
    guess = easygui.integerbox("What's yer guess, matey? ")
    if not guess: break
    if guess < secret:
    	easygui.msgbox(str(guess) + " Too low, ye scurvy dog!")
    elif guess > secret:
    	easygui.msgbox(str(guess) + " Too high, landlubber!")
    tries = tries + 1

if guess == secret:
	easygui.msgbox("Avast ye got it! Found my secret, ye did")
else:
    easygui.msgbox("No more guesses! Better luck next time, matey!")
