import random
choices=["rock","paper","scissor"]
print("   Welcome To ROCK PAPER SCISSOR GAME !")
print("----------------------------------------------")

user_choice=input("ENTER YOUR CHOICE:(rock,paper,scissor):")
computer_choice=random.choice(choices)
print(f"computer_choice: {computer_choice}")

if user_choice == computer_choice:
    print(f"Both picked {user_choice} ITS A TIE")

elif (user_choice=="rock"and computer_choice=="scissor" )or(user_choice=="scissor"and computer_choice=="paper") or(user_choice=="paper"and computer_choice=="rock" ):
     print(f" {user_choice} beats {computer_choice} SO YOU WIN")
else:
    print(f" {computer_choice} beats {user_choice} SO YOU LOOSE!")
    
    
     