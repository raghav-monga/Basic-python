#rock paper scissor game

import random
player_wins=0
computer_wins=0
winner=3

while player_wins<winner and computer_wins<winner:
    print(f"\nPlayer score:{player_wins} Computer score:{computer_wins}")

    print(" ...rock...")
    print("...paper...")
    print("...scissors...")

    choice= input("(Enter player's choice):").lower()
    if(choice=="quit" or choice=="q"):
        break
    computer=random.randint(0,2)
    if(computer==0):
        computer="rock"
    elif(computer==1):
        computer="scissors"
    else:
        computer="paper"    
    print(f"The computer chose {computer}") 

    if(choice==computer):
        print("Draw!!")
    elif(choice=="rock"):
        if(computer=="scissors"):
            print("Player wins")
            player_wins+=1
            
        else:
            print("computer wins")
            computer_wins+=1
              

    elif(choice=="scissors"):
        if(computer=="rock"):
            print("Computer wins")
            computer_wins+=1
            
        else:
            print("Player wins")
            player_wins+=1
                

    elif(choice=="paper"):
        if(computer=="rock"):
            print("Player wins")
            player_wins+=1
             
        else:
            print("Computer wins")
            computer_wins+=1
                
    else:
         print("Enter something valid")        

if(player_wins<computer_wins):
         print("\nOH NOO! Computer won")
elif(player_wins==computer_wins):
         print("It's a tie")         
else:
         print("\nYAYYYY!!! You won")

print(f"Final scores: \nPlayer:{player_wins} \t computer:{computer_wins}")                      
     
