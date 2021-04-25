import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
game_on=True

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank+' of '+self.suit


class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def __str__(self):
        deck_cards=''
        for item in self.all_cards:
            deck_cards+='\n'+item.__str__()
        return deck_cards

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        single_card=self.all_cards.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces
        self.hit=False

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if self.card.rank=='Ace':
            self.aces+=1

    def adjust_for_ace(self):
        if self.value>21 and self.aces>1:
            self.value=self.value-10
            self.aces=self.aces-1


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

while game_on:
    newdeck = Deck()
    newdeck.shuffle()
    player1=Hand()
    player2=Hand()
    playing=True
    for i in range(0,3):
        player1.add_card(newdeck.deal())
        player2.add_card(newdeck.deal())
    while playing
        if player1.value>21 and player1.aces=0:
            print("Player1: BUSTED! and Player2: Won!")
            game_on=False
            break
        elif player2.value>21 and player2.aces=0:
            print("Player2: BUSTED! and Player1: Won!")
            game_on = False
            break
        else:
            if player1.aces>0:
                player1.adjust_for_ace()
            else player2.aces>0:
                player2.adjust_for_ace()
    else:
        for player in [player1, player2]:
            if player.hit==True:
                pass
            else:
                choice = input(f'Hello {player}! HIT or DRAW?')
                if choice=="HIT":
                    player.hit=True
                elif choice=="DRAW":
                    player.add_card(newdeck.deal())
                else:
                    print("Wrong Option!!! Enter HIT or DRAW?")





print(newdeck)
p1=Hand()
p1.add_card(newdeck.deal())
p1.add_card(newdeck.deal())
print(p1.value)
for item in p1.cards:
    print(item)




