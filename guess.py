import random

random_number=random.randint(1,10)  #taking random input
number=None

while number != random_number:
	number = input("Pick a number from 1 to 10: ")
	number = int(number)
	if number < random_number:
		print("Too LOW!")
	elif number > random_number:
	    print("Too HIGH!")
	else:
	    print("You WON!!!")
	    play=input("Do you want to play again(y/n): ")
	    if play=="y":
	        random_number=random.randint(1,10)
	        number=None
	    else:
	         print("Thank you for playing!")
	         break        	
