# 6.5. 2022
# no split
from random import choice


def show():
    print(f"\ndealer: {hand_cards(dealer)}\nplayer: {hand_cards(player)}")


def stand():
    global soft_end

    soft_end = True
    dealer[0] = secret_card

    while hand_value(dealer) <= 17:
        dealer.append(card())

        if hand_value(dealer) > 21:
            ace_check(dealer)

    check()


def check():
    show()
    if hand_value(player) > 21:
        if ace_check(player) != True:
            return dealer_win()

    elif hand_value(dealer) > 21:
        if ace_check(dealer) != True:
            return player_win()

    if soft_end:

        if hand_value(player) > hand_value(dealer):
            return player_win()

        elif hand_value(player) < hand_value(dealer):
            return dealer_win()

        else:
            return push()


def ace_check(hand):
    for i in range(len(hand)):

        if hand[i][1] == 11:
            hand[i][1] = 1

            return True


def hand_value(hand):
    s = 0
    for i in range(len(hand)):
        s += hand[i][1]

    return s


def hand_cards(hand):
    c = ""
    for i in range(len(hand)):
        c += hand[i][0]

    return c


def player_win():
    global money, soft_end
    money += bet
    soft_end = True
    print(f"\nCongratulations, you won ${bet}.")


def dealer_win():
    global money, soft_end
    money -= bet
    soft_end = True
    print(f"\nThe dealer won, you lost ${bet}.")


def push():
    global soft_end
    soft_end = True
    print("\nIt's a push.")


def card():

    card = ["", 0]

    card[0] = cards_names.pop(cards_names.index(choice(cards_names)))
    card[1] = cards_values.pop(card[0])
    if len(dealer) > 2:
        show()

    return card


def shuffle():
    global cards_names, cards_values
    cards_names = ['2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥',
               '9♥', '10♥', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♣', 'J♦', 'J♥', 'J♠', 'Q♣', 'Q♦', 'Q♥', 'Q♠', 'K♣', 'K♦', 'K♥', 'K♠', 'A♣', 'A♦', 'A♥', 'A♠']

    cards_values = {"2♣": 2, "3♣": 3, "4♣": 4, "5♣": 5, "6♣": 6, "7♣": 7, "8♣": 8, "9♣": 9,
                "10♣": 10, "2♦": 2, "3♦": 3, "4♦": 4, "5♦": 5, "6♦": 6, "7♦": 7, "8♦": 8,
                "9♦": 9, "10♦": 10, "2♥": 2, "3♥": 3, "4♥": 4, "5♥": 5, "6♥": 6, "7♥": 7,
                "8♥": 8, "9♥": 9, "10♥": 10, "2♠": 2, "3♠": 3, "4♠": 4, "5♠": 5, "6♠": 6,
                "7♠": 7, "8♠": 8, "9♠": 9, "10♠": 10, "J♣": 10, "J♦": 10, "J♥": 10, "J♠": 10,
                "Q♣": 10, "Q♦": 10, "Q♥": 10, "Q♠": 10, "K♣": 10, "K♦": 10, "K♥": 10, "K♠": 10,
                "A♣": 11, "A♦": 11, "A♥": 11, "A♠": 11}


def start():
    global soft_end, dealer, player, bet, secret_card

    shuffle()

    soft_end = False
    dealer = [["⍰ ", 0]]
    player = []

    print(f"\nYou have ${money}.")
    while True:
        bet = int(input("\nHow much would you like to bet? "))
        if bet <= money:
            break
        else:
            print("\nPlese bet only the money you have or cry.")

    for i in range(2):
        player.append(card())

    dealer.append(card())
    secret_card = card()

    print(
        f"\nThe dealer has a secret card and {dealer[1][0]}.\nYou have {player[0][0]} and {player[1][0]}.")

    if hand_value(player) == 21:
        print("\nThat's blackjack, congratulations.")
        stand()

def good_bye():
    print("\n|⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯|")
    print("|Thank you for playing.|")
    print("|⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯|")




money = 1000
end = False


while end == False and money > 0:
    
    start()

    while soft_end == False and money > 0:
        ask = input("\nWhat would you like to do? ").lower()

        if ask == "exit":
            end = True
            break

        elif ask == "hit":
            player.append(card())
            check()

        elif ask == "stand":
            stand()

        elif ask == "double down":
            if bet*2 <= money:
                bet *= 2
                player.append(card())
                stand()
            else:
                print("\nUnfortunately you can't afford to do that right now.")

        else:
            print("\nEither you can't do that or the command is uknown.")


good_bye()
