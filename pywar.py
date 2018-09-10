"""
* Two players, one human, one computer
* In each round, each player plays the top card in their hand
* The player who plays the highest card adds the two cards to their reserve pile
* If the cards are equal, a WAR sequence occurs
* * Each player plays three face-down cards and one face-up card; the player whose fourth card is highest takes the entire pile
* When all cards in a hand are played, the player picks up the reserve pile, and the card count for both sides is announced
* When one player has zero cards in hand AND zero cards in reserve, the other player wins
"""

import classes as Classes

def Game():
    """
    print("Welcome to the card game. This means WAR!")
    print("Who are the two players?")

    name1 = raw_input("Player 1: ")
    name2 = raw_input("Player 2: ")
    
    player1 = Player(name1)
    player2 = Player(name2)
    """
    
    player1 = Classes.Player("Bob")
    player2 = Classes.Player("Jenni")

    players = [player1, player2]

    myDeck = Classes.Deck()
    myDeck.shuffle()
    
    myDeck.dealCards(players)

    winner = False

    while not winner:        
        cardsPlayed = []
        for each in players:
            card = each.playCard()
            cardsPlayed.append(card)
            print(each.name, " has played ", card)
        myDeck.compareCards(players, cardsPlayed)
   
Game()