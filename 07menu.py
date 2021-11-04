import sys
import os

def options():
    os.system('cls')
    print (" ------------------------------------------------ ")
    print ("|                                                |")
    print ("|    07Menu                                      |") 
    print ("|    Name :Isabelle Pannell                      |")
    print ("|    Version : 01                                |")
    print ("|                                                |")
    print (" ------------------------------------------------ ")
    print ("")
    print ("1. Hello World")
    print ("2. Goodbye World")
    print ("3. Goodbye Person")
    print ("4. Good Teacher")
    print ("5. forLoop")
    print ("6. whileLoop")
    print ("7. sting Loop")
    print ("8. Convert to ascii")
    print ("9. Encode a string")
    print ("x. To Exit")

def helloworld():
    print ("")
    print ("----Start of Output ---------------------------")
    print ("")
    print ("Hello World")
    print ("")
    print ("----End of Output -----------------------------")

def goodbyeworld():
    print ("")
    print ("----Start of Output ---------------------------")
    print ("")
    print ("Hello World")
    user = input("------> Program paused - press enter to continue")
    print("Goodbye World")
    print ("")
    print ("----End of Output -----------------------------")

def goodbyeperson():
    print ("")
    print ("----Start of Output ---------------------------")
    print ("")
    print ("Hello World")
    user = input("What is your name ? ")
    print("Goodbye " + user)
    print ("")
    print ("----End of Output -----------------------------")

def goodteacher():
    print ("")
    print ("----Start of Output ---------------------------")
    print ("")
    user = input("Teacher's name (try Mr Horan) ")
    if user == "Mr Horan":
        print ("You are lucky, he is a great teacher.")
    else:
        print (user + " is an ok teacher")
    print ("")
    print ("----End of Output -----------------------------")

def forloop():
    print ("")
    print ("----Start of Output ---------------------------")
    print ("")
    for user in range(1, 500):
        print (user)
    print ("")
    print ("----End of Output -----------------------------")

def whileloop():
    print ("")
    print ("----Start of Output ---------------------------")
    print ("")
    subject = input ("What is the name of this subject ")
    while subject != "IST":
        print ("Not Correct - try again")
        subject = input ("What is the name of this subject ")
        continue
    else:
        print ("")
        print ("")
        print (" Congratulations!!")
        print ("")
        print ("")
        print ("")
    print ("----End of Output -----------------------------")

while True:
    options()
    menu = input ('Enter an option ')
    valid = ["1", "2", "3", "4", "5", "6", "x"]

    if menu in valid:
        if menu == "1":
            helloworld()
        elif menu == "2":
            goodbyeworld()
        elif menu == "3":
            goodbyeperson()
        elif menu == "4":
            goodteacher()
        elif menu == "5":
            forloop()
        elif menu == "6":
            whileloop()
        elif menu == "x":
            print ("")
            print ("----Start of Output ---------------------------")
            print ("")
            print ("")
            print ("----End of Output -----------------------------")
            print ("")
            print ("")
            print ("")
            input ("Press Enter to continue")
            print ("")
            sys.exit()
    else:
        print ("")
        print ("----Start of Output ---------------------------")
        print ("")
        print ("invalid option")
        print ("")
        print ("----End of Output -----------------------------")
        
    print ("")
    print ("")
    print ("")
    input ("Press Enter to continue")