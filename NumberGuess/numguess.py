import art
import random

game_over = False
attempts = 0


def run_game(mode):
    global attempts

    if mode == "hard":
        attempts = 5
        return attempts
    elif mode == "easy":
        attempts = 10
        return attempts
    else:
        return 0


def check_guess(n):
    global attempts

    if n < number_to_guess:
        print("Too low.")
        attempts -= 1
        return 0
    elif n > number_to_guess:
        print("Too high.")
        attempts -= 1
        return 0
    else:
        print(f"You got it, {number_to_guess} was the number!")
        return 1


while not game_over:
    number_to_guess = random.choice(range(1, 101))
    print(art.logo)
    print("Welcome to Number Guess!")
    print("I'm thinking of a number between 1 and 100.")
    while 1:
        difficulty = input("Choose the difficulty, 'easy' or 'hard': ").lower()
        attempts = run_game(difficulty)
        if attempts == 5 or attempts == 10:
            while attempts != 0:
                print(f"You have {attempts} attempts remaining to guess the number.")
                try:
                    guess = int(input("Make a guess: "))
                    if guess > 0 and guess < 101:
                        is_correct = check_guess(guess)
                        if is_correct == 1:
                            break
                except ValueError:
                    pass
            while 1:
                play_again = input("Would you like to play again? y/n: ").lower()
                if play_again == "y":
                    break
                elif play_again == "n":
                    game_over = True
                    break
            break
