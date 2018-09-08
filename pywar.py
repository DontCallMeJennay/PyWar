"""
* Two players, one human, one computer
* In each round, each player plays the top card in their hand
* The player who plays the highest card adds the two cards to their reserve pile
* If the cards are equal, a WAR sequence occurs
* * Each player plays three face-down cards and one face-up card; the player whose fourth card is highest takes the entire pile
* When all cards in a hand are played, the player picks up the reserve pile, and the card count for both sides is announced
* When one player has zero cards in hand AND zero cards in reserve, the other player wins
"""

import random

class Player(object):
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.reserve = []

    def playCard(self):
        """
        Removes top card from player's deck and adds it to game discard pile. Returns a string.
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
        # print("Picking up", len(self.hand), " cards from reserve.", self.hand)

    def wageWar(self):
        """
        Selects stack of four cards to play when a War is declared. Returns a list.
        """
        if len(self.hand) > 3:
            cards = self.hand.splice[0:3]
        else:
            cards = self.hand.splice[0:]
        return cards


class Deck(object):
    def __init__(self):
        self.deck = "1 2 3 1 2 3 4 5".split(" ")
        self.winCount = len(self.deck)
        self.discards = []
        self.players = []
    
    def battle(self, players):
        """
        In the event of a War (when both played cards are equal, this compares the stacks of cards played to determine the winner.
        """
        cards1 = players[0].wageWar()
        cards2 = players[1].wageWar()
        if cards1[3] == cards2[3]:
            return self.battle(players)
        elif cards1[3] > cards2[3]:
            print(players[0].name, " won the war!")
            players[0].reserve.extend(cards1)
            players[0].reserve.extend(cards2)
        else:
            print(players[1].name, " won the war!")
            players[1].reserve.extend(cards1)
            players[1].reserve.extend(cards2)           

    def compareCards(self, players, cards):
        """
        Compares players' played cards to determine who gets the discards.
        """
        # print(tuples)
        if cards[0] == cards[1]:
            print("WAR!")
            # self.battle()
        elif cards[0] > cards[1]:
            players[0].reserve.extend(cards)
            print(players[0].name, " takes the cards")
            print(players[0].name, " has ", len(players[0].hand), " cards in hand and ", len(players[0].reserve), " cards in reserve.")
        else:
            players[1].reserve.extend(cards)
            print(players[1].name, " takes the cards")
            print(players[0].name, " has ", len(players[1].hand), " cards in hand and ", len(players[1].reserve), " cards in reserve.")
        
       

    def dealCards(self, players):
        """
        Shuffles deck and deals equally to each player until deck length = 0.
        Assumes PLAYERS variable is a list of 2 class instances.
        """
        b = True
        while len(self.deck) > 0:
            card = self.deck.pop(0)
            if b:                
                players[0].hand.append(card)
            else:
                players[1].hand.append(card)
            b = not b
        print("First deal: players have ", len(players[0].hand), " cards in hand.")

    def shuffle(self):
        """
        Shuffles game deck. No return.
        """
        dl = len(self.deck)-1
        tmp = ""
        for i in range(0, dl):
            r = random.randint(0, dl)
            tmp = self.deck[i]
            self.deck[i] = self.deck[r]
            self.deck[r] = tmp
        # print(self.deck)
    
    def winCheck(self, player):
        """
        Checks each player's hand and discard length to see if the game has been decided. Returns player name if True, or False if no winner.
        """
        if len(player.hand) == 0 and len(player.reserve) == self.winCount:
            print(player.name, "wins the war! Thanks for playing!")
            return 0

def Game():
    """
    print("Welcome to the card game. This means WAR!")
    print("Who are the two players?")

    name1 = raw_input("Player 1: ")
    name2 = raw_input("Player 2: ")
    
    player1 = Player(name1)
    player2 = Player(name2)
    """
    
    player1 = Player("Bob")
    player2 = Player("Jenni")

    players = [player1, player2]

    myDeck = Deck()
    myDeck.shuffle()
    
    myDeck.dealCards(players)

    winner = False

    while not winner:        
        cardsPlayed = []
        for each in players:
            card = each.playCard()
            cardsPlayed.append(card)
            print(each.name, " has played ", card)
            if len(each.hand) == 0:
                winner = True
        myDeck.compareCards(players, cardsPlayed)
   
Game()