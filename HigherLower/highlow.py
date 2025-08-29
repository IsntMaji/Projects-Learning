from random import randint
from art import logo, vs
from game_data import data

score = 0

def data_info(num, letter):
    return f"Option {letter}: {data[num]["name"]}, a {data[num]["description"]}, from {data[num]["country"]}."

while 1:
    print(logo)
    list_upper = len(data) - 1
    A_num = randint(0, list_upper)
    B_num = randint(0, list_upper)
    while 1:
        if A_num == B_num:
            while A_num == B_num:
                B_num = randint(0, list_upper)
        A_followers = data[A_num]["follower_count"]
        B_followers = data[B_num]["follower_count"]
        print(data_info(A_num, "A"))
        print(vs)
        print(data_info(B_num, "B"))
        while 1:
            try:
                answer = input("Which has more Instagram followers? A/B? ").lower()
                if answer == "a":
                    if A_followers > B_followers:
                        score += 1
                        print(f"You're right! Current score: {score}")
                        B_num = A_num
                        break
                    elif A_followers < B_followers:
                        print(f"You were incorrect! Final score: {score}")
                        score = 0
                        break
                elif answer == "b":
                    if B_followers > A_followers:
                        score += 1
                        print(f"You're right! Current score: {score}")
                        A_num = B_num
                        break
                    elif B_followers < A_followers:
                        print(f"You were incorrect! Final score: {score}")
                        score = 0
                        break
            except ValueError:
                pass
        if score == 0:
            try:
                play_again = input("Would you like to try again? Y/N: ").lower()
                if play_again == "y":
                    break
                elif play_again == "n":
                    exit()
            except ValueError:
                pass
