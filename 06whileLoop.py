print(" ------------------------------------------------")
print("|                                                |")
print("|    06whileLoop                                 |")
print("|    Name : Isabelle Pannell                     |")
print("|    Version : 01                                |")
print("|                                                |") 
print(" ------------------------------------------------")
user = input("What is the name of this subject ")
while user != ("IST"):
    print("Not correct - try again")
    user = input("What is the name of this subject ")
    continue
else:
    print("\nCongratulations!!\n")