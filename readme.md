# PyWar
## "War" card game written in Python

## Gameplay
* Two players, one human, one computer
* In each round, each player plays the top card in their hand
* The player who plays the highest card adds the two cards to their reserve pile
* If the cards are equal, a WAR sequence occurs
  * Each player plays three face-down cards and one face-up card; the player whose fourth card is highest takes the entire pile
* When all cards in a hand are played, the player picks up the reserve pile, and the card count for both sides is announced
* When one player has zero cards in hand AND zero cards in reserve, the other player wins

## Further ideas for interactivity
* Ask user to guess the winner based on the options chosen:
  * Choose deck size
  * Alter deck composition (e.g., lots of duplicates or no duplicates)
  * To shuffle or not to shuffle?  What if only one player shuffles their hand?
  * Calculated hand value

## Further ideas for testing decks
* Small decks (absolute minimum is 10)
* Very large decks (100? 1000?)
* Odd-numbered decks (does this even work?)
* Oddly-weighted dealing -- what happens when one player starts with all the aces?
