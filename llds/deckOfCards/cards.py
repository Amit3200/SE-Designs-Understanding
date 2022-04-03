# Deck of Cards

# Deck
    # Cards         - 52 - (13 x 4)

# Cards
    # Shapes        - Spade, Diamond, Heart, Club
    # Face Value    - [1 - 13] [J - 11, Q - 12, K - 13]


# Hand
    # Player holding cards
    # limit to 5

from enum import Enum
from random import randint

class Suits(Enum):
    Spade   = 1
    Diamond = 2
    Heart   = 3
    Club    = 4

class Card:
    suit        : Suits
    face_value  : int

    def __init__(self, suit : Suits, face_value : int):
        self.suit = suit 
        self.face_value = face_value
    
    def __str__(self):
        val = self.face_value
        if val == 11:
            val = "J"
        elif val == 12:
            val = "Q"
        elif val == 13:
            val = "K"
        return str(val) + " of "+str(self.suit).split('.')[1]
    
    def get_suit(self) -> Suits:
        return self.suit
    
    def get_face_value(self) -> int:
        return self.face_value
    

class Deck:
    cards : list[Card] = []

    def __init__(self):
        self.cards = []
        for value in range(1,14):
            for suit in Suits:
                card = Card(suit, value)
                self.cards.append(card)
    
    def __str__(self):
        card_val = ""
        for card in self.cards:
            card_val += str(card) + "\n"
        return card_val

    def shuffle(self):
        ceil     = len(self.cards) - 1
        for idx in range(0,len(self.cards)):
            swap_idx = randint(0,randint(0,ceil))
            self.cards[swap_idx], self.cards[idx] = self.cards[idx], self.cards[swap_idx]
    
    def draw(self) -> Card:
        return self.cards.pop()
    
    def draw_random(self) -> Card:
        rand_idx = randint(0, len(self.cards) - 1)
        card     = self.cards[rand_idx]
        del self.cards[rand_idx]
        return card


class Hand:
    cards   : list[Card] = []
    hand_id : int = None
    
    def __init__(self,hand_id):
        self.hand_id = hand_id
    
    def __str__(self):
        card_val = "{hid} Holding\n".format(hid = self.hand_id)
        for card in self.cards:
            card_val += str(card) + "\n"
        return card_val
        
    
    def add_to_hand(self, card):
        if len(self.cards) + 1 <= 5:
            self.cards.append(card)
        else:
            self.display_card_error(1)
        
    def remove_from_hand(self, idx) -> Card:
        if len(self.cards) >= 1:
            card = self.cards[idx]
            del self.cards[idx]
            return card
        else:
            self.display_card_error(2)

    def display_card_error(error_code: int):
        if error_code == 1:
            print("Hand holding 5 cards already.")
        elif error_code == 2:
            print("Hand doesn't have enough cards to withdraw.")
        else:
            print("Some unhandled exception.")
    
deck = Deck()
print(deck)
deck.shuffle()
print(deck)

hand = Hand(1)
hand.add_to_hand(deck.draw())
print(hand)