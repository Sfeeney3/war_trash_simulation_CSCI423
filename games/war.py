import math
import random
import numpy as np



class war:

    def __init__(self,r_val) -> None:
        
        self.rand = r_val
        self.player1 = {'deck':[], 'winnings_deck': []}
        self.player2 = {'deck':[], 'winnings_deck': []}
        self.num_turns = 0
        self.transitions = 0
        self.winner = []
        self.game_over = False
        self.deck = self.build_deck()
        self.deck = self.shuffle_cards(self.deck)
        self.set_player_decks()

    def build_deck(self):

        deck = []
        num_cards = 4
        c = 1
        for _ in (range(13)):
            #print(c)
            #add 4 of every card to deck
            deck.extend([c+1] * num_cards)

            c = c+1
        return deck

    def shuffle_cards(self,deck:list):

        #Fisher-Yates for shuffling

       
        n = len(deck)

        for c in range(n):
            r = random.uniform(.01,.999) #works for now
            p = int((r*(n-c))+c)
            #print(p)
            #print(c)

            #constant time complexity for this operation
            deck[c], deck[p] = deck[p], deck[c]

            #c = c+1
        return deck    



    def war_turn(self):
        
        if len(self.player1['deck']) == 0:
            self.check_winnings(1)
            if self.game_over: return
        
        if len(self.player2['deck']) == 0:
            self.check_winnings(2)
            if self.game_over: return


        
        p1_card = self.player1['deck'][0]
        p2_card = self.player2['deck'][0]
        

        winnings = [p1_card,p2_card]

        self.player1['deck'].pop(0)
        self.player2['deck'].pop(0)

        end_turn = False
        
        

        while end_turn == False:

            if p1_card > p2_card:
                self.num_turns = self.num_turns + 1
                self.player1['winnings_deck'].extend(winnings)
                end_turn = True
            
            elif p2_card > p1_card:
                self.num_turns = self.num_turns + 1
                self.player2['winnings_deck'].extend(winnings)
                end_turn = True
            
            elif p2_card == p1_card:
                self.num_turns = self.num_turns + 1
                if len(self.player1['deck']) == 0:
                    #self.player2['winnings_deck'].extend(winnings)
                    self.check_winnings(1)
                    if self.game_over: return
        
                elif len(self.player2['deck']) == 0:
                    #self.player1['winnings_deck'].extend(winnings)
                    self.check_winnings(2)
                    if self.game_over: return

                #
                elif(self.game_over == False):
                    p1_card = self.player1['deck'][0]
                    p2_card = self.player2['deck'][0]

                    new_winnings = [p1_card,p2_card]

                    winnings.extend(new_winnings)

                    self.player1['deck'].pop(0)
                    self.player2['deck'].pop(0)
                    
                else:
                    end_turn = True
            #print(len(self.player1['winnings_deck']))
        
        if ((len(self.player2['deck']) + len(self.player2['winnings_deck'])) > (len(self.player1['deck']) + len(self.player1['winnings_deck']))):

            if (len(self.winner)) == 0:

                self.winner.append(2)
            
            

            else:
                #print(self.winner[-1])
                reverse_winner = self.winner[-1]
                if reverse_winner == 2:
                    return
                
                elif reverse_winner == 1:
                    self.transitions = self.transitions +1
                    self.winner.append(2)
        
        if ((len(self.player1['deck']) + len(self.player1['winnings_deck'])) > (len(self.player2['deck']) + len(self.player2['winnings_deck']))):

            if (len(self.winner)) == 0:

                self.winner.append(1)
            
            

            else:
                reverse_winner = self.winner[-1]
                if reverse_winner == 1:
                    return
                
                elif reverse_winner == 2:
                    self.transitions = self.transitions +1
                    self.winner.append(1)
        
        
        #print(self.num_turns)

    def check_win(self, player:int, value:bool):
        #print("Player ", player, "wins!")
        print("war turns: ", self.num_turns,  "transitions:", self.transitions, "last: ", 0)
        self.game_over = value
        
    



    #GETTRS
    def get_num_cards_p1(self,player):

        return self.num_cards[player-1]
    
    #SETTRS
    def set_player_decks(self):
        self.player1['deck'].extend(self.deck[26:52])
        self.player2['deck'].extend(self.deck[0:26])
    
    def check_winnings(self, player:int):

        #print("check winnings call")

        if player == 1:
            if len(self.player1['winnings_deck'])> 0:
                self.player1['deck'] = self.shuffle_cards(self.player1['winnings_deck'].copy())
                self.player1['winnings_deck'] = []
            else:
                self.check_win(2,True)
        
        if player == 2:
            if len(self.player2['winnings_deck'])> 0:
                self.player2['deck'] = self.shuffle_cards(self.player2['winnings_deck'].copy())
                self.player2['winnings_deck'] = []
            else:
                self.check_win(1,True)


