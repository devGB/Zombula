import easygui
#flavor = easygui.buttonbox("What is your favorite ice cream flavor?",
#				choices = ['vanilla', 'Chocolate', 'strawberry', 'Caramel'] )
#flavor = easygui.choicebox("What is your favorite ice cream flavor?",
#				choices = ['vanilla', 'Chocolate', 'strawberry', 'Caramel'] )
flavor = easygui.enterbox("What is your favorite ice cream flavor?",
                          default = 'Vanilla')
easygui.msgbox ("You entered " + flavor)
