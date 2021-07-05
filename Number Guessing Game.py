import math
import random

lower= int(input("Enter a lower bound: "))
upper= int(input("Enter a upper bound: "))
x= random.randint(lower, upper)
print("\n\tYou have only ", round(math.log(upper-lower + 1,2))," chances to guess the number!\n")

count = 0
while count< math.log(upper-lower +1, 2):
    count= count + 1
    guess= int(input("Guess a number: "))
    if x==guess:
        print("Congratulations you did it in ", count, " try")
        break
    elif x> guess:
        print("You guessed to small!")
    elif x< guess:
        print("You guess too high!")
if count>= math.log(upper-lower +1 ,2):
    print("The number is %d" % x)
    print("Better Luck Next Time!")
