# Blackjack game

"""
1. create 52 cards -> Ok
2. Shuffle the deck -> OK
3. Create 3 Players and Dealer
4. Ask the player for their bet
5. Deal two cards to the Dealer and Two cards for each player
6. Dealer shows you only one card
7. Ask the players if they want to Hit and add more card to thier deck or stay
8. If the Players doesn't go BUST (over 21) ask him again to Hit or stay
9. If players stands, there is a Dealer move. The dealer always hit until his/her value meets or exceed 17
10. Determine the winner and adjust the chips to the Dealer or/and Players
11. Ask the player if they'd go play again

"""

# 1. create 52 cards

import random

suits = {"Hearts", "Spades", "Clubs", "Diamonds"}
ranks = {"Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"}
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
playing = True
playing_one = True


def main():
    while True:
        global playing_one
        global playing
        # invoke the classes
        allcards = Card(ranks,suits)
        mydeck = Deck()
        player_one = Player("Player 1")
        player_two = Player("Player 2")
        player_three = Player("Player 3")
        dealer = Player("Dealer")
        my_chips = Chips("Player 1")
        player_2_chips = Chips("Player 2")
        player_3_chips = Chips("Player 3")

        #creating lists with players
        players = [player_one, player_two, player_three]
        players_chips = [my_chips, player_2_chips, player_3_chips]

        #Create empty lists for players and Dealer
        print("Welcome in the BlackJack Game!\n")

        get_bet(my_chips)
        get_bet_AI(player_2_chips)
        get_bet_AI(player_3_chips)


        #Shuffle the deck
        mydeck.shuffle_deck()

        #add cards to the deck
        #Player One - You
        player_one.add_card(mydeck.deal())
        player_one.add_card(mydeck.deal())



        #Player Two and Three - AI - deal cards

        player_two.add_card(mydeck.deal())
        player_two.add_card(mydeck.deal())

        player_three.add_card(mydeck.deal())
        player_three.add_card(mydeck.deal())

        #Dealer - show only second card - for now

        dealer.show_first_value(mydeck.deal())
        dealer.show_first_value(mydeck.deal())

        # Players show all values
        print("You have:\n", *player_one.cards, sep='\n')
        print("Your value is: ", player_one.value)

        print("\nPlayer Two has:\n", *player_two.cards, sep='\n')
        print("Player Two value is: ", player_two.value)

        print("\nPlayer Three has:\n", *player_three.cards, sep='\n')
        print("Player Three value is: ", player_three.value)

        # Dealer shows only on value from second card, first one is hidden
        print("\n Dealer has:\n")
        print("<First Dealers card is hidden>")
        print("Second Dealers card is:", dealer.cards[1])
        print("Dealer value is:",dealer.dealer_one_value[1])

        #thinking about create loop with 'stand' option - if players stand then the loop break 
        while playing_one:

            #Player one hit or stand - the value is show
            player_one.hit_or_stand(mydeck, player_one)

            if player_one.value > 21:
                print(f"{player_one.name} BUST! You loose {my_chips.default}")
                my_chips.lose_bet()
                print(f"Your total depo is: {my_chips.total}")
                break
        
        while playing:
            #Player Two turn 
            player_two.hit_or_stand_AI(dealer.dealer_one_value[1], player_two.value, mydeck, player_two)

            #Player Three turn
            player_three.hit_or_stand_AI(dealer.dealer_one_value[1], player_three.value, mydeck, player_three)


            for player in players:
                if player.value > 21:
                    print(f"{player.name} BUSTS and loses !")
                    players.remove(player)
                    break
                    
                    
        for player in players:
                    
            if player.value <= 21:
                while dealer.value < 17:
                    print("Dealer has: ", *dealer.cards, sep="\n")
                    print("Dealer value is: ", dealer.value)
                    dealer.hit(mydeck)

                #if dealer looses    
                if dealer.value > 21:
                    print("Dealer has: ", *dealer.cards, sep="\n")
                    print("Dealer value is: ", dealer.value)
                    print(f"{dealer.name} BUST!")
                    # win for every player who have less than 21
                    for player in players:
                        # PLAYER ONE
                        if player == player_one:
                            print(f"{player_one.name} wins this part and earn {my_chips.default*1.5}")
                            my_chips.win_bet()
                            print(f"Your total depo is: {my_chips.total}")
                        # PLAYER TWO
                        if player == player_two:
                            print(f"{player_two.name} wins this part and earn {player_2_chips.default*1.5}")
                            player_2_chips.win_bet()
                            print(f"Your total depo is: {player_2_chips.total}")
                        # PLAYER THREE
                        if player == player_three:
                            print(f"{player_three.name} wins this part and earn {player_3_chips.default*1.5}")
                            player_3_chips.win_bet()
                            print(f"Your total depo is: {player_3_chips.total}")

                elif dealer.value > player.value:
                    print("Dealer has: ", *dealer.cards, sep="\n")
                    print("Dealer value is: ", dealer.value)
                    print(f"Dealer wins over {player.name}!")
                    for chips in players_chips:
                        if chips.name == player.name:
                            print(f"{player.name} lose his bet which is: {chips.default}")
                            chips.lose_bet()

                elif player.value > dealer.value:
                    print(f"{player.name} has: ", *player.cards, sep="\n")
                    print(f"{player.name} value is: ", player.value)
                    print(f"{player.name} wins!")
                    for chips in players_chips:
                        if chips.name == player.name:
                            print(f"{player.name} win his bet which is: {chips.default*1.5}")
                            chips.win_bet()
                else:
                    for chips in players_chips:
                        if chips.name == player.name:
                            print(f"{player.name} has a draw with dealer!")
                            chips.draw_bet()

                
        play_again = input("Do you want to play again? hit 'y' or 'n' ").lower()
        if play_again.startswith('y'):
            print(f"""Total depo of players is:
                 {my_chips.name} is: {my_chips.total}
                 {player_2_chips.name} is: {player_2_chips.total}
                 {player_3_chips.name} is: {player_3_chips.total}
                  """)
            playing = True
            playing_one = True
            continue
        else:
            print("Thanks for playing!")
            break

 

