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
import time

def Game():
    """
    print("Welcome to the card game. This means WAR!")
    print("Who are the two players?")

    name1 = raw_input("Player 1: ")
    name2 = raw_input("Player 2: ")
    
    player1 = Player(name1)
    player2 = Player(name2)
    """
    
    player1 = Classes.Player("Player 1")
    player2 = Classes.Player("Player 2")

    players = [player1, player2]

    myDeck = Classes.Deck()
    myDeck.shuffle(myDeck.deck)
    
    myDeck.deal_cards(players)

    winner = False

    while not winner:        
        played = []
        print("[Game loop]")
        print("[Total cards on board: {}]".format(len(player1.hand) + len(player1.reserve) + len(player2.hand) + len(player2.reserve)))
        myDeck.win_check(players)
        for each in players:
            total = len(each.hand) + len(each.reserve)
            print("{} now has a total of {} cards.".format(each.name, total))
            if total > 0:
                card = each.play_card()
                played.append(card)
                print("{} plays the {} of {}!".format(each.name, card[0], card[1]))
            else:
                myDeck.win_check(players)
        #time.sleep(1)
        myDeck.compare_cards(players, played)
        #time.sleep(5)
   
Game()