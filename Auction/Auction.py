import art
from os import system

bidder = {}
print(art.logo)
run = True

print("Welcome to the secret auction!")
while run:
    key = input("What is your name?\n")
    value = int(input("What is your bid?\n$"))
    bidder[key] = value
    next_person = input("Are there any other bidders? y/n\n").lower()
    if next_person == "y":
        system("cls")
    elif next_person == "n":
        run = False
        system("cls")

top_bid = {"winner": [1, 1]}
for key in bidder:
    if bidder[key] > top_bid["winner"][1]:
        top_bid["winner"][0] = key
        top_bid["winner"][1] = bidder[key]

print(f"The winner of this auction is: {top_bid["winner"][0]} with a bid of ${top_bid["winner"][1]}")
