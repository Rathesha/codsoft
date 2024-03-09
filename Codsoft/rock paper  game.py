import random
user_score = 0
computer_score = 0
print(" Rock","paper","scissor")
while user_score < 3 and computer_score < 3:
    player=input("\choose 'rock','paper','scissors'\n>")
    computer=random.choice(["rock","paper","scissors"])
    print("player:", player)
    print("computer:",computer)
    if (player==computer):
        print("It's a tie!")
        user_score += 1  
    elif player=="rock" and computer == "paper":
        print("you win!")
        computer_score += 1  
    elif player=="rock" and computer=="scissor":
        print("you win!")
        user_score += 1  
    elif player=="paper" and computer=="scissor":
        print("you win!")
        computer_score += 1
    elif player=="paper" and computer=="scissor":
        print("you win!")
        user_score += 1
    elif player=="scissor" and computer=="rock":
        print("you win!")
        computer_score+=1
    elif player=="scissor" and computer=="paper":
        print("you win!")
        user_score+=1
    
    else:
        print("you loose!")
    print("player: ", user_score)
    print("computer: ",computer_score)

 
    
