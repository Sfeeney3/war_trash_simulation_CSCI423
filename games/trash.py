import math
import random
import numpy as np





class trash:

    """This class implements the Trash card game."""

    def __init__(self,r_vals) -> None:

        """Initializes the game setup."""
        self.rand = iter(r_vals)  # turn the list into an iterator
        self.discard_deck = [] # Deck where players discard cards
        self.draw_deck = [] # Deck from which players draw cards
        self.player1 = {'deck': [], 'visibility': [], 'array_count': [x for x in range(1,11)]}
        self.player2 = {'deck': [], 'visibility': [], 'array_count': [x for x in range(1,11)]}
        self.player1['visibility'] = ['X'] * self.player1['array_count'][-1]
        self.player2['visibility'] = ['X'] * self.player2['array_count'][-1]

        self.num_turns = 0        # Counter for number of turns taken
        self.transitions = 0      # Counter for transitions in lead
        self.winner = []          # Stores the winner
        self.game_over = False    # Flags if the game is over
        self.deck = self.build_deck()  # Build the primary deck
        self.deck = self.shuffle_cards(self.deck)  # Shuffle the primary deck
        self.initial_set_decks()  # Set the initial decks for players

    def build_deck(self):

        """Builds a deck of cards. Aces low for TRASH"""

        deck = []
        num_cards = 4
        c = 0
        for _ in (range(13)):

            #add 4 of every card to deck
            deck.extend([c+1] * num_cards)

            c = c+1

        return deck

    def shuffle_cards(self,deck:list):

        """Shuffles cards using the Fisher-Yates algorithm."""

       
        n = len(deck)

        for c in range(n):
            r = next(self.rand)  # get the next random value from the file
            p = int((r*(n-c))+c)


            #constant time complexity for this operation
            deck[c], deck[p] = deck[p], deck[c]

            #c = c+1
        return deck 

    #SETTRS

    def initial_set_decks(self):

        """Sets initial decks for the two players."""

        self.player1['deck'].extend(self.deck[10:20])
        self.player2['deck'].extend(self.deck[0:10])
        
        self.draw_deck.extend(self.deck[20:51]) # Update this line
        self.discard_deck.append(self.deck[-1])

        #consistency checks
        #print(len(self.player2['deck']) + len(self.player1['deck']) + len(self.draw_deck) + len(self.discard_deck))

    
    def can_place_card(self, card, player):

        """Checks if a card can be placed in the player's deck."""

        #print('last_call can_place_card!')
        if card == 11:
            if 'X' in player['visibility']:
                return True
        elif card in [12, 13] or card > len(player['deck']):
            return False
        elif player['visibility'][card-1] == 'X':
            return True
        else:
            return False

    def place_card(self, card, player):

        """Places a card in the player's deck and returns the old card."""

        #print('last_call place_card!')
        if card == 11:
            index = player['visibility'].index('X')
        else:
            index = card - 1
        old_card = player['deck'][index]
        player['deck'][index] = card
        player['visibility'][index] = card
        return old_card

    def is_game_over(self):

        """Checks if the game is over."""

        #print('last_call is_game_over!')
        # The game is over when either player's array_count is empty.
        if len(self.player1['array_count']) == 0 or len(self.player2['array_count']) == 0:
            return True
        else: return False

    def is_array_cleared(self, player):

        """Checks if the player's array is cleared."""

        #print('Visibility Array:', player['visibility'])
        if 'X' in player['visibility']:
            #print('Array Not Cleared.')
            return False
        else:
            #print('Array Cleared!')
            return True


    def shuffle_and_reset_deck(self, current_player):

        """Shuffles and resets the player's deck when their array is cleared."""

        #print('last_call shuffle_and_reset_deck!')
        shuffled_deck = current_player['deck'] + self.draw_deck + self.discard_deck
        shuffled_deck = self.shuffle_cards(shuffled_deck)
        #print(len(shuffled_deck))

        array_size = current_player['array_count'][-1]
        current_player['deck'] = shuffled_deck[:array_size]
        self.draw_deck = shuffled_deck[array_size:]
        self.discard_deck = []

        current_player['visibility'] = ['X'] * array_size

        

    def play_turn(self, player, opponent):

        """Plays a single turn of trash for a player."""

        initial_leader = "player" if len(player['array_count']) < len(opponent['array_count']) else "opponent"


        if len(self.draw_deck) == 0:
            self.draw_deck = self.shuffle_cards(self.discard_deck[:-1])
            self.discard_deck = [self.discard_deck[-1]]
        
        if self.can_place_card(self.discard_deck[-1],player):
            card_in_hand = self.discard_deck.pop()
        else:
            card_in_hand = self.draw_deck.pop()


        while self.can_place_card(card_in_hand, player):

            card_in_hand = self.place_card(card_in_hand, player)

            if card_in_hand in [12, 13]:  # Queen and King are represented by 12 and 13
                break

            if self.is_array_cleared(player):
                player['array_count'].pop()
                
                if not self.is_game_over():
                    self.shuffle_and_reset_deck(player)
        
        
        if self.is_array_cleared(player):
            
            if player['array_count']: player['array_count'].pop()
            
            if not self.is_game_over():
                self.shuffle_and_reset_deck(player)
            
        
        self.discard_deck.append(card_in_hand)

        

        current_leader = "player" if len(player['array_count']) < len(opponent['array_count']) else "opponent"
        if initial_leader != current_leader:
            self.transitions += 1






    def play_game(self):

        """Plays the game until a player wins."""

        while not self.is_game_over():

            self.play_turn(self.player1, self.player2)
            self.num_turns += 1

            if self.is_game_over():  # check if the game ended after player1's turn
                break
            

            self.play_turn(self.player2, self.player1)
            self.num_turns += 1
            
        # Determine the winner
        if len(self.player1['array_count']) == 0:
            self.winner = "Player 1"
        else:
            self.winner = "Player 2"
    
    def play_game_check(self):
        
        """Play the game for a set number of rounds for testing purposes."""

        for i in range(100):
            print("player1")
            self.play_turn(self.player1, self.player2)
            self.num_turns += 1

            if self.is_game_over():  # check if the game ended after player1's turn
                break
            print("player2")
            self.play_turn(self.player2, self.player1)
            self.num_turns += 1

        # Determine the winner
        if len(self.player1['array_count']) == 0:
            self.winner = "Player 1"
        else:
            self.winner = "Player 2"