class Card:

    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return self.rank + ' of ' + self.suit

   
#for testing

# two_hearts = Card(rank="Two", suit="Hearts")
# print(two_hearts)

class Deck():

    def __init__(self) -> None:
        self.deck = [] #create empty deck
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def __str__(self) -> str:
        show_deck = ''
        for card in self.deck:
            show_deck += '\n' + str(card)
        return show_deck
    
    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
#for test
    
class Player():

    def __init__(self, name) -> None:
        self.name = name
        self.cards = []
        self.value = 0
        self.dealer_one_value = []
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces = 1

    def adjust_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def hit(self, deck):
        self.add_card(deck.deal())
        self.adjust_aces()

    def show_first_value(self, card):
        self.add_card(card)
        # self.cards.append(card)
        self.dealer_one_value.append(values[card.rank])
        

    def hit_or_stand(self, deck, player):
        global playing_one
        while True:
            player_x = input("Would you like to hit or stay? (h/s): ").lower()

            if player_x == 'h':
                self.hit(deck)
                print("You have:\n", *player.cards, sep="\n")
                print("Your value is: ", player.value)
                
            elif player_x == 's':
                print(f'{self.name} Stands! Now it\'s opponent turn!')
                playing_one = False
                break
            elif player.value > 21:
                #playing = False
                break
            else:
                print("Sorry, please try again!")
                continue
            break

    def hit_or_stand_AI(self, dealer_value, player_value, deck, player):
        
        global playing
        while player_value <= 21:
            if player_value <= 16 and (dealer_value >= 7 or dealer_value <= 11):
                self.hit(deck)
                print(f"{self.name} have:\n", *player.cards, sep="\n")
                print(f"{self.name} value is: ", player.value)
            elif player_value <= 11:
                self.hit(deck)
                print(f"{self.name} have:\n", *player.cards, sep="\n")
                print(f"{self.name} value is: ", player.value)
            else:
                print(f"{self.name} stands! Now is the opponent turn!")
                playing = False
                break
                
            break
                

class Chips():

    def __init__(self, name) -> None:
        self.total = 500
        self.default = 0
        self.name = name


    def win_bet(self):
        self.total += (self.default*1.5)

    def lose_bet(self):
        self.default * 0

    def draw_bet(self):
        self.total += (self.default)

def get_bet(chips):

        while True:
            try: 
                chips.bet_chips = int(input("What bet do you want to place?: "))
                if chips.bet_chips % 5 != 0:
                    print("Bet should divide by 5!")
                else:
                    chips.total -= chips.bet_chips
                    chips.default += chips.bet_chips
                    print(f"{chips.name} bet {chips.default}!")
            except ValueError:
                print("Please put a correct value!")
            else:
                if chips.bet_chips > chips.total:
                    print("You cannot exceeded", chips.total)
                else:
                    break

def get_bet_AI(chips):
    bet = random.randrange(5, chips.total, 5)
    chips.total -= bet
    chips.default += bet
    print(f"{chips.name} bet {chips.default}!")
    


def player_win(player, dealer, chips):
    print(f"{player} win {chips*1.5}")
             
        


    

    
    

    




if __name__ == "__main__":
    main()
