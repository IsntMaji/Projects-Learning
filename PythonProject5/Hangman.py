import hangman_words
import hangman_art
import random

chosen_word = random.choice(hangman_words.word_list)
compare = list(chosen_word)
blanks = []
guessed_letters = set()

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
    last_guess = guess

    for x in range(0, 1):
        if guess in guessed_letters:
            print("You have already guessed that!")

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

    if verdict == 1 and guess not in guessed_letters:
        print(f"You guessed {guess},{correct}")
    elif verdict == 0:
        life -= 1
        print(f"You guessed {guess},{wrong}")
    else:
        pass

    guessed_letters.add(guess)

if displayed_word == chosen_word:
    print(hangman_art.poggers)
    print(displayed_word)
    print("YOU WIN!")