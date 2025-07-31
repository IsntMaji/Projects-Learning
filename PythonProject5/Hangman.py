import hangman_words
import hangman_art
import random

chosen_word = random.choice(hangman_words.word_list)
compare = list(chosen_word)
blanks = []

for char in compare:
    blanks += "_"

displayed_word = ''.join(blanks)
life = 6

print(f"{hangman_art.logo}")
while displayed_word != chosen_word:

    if life <= 0:
        print(f"{hangman_art.stages[life]}")
        print(chosen_word)
        print("YOU LOSE!")
        break

    print(f"{hangman_art.stages[life]}")
    print(f"Word to guess: {displayed_word}")
    print(f"LIVES {life}/6")
    guess = input("Guess a letter: ").lower()
    verdict = 0
    position = 0

    for _ in compare:
        if _ == guess:
            blanks[position] = guess
            displayed_word = ''.join(blanks)
            verdict = 1
        position += 1

    correct = " that is in the word. Congrats!"
    wrong = " that is not in the word. You lose a life!"

    if verdict == 1:
        print(f"You guessed {guess},{correct}")
    else:
        life -= 1
        print(f"You guessed {guess},{wrong}")

if displayed_word == chosen_word:
    print(hangman_art.poggers)
    print(displayed_word)
    print("YOU WIN!")