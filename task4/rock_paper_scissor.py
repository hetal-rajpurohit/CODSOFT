#rock paper scissor game
print("=================================")
print("     Rock, paper, scissor game   ")
print("=================================")

print("             FUN TIME              ")
print("CHOOSE ANY ONE:")
print("Rock")
print("Paper")
print("Scissor")
import random
choices = ["rock", "paper", "scissor"]
user_score = 0
computer_score = 0

while True:
    user_choice = input("Enter your choice: ").lower()
    if user_choice not in choices:
        print("Invalid choice, please choose again.")
        continue

    computer_choice = random.choice(choices)

    print("Your choice: ", user_choice)
    print("Computer's choice: ", computer_choice)

    if user_choice == computer_choice:
        print("Result: It's a Tie >-<")

    elif ((user_choice == "rock" and computer_choice == "scissor") or 
          (user_choice == "paper" and computer_choice == "rock") or
          (user_choice == "scissor" and computer_choice == "paper")):
        print("Result: Yayyy! You win")
        user_score +=1
    else:
        print("Result: you lose")
        computer_score +=1

    #displaying score
    print("Your score: ",user_score)
    print("Computer's score: ",computer_score)
    play_again = input("Do you want to play again ?: ")
    if play_again != "yes":
        print("---Thank you for playing!---")
        break