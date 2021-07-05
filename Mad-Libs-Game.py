#The following code is according to Python 3
print("Welcome to Mad Libs Game!")

#Take inputs from user
name= input("Enter any name: ")
theme= input("Enter a theme: ")
place= input("Enter any place: ")
time= input("Enter any time: ")
verb= input("Enter any verb: ")
animal= input("Enter name of any animal: ")
body= input("Enter name of any body part: ")
contact= input("Enter contact information: ")

#Print the final story line with the words entered by the user
print(name+" is having a "+ theme+" party! It is going to be at "+place+". Please make sure you show up at "+time+" or else you will be required to "+ verb +" a/an "+ animal+ " with your "+ body+ ". RSVP at "+ contact+".")
