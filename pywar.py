"""
* Two players, one human, one computer
* In each round, each player plays the top card in their hand
* The player who plays the highest card adds the two cards to their reserve pile
* If the cards are equal, a WAR sequence occurs
* * Each player plays three face-down cards and one face-up card; the player whose fourth card is highest takes the entire pile
* When all cards in a hand are played, the player picks up the reserve pile, and the card count for both sides is announced
* When one player has zero cards in hand AND zero cards in reserve, the other player wins
"""

class Player(object, name):
    def __init__(self):
        self.hand = []
        self.name = name
        self.reserve = []

    def playCard(self):
        """
        Removes top card from player's deck and adds it to game discard pile. Returns a list item (string).
        """
        card = self.hand.pop()
        if len(self.hand) < 1 and self.reserve > 0:
            self.useReserves()
        return card

    def useReserves(self):
        """
        Transfers player's reserve pile to their hand when they run out of cards.
        """
        self.hand = self.reserve
        self.reserve = []
        print("Picking up reserves. Your hand now has ", len(self.hand), " cards.")

    def wageWar(self):
        """
        Selects stack of four cards to play when a War is declared. Returns a list.
        """
        if len(self.hand) > 3:
            cards = self.hand.splice(0:3)
        else:
            cards = self.hand.splice(0:)
        return cards


class Game(object):
    def __init__(self):
        self.deck = "23456789A".split("")
        self.discards = []
        self.players = []
    
    def battle(self, players)
        """
        In the event of a War (when both played cards are equal, this compares the stacks of cards played to determine the winner.
        """

    def compareCards(self, cards)
        """
        Compares players' played cards to determine who gets the discards. Accepts list of 2, returns player name who gets the discard pile.
        """

    def dealCards(self, players)
        """
        Shuffles deck and deals equally to each player until deck length = 0.
        """

    def shuffleCards(self)
        """
        Shuffles deck. Returns list.
        """
    
    def winCheck(self, players)
        """
        Checks each player's hand and discard length to see if the game has been decided. Returns player name if True, or False if no winner.
        """