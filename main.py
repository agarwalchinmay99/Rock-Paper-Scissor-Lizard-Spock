import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

player_choice = input("I Choose ")
print("You chose " + (player_choice) + "!")

def name_to_number(player_choice): 
       
    if(player_choice == "rock"):
        return 0
    elif(player_choice == "spock"):
        return 1
    elif(player_choice == "paper"):
        return 2
    elif(player_choice == "lizard"):
        return 3
    elif(player_choice == "scissors"):
        return 4
    else:
        print("but thats an Invalid input.")
        return "Invalid input."
       
        
       

#test cases for first function
#print(name_to_number("rock"))
#print(name_to_number("paper"))
#print(name_to_number("scissors"))
#print(name_to_number("lol"))
#print(name_to_number("lizard"))
#print(name_to_number("spock"))
    
def number_to_name(number):
   
    if(number == 0):
        return "rock"
    elif(number == 1):
        return "spock"
    elif(number == 2):
        return "paper"
    elif(number == 3):
        return "lizard"
    elif(number == 4):
        return "scissors"
    else:
        return "Invalid Number Input"
    
#print()
#test cases for second function
#print(number_to_name(0))
#print(number_to_name(1))
#print(number_to_name(2))
#print(number_to_name(3))
#print(number_to_name(4))
#print(number_to_name(5))


#number = random.randrange(0,4)
computer_choice = number_to_name(number = random.randrange(0,4))
print("Computer Chooses " + computer_choice + "!")

def rpsls(player_choice, computer_choice):
    """
    Given string player_choice, play a game of RPSLS 
    and print results to console
    """
    if(player_choice == computer_choice):
        print("This match was a draw. Wanna play again?")
        
    elif(player_choice != computer_choice):
        if((player_choice == "rock") and (computer_choice == "spock" or computer_choice == "paper")):
            print("Computer won this round. Wanna play again?")
            
        elif(player_choice == "rock"):
            print("You won this round. Wanna play again?")
            
        elif((player_choice == "spock") and (computer_choice == "lizard" or computer_choice == "paper")):
            print("Computer won this round. Wanna play again?")
            
        elif(player_choice == "spock"):
            print("You won this round. Wanna play again?")
            
        elif((player_choice == "paper") and (computer_choice == "lizard" or computer_choice == "scissors")):
            print("Computer won this round. Wanna play again?")
            
        elif(player_choice == "paper"):
            print("You won this round. Wanna play again?")
            
        elif((player_choice == "lizard") and (computer_choice == "scissors" or computer_choice == "rock")):
            print("Computer won this round. Wanna play again?")
            
        elif(player_choice == "lizard"):
            print("You won this round. Wanna play again?")
            
        elif((player_choice == "scissors") and (computer_choice == "rock" or computer_choice == "spock")):
            print("Computer won this round. Wanna play again?")
           
        elif(player_choice == "scissors"):
            print("You won this round. Wanna play again?")
            
        else:
            print("You gave an invalid input. Try again.")
           
        
print(rpsls(player_choice, computer_choice))    
     
    
## test your code
"""Hit run and when it asks your input, enter anything out of rock, spock, paper, scissors and lizard"""
