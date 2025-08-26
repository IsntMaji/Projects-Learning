import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while 1:
    player_cards = {"cards": []}
    dealer_cards = {"cards": []}
    game_start = input("Do you want to play a game of Blackjack? y/n?: ").lower()
    if game_start == 'y':
        print(art.logo)
        for i in range(0,2):
            player_cards["cards"].append(random.choice(cards))
        if sum(player_cards["cards"]) == 22:
            player_cards["cards"][0] = 1
        print(f"Your cards: {player_cards["cards"]}, current score: {sum(player_cards["cards"])}")
        dealer_cards["cards"].append(random.choice(cards))
        print(f"Dealer's first card: {dealer_cards["cards"][0]}")
        while 1:
            player_choice = input("Type 'y' for another card, type 'n' to wave: ").lower()
            if player_choice == 'y':
                player_cards["cards"].append(random.choice(cards))
                c = 0
                for i in player_cards["cards"]:
                    if i == 11:
                        if sum(player_cards["cards"]) > 21:
                            player_cards["cards"][c] = 1
                    c += 1
                print(f"Your cards: {player_cards["cards"]}, current score: {sum(player_cards["cards"])}")
                if sum(player_cards["cards"]) > 21:
                    print("You busted!")
                    break
                else:
                    print(f"Dealer's first card: {dealer_cards["cards"][0]}")
            elif player_choice == 'n':
                print(f"Your final hand: {player_cards["cards"]}, final score: {sum(player_cards["cards"])}")
                while sum(dealer_cards["cards"]) < 17:
                    dealer_cards["cards"].append(random.choice(cards))
                    d = 0
                    for i in dealer_cards["cards"]:
                        if i == 11:
                            if sum(dealer_cards["cards"]) > 21:
                                dealer_cards["cards"][d] = 1
                        d += 1
                print(f"Dealer's final hand: {dealer_cards["cards"]}, final score: {sum(dealer_cards["cards"])}")
                if sum(dealer_cards["cards"]) > 21:
                    print("DEALER BUSTED, YOU WIN! 😊")
                    break
                elif sum(player_cards["cards"]) > sum(dealer_cards["cards"]):
                    print("YOU WIN! 😊")
                    break
                elif sum(player_cards["cards"]) < sum(dealer_cards["cards"]) and sum(dealer_cards["cards"]) <= 21:
                    print("YOU LOSE! 😭")
                    break
                else:
                    print("IT'S A DRAW! 😮")
                    break
    elif game_start == 'n':
        exit()
