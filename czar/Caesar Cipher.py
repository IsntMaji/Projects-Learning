alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art
print(art.logo)

run = True
while run:
    program = input("Type 'run' to start, 'stop' to quit\n").lower()
    if program == "run":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction != "encode" and direction != "decode":
            print("That is not an option, restart")
            exit()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        # def encrypt(original_text, shift_amount):
        #     encrypted_word = []
        #     for letter in original_text:
        #         if letter == " ":
        #             encrypted_word.append(letter)
        #         else:
        #             letter_place = alphabet.index(letter)
        #             final_number = letter_place + shift_position
        #             if final_number > 25:
        #                 final_number -= 26
        #             encrypted_word.append(alphabet[final_number])
        #     output = ''.join(encrypted_word)
        #     print(f"Your encrypted message is: {output}")

        # def decrypt (original_text, shift_amount):
        #     decrypted_word = []
        #     for letter in original_text:
        #         if letter == " ":
        #             decrypted_word.append(letter)
        #         else:
        #             letter_place = alphabet.index(letter)
        #             final_number = letter_place - shift_position
        #             if final_number < 0:
        #                 final_number += 26
        #             decrypted_word.append(alphabet[final_number])
        #     output = ''.join(decrypted_word)
        #     print(f"Your decrypted message is: {output}")

        # if direction == "encode":
        #     encrypt(text, shift)
        # elif direction == "decode":
        #     decrypt(text, shift)

        # def caesar(text_direction, original_text, shift_position):
        #     cipher_word = ""
        #     if text_direction == "encode":
        #         for letter in original_text:
        #             if letter == " ":
        #                 cipher_word += letter
        #             else:
        #                 final_number = alphabet.index(letter) + shift_position
        #                 final_number %= len(alphabet)
        #                 cipher_word += alphabet[final_number]
        #     elif text_direction == "decode":
        #         for letter in original_text:
        #             if letter == " ":
        #                 cipher_word += letter
        #             else:
        #                 final_number = alphabet.index(letter) - shift_position
        #                 final_number %= len(alphabet)
        #                 cipher_word += alphabet[final_number]
        #     print(f"Your message is: {cipher_word}")

        def caesar(text_direction, original_text, shift_position):
            cipher_word = ""
            for letter in original_text:
                if letter not in alphabet:
                    cipher_word += letter
                else:
                    if text_direction == "encode":
                        final_number = alphabet.index(letter) + shift_position
                    elif text_direction == "decode":
                        final_number = alphabet.index(letter) - shift_position
                    final_number %= len(alphabet)
                    cipher_word += alphabet[final_number]
            print(f"Your message is: {cipher_word}")

        caesar(direction, text, shift)

    else:
        if program == "stop":
            run = False
            break
