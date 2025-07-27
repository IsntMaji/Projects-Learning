rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

rock_paper_scissors_options = [rock, paper, scissors]

print("Welcome to rock, paper, scissors")
player_choice = input("What do you play?\n").lower()
computer_choice = random.choice(rock_paper_scissors_options)

if player_choice == "rock":
    print("YOUR HAND:")
    print(rock)
    if computer_choice == scissors:
        print("COMPUTER HAND:")
        print(scissors)
        print("You win!")
    elif computer_choice == paper:
        print("COMPUTER HAND:")
        print(paper)
        print("You lose!")
    else:
        print("COMPUTER HAND:")
        print(rock)
        print("It's a tie!")
elif player_choice == "paper":
    print("YOUR HAND:")
    print(paper)
    if computer_choice == scissors:
        print("COMPUTER HAND:")
        print(scissors)
        print("You lose!")
    elif computer_choice == paper:
        print("COMPUTER HAND:")
        print(paper)
        print("It's a tie!")
    else:
        print("COMPUTER HAND:")
        print(rock)
        print("You win!")
elif player_choice == "scissors":
    print("YOUR HAND:")
    print(scissors)
    if computer_choice == scissors:
        print("COMPUTER HAND:")
        print(scissors)
        print("It's a tie!")
    elif computer_choice == paper:
        print("COMPUTER HAND:")
        print(paper)
        print("You win!")
    else:
        print("COMPUTER HAND:")
        print(rock)
        print("You lose!")
else:
    print("You typed an invalid choice.")
