import random

class Player(object):
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.reserve = []

    def calc_hand_value(self):
        n = 0
        for i in range(self.hand):
            n += self.hand[i]
        return n

    def draw_for_battle(self):
        """
        Selects stack of four cards to play when a War is declared. Returns a list.
        """
        self.pick_up_reserves()
        if len(self.hand) > 3:
            cards = self.hand[0:4]
            self.hand = self.hand[4:]
        else:
            cards = self.hand
        return cards

    def play_card(self):
        """
        Removes top card from player's deck and adds it to game discard pile. Returns a string.
        """
        if len(self.hand) == 0 and self.reserve > 0:
            self.pick_up_reserves()
        card = self.hand.pop()
        return card

    def pick_up_reserves(self):
        """
        Transfers player's reserve pile to their hand when they run out of cards.
        """
        print("({} picks up {} cards from reserve.)".format(
            self.name, len(self.reserve)))
        self.reserve = self.shuffle(self.reserve)
        self.hand.extend(self.reserve)
        self.reserve = []

    def shuffle(self, deck):
        """
        Shuffles and returns deck
        """
        dl = len(deck)-1
        tmp = ""
        for i in range(0, dl):
            r = random.randint(0, dl)
            tmp = deck[i]
            deck[i] = deck[r]
            deck[r] = tmp
        return deck