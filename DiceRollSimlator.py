#This is project nuber 2 of my python journey this is a program to simulate a dice roll
#Author Gamuchirayi Manungo 

#imported Libraries 
import random

#list that contains allowed commands 
allowed = ['roll','exit']

print("""Welcome to the dice role Simulator... 

	Plese see the following options on how to use the Program.
	1. To roll The Dice type in - Roll 
	2. to exit the program type in - exit 
	""")

#Main body of code
def Main():
	print("Program Started")
	
	while True:
		#request input from user
		user_input = input("[*]>").lower()
		#error handerling in user enters intergers instead of string characters
		try:
			str(user_input)
		except:
			print("Please Make Sure You Enter String Characters Only")
			continue
		#error handerling making sure user does not enter an input the program does not understand
		if user_input.lower() not in allowed:
			print("You have not entered a valid command Please check the possible instructions")
			continue
		else:
			#when output is correct check what user entered an perform action
			if user_input == 'roll':
				#using random module to generate a random set of intergers
				first_dice = random.randint(1,6)
				second_dice = random.randint(1,6)
				print("[*]>Dice 1:\t", first_dice)
				print("[*]>Dice 2:\t",second_dice)
				continue
				#when input is eqaul to exit program is aborted. 
			elif user_input == 'exit':
				print("[*]>you have ended the program")
				break

#calling function to execute	
Main()
