import random


class Player(object):
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.reserve = []

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


class Deck(object):
    def __init__(self):
        self.deck = self.make_std_deck()
        self.discards = []
        self.players = []
        self.CARD_RANKS = {
            "2": 0,
            "3": 1,
            "4": 2,
            "5": 3,
            "6": 4,
            "7": 5,
            "8": 6,
            "9": 7,
            "10": 8,
            "Jack": 9,
            "Queen": 10,
            "King": 11,
            "Ace": 12
        }
        self.rounds = 0
        self.WIN_COUNT = len(self.deck)

    def battle(self, players):
        """
        In the event of a War (when both played cards are equal, this compares the stacks of cards played to determine the winner.
        """
        cards1 = players[0].draw_for_battle()
        cards2 = players[1].draw_for_battle()
        self.discards.extend(cards1)
        self.discards.extend(cards2)
        if len(cards1) < 4:
            print("\n{} loses because they don't have enough cards!\n".format(
                players[0].name))
            print("{} wins the war after {} rounds! Thanks for playing!".format(
                players[1].name, self.rounds))
            exit()
        if len(cards2) < 4:
            print("\n{} loses because they don't have enough cards!\n".format(
                players[1].name))
            print("{} wins the war after {} rounds! Thanks for playing!\n\n".format(
                players[0].name, self.rounds))
            exit()
        print("\nBATTLE: {} of {} vs {} of {}".format(
            cards1[3][0], cards1[3][1], cards2[3][0], cards2[3][1]))

        a = self.CARD_RANKS[cards1[3][0]]
        b = self.CARD_RANKS[cards2[3][0]]

        if a == b:
            return self.battle(players)
        elif a > b:
            print("{} won the battle!".format(players[0].name))
            players[0].reserve.extend(self.discards)
        else:
            print("{} won the battle!".format(players[1].name))
            players[1].reserve.extend(self.discards)
        print("Player 1's new card count: {}".format(
            len(players[0].reserve)+len(players[0].hand)))
        print("Player 2's new card count: {}\n".format(
            len(players[1].reserve)+len(players[1].hand)))
        self.discards = []
        return

    def count_rounds(self):
        self.rounds += 1

    def compare_cards(self, players, cards):
        """
        Compares players' played cards to determine who gets the discards. Input is players and two card tuples; output is player who gets the cards.
        Adding court cards makes this a bit more complicated...
        """
        a = self.CARD_RANKS[cards[0][0]]
        b = self.CARD_RANKS[cards[1][0]]

        if a == b:
            print("\nWAR!\nEach player counts out three cards face-down, then draws one more.\n")
            self.discards = cards
            self.battle(players)
        elif a > b:
            players[0].reserve.extend(cards)
            print("\n{} takes the cards.\n".format(players[0].name))
        else:
            players[1].reserve.extend(cards)
            print("\n{} takes the cards.\n".format(players[1].name))

    def deal_cards(self, players):
        """
        Deals deck equally to each player until deck length = 0.
        Assumes PLAYERS variable is a list of 2 class instances.
        """
        b = True
        while len(self.deck) > 0:
            card = self.deck.pop()
            if b:
                players[0].hand.append(card)
            else:
                players[1].hand.append(card)
            b = not b
        print("After the first deal, {} has {} cards in hand and {} has {}.".format(
            players[0].name, len(players[0].hand), players[1].name, len(players[1].hand)))

    def make_std_deck(self):
        values = "Ace King Queen Jack 10 9 8 7 6 5 4 3 2".split(" ")
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        deck = []
        for val in values:
            for suit in suits:
                deck.append((val, suit))
        return deck

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

    def win_check(self, players):
        """
        Checks each player's hand and discard length to see if the game has been decided. Returns player name if True, or False if no winner.
        """
        for each in players:
            hl = len(each.hand)
            rl = len(each.reserve)
            if hl + rl == self.WIN_COUNT:
                print("{} wins the war after {} rounds! Thanks for playing!".format(
                    each.name, self.rounds))
                exit()

        self.count_rounds()
