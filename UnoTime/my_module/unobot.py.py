import random
import string

#unobot
class UnoGame:
    
    """ This class has methods that set up the background aspects of the game, 
    specifically the deck, the player hands, and the first card of the game.
    
    Attributes
    -----------
    deck : empty list
        used to populate the whole uno deck.    
    """
    
    def __init__(self, deck = []):
        self.deck = deck
        
    def deck_gen(self, colors = ['r', 'g', 'b', 'y']): 
        """This generates the deck for the uno game with number/color cards and special cards. 
        The number cards are a combination of one possible color, and one number 1-9.         
        The special cards are +4 cards, skip cards, and +2 cards.
        
        Parameters
        ----------
        colors : list
            These are the colors of the uno deck, and will be used to generate the deck, 
            the player hands, and the first card of the game 
            
        Returns 
        ----------
        deck : list of strings
            This is the full Uno deck 
        """
        x = 0  
        
        for num in range (1,10):
            for color in colors:
                new_card = color + str(num)
                self.deck.append(new_card)
                self.deck.append(new_card)
        
        while x <= 4: 
            self.deck.append('+4')
            self.deck.append('skip')
            self.deck.append('+2')
            x += 1 
            
        return self.deck
     
    #generates 5 random normal cards and make a list of strings 
    def deal(self): 
        x = 0
        hand = []
        
        while x < 5: 
            card = random.choices(self.deck)
            hand += card
            x += 1
            random.shuffle(self.deck)
        return hand
    
    #generates a random normal starting card
    def deal_card(self, colors = ['r', 'g', 'b', 'y']):
        curr_card = random.choice(colors) + str(random.randrange(1,9))
        return curr_card
    
"""This begins the chat, and encompasses the player's turn. 
Checks the input and determines how to proceed. Something like the main method."""
def begin_game():
    
    print(' Welcome to Uno! A card game! (To end the game, input "quit" or "q")\
    \n Below this message, you can see the current card, and your current hand.\
    \n Since you\'re playing against a computer, you won\'t be able to see their cards, but you CAN see how many they have.\
    \n In the input box, you can play anything in your hand, without quotation marks, following the "normal" rules of Uno:\
    \n     Rule 1. Input a card that matches the Current Card in number or color.\
    \n     Rule 2. A +2, +4, or skip can be played on any card, AND any card can be played on a +2, +4, or skip.\
    \n     Rule 3. If you don\'t have a card that works, input "draw" or "d" and you\'ll get ONE card. Then the computer plays.\
    \n     Rule 5. When the computer reaches one card, and they forget to call it, input "uno" and they\'ll have to draw.\
    \n     Rule 5. The "+2", "+4" and "skip" cards will add 2 or 4 cards to your opponent\'s hand, or skip their turn entirely!\
    \n     Rule 6. Have fun, and give me an A :)\
    \n     ------------------------------------')
    
    #gives first card
    curr_card = game.deal_card() 
    turns = 0 
    
    #this checks whether the player's last input was a valid 'uno'
    uno_true = False
    
    #this is the main loop, which goes through the player turn, and checks for win conditions
    player_input = ''
    play = True
    
    while play: 

        turns += 1 
        
        
        # gives a weighted chance that the computer says or forgets Uno 
        if len(computer_hand) == 1: 
            uno_num = random.random()
            if uno_num < 0.7:
                print("\n    Computer: Uno!") 
                comp_uno_true = True 
                
            else: 
                comp_uno_true = False 
                hint_num = random.random()
                if hint_num < 0.3: 
                    print('         ....psst! the computer didn\'t call Uno!')

        elif len(computer_hand) == 0: 
            print('Looks like the computer won this time... try again?')
            break
        
        turn_print(turns, computer_hand, player_hand, curr_card)
        turn = 'player'    
        #sets up the chat box and allows player to provide player_input 
        player_input = input('Your move: ')
        
        if player_input == 'quit' or player_input == 'q':
            print('Good game!')
            play = False                    
       
            
        #checks if input is 'uno', whether they are calling uno for themselves or for the computer, 
        # if for self and valid: sets uno_true to True 
        # if for computer and valid: gives comp one card, if invalid: gives player one card 
        elif player_input == 'uno': 
            
            if len(player_hand) == 1: 
                print("Almost there!")
                
                uno_true = True
                turns -=1

            elif len(computer_hand) == 1:
                if comp_uno_true: 
                    print("The computer already called it! Draw one.")
                    
                    draw(turn)
                    
                else: 
                    print("The computer forgot to say Uno! Nice catch.")
                    
                    draw('computer')
            
                    
        elif player_input == 'draw' or player_input == 'd': 
            print('\nAdding one card!\n')
            
            draw(turn)
            curr_card = computer_turn(curr_card)
            uno_true = False  
            
        elif player_input == 'r':
                player_hand.remove(player_hand[0])
            
        #First checks for player win conditions, where the winning card must be in the player's hand,
        #it must be the last card, the previous entry must have been 'uno', and the card must be playable to win
        elif player_input in player_hand:   
            if len(player_hand) == 1: 
                if uno_true == True: 
                    if is_playable(player_input, curr_card):
                        print("Congrats! You Won!!\nRestart kernel to play again!\n")  
                        win(uno_true, 'player')
                        play = False 
                        break
                
                #checks to make sure player inputs uno   
                elif player_input != 'uno': 
                    print('You didn\'t say Uno!')
                    draw(turn)
                    curr_card = computer_turn(curr_card)      
            
            if player_input == 'skip':
                print('\nNice skip!')
                play_it(player_input)
                curr_card = player_input

            elif player_input == '+2' or player_input == '+4': 
                print('\nThat\'ll show that computer!\n')
                play_it(player_input)
                draw_num(int(player_input[1]), 'computer')
                curr_card = player_input
                curr_card = computer_turn(curr_card)
                
            #num/color card input
            elif (player_input[0] in curr_card or player_input[1] in curr_card or is_playable(player_input, curr_card)):#####curr_card
                print('\nGood play!\n')
                curr_card = player_input
                play_it(player_input)
                curr_card = computer_turn(curr_card)
                
            else:  #accounts for if card is in player hand, but does not work 
                whoopsie()
                turns -= 1
                
            uno_true = False   
    
        else:  #catches all other inputs
            whoopsie()
            turns -= 1

            
def is_playable(card_input, curr_card):
    """Checks if either a card is playable because it is a special card, or if the previous card was speical
    Parameters
    ----------
    card_input : string
        the card to be checked
    curr_card : string
        the card on the top of the deck
    Returns
    ---------
    boolean
        if the card if playable, returns True.
    """
    if card_input in ["+2", "+4", "skip"] or curr_card in ["+2", "+4", "skip"]: 
        return True  
    elif(card_input[0] in curr_card or card_input[1] in curr_card): 
        return True
    else: 
        return False         

def computer_turn(curr_card):   ##### make sure to programm for his uno
    """Checks for computer Uno, then goes through computer hand and removes first applicable card. If 
    no card is applicable, computer draws one 
    Parameters
    ----------
    curr_card : string
        the top card of the deck
        
    Returns
    ---------
    curr_card : string
        the card played by the computer
    """
    turn = 'computer'     
    
    #goes through hand to find first viable card to play. 
    for card in computer_hand:
        
        if card == '+2' or card == '+4':
            computer_hand.remove(card)
            curr_card = card
            draw_num(int(curr_card[1]), 'player')
            print('    Computer move:', curr_card)
            return curr_card
            
        elif card == 'skip':            
            computer_hand.remove(card)
            curr_card = card
            print('    Computer move:', curr_card)
            print('\n    Ah, you got skipped!\n')
            curr_card = computer_turn('skip')
            return curr_card
            
        elif card[0] == curr_card[0] or card[1] == curr_card[1] or is_playable(card, curr_card): #######
            computer_hand.remove(card)
            curr_card = card 
            print('    Computer move:', curr_card) 
            return curr_card
           
        
        comp_uno_true = False 
    
    print('    Computer couldn\'t play! Draws one.')
    draw('computer')
    return curr_card

def draw(person): 
    """Appends one card from the deck to the hand of the appropriate player
    Parameters
    ----------
    person : string
        the person playing the card
    Returns
    --------
    Nothing
    
    """
    new_card = random.choice(the_deck)
    the_deck.remove(new_card)
    
    if person == 'player': 
        player_hand.append(new_card)
    elif person == 'computer': 
        computer_hand.append(new_card)
        
def play_it(player_input):
    """removes the played card from player hand, and updates the current card"""
    played_card = player_hand.index(player_input)
    player_hand.remove(player_hand[played_card])
    curr_card = player_input
           
def draw_num(to_draw, turn):
    """This method adds the appropriate amount of cards to the appropriate player's deck for the +2 or +4 cards.
    Parameters 
    ----------
    curr_card : string
        the current card, +2/4
    turn : string
        the person that played the card  
    Returns
    ---------
    x : int
        the amount of cards to be drawn *for testing
    
    """
    x = 0 
    while x < to_draw: 
        draw(turn)
        x += 1
    return x

#checks for valid win conditions    
def win(winning, player):
    out = ''
    play = True
    if winning:  
        if player == 'player':
            out = ("You won Uno! Great job!!")
            play = False 
            return play
        elif player == 'computer':
            out = ("Looks like the computer won this round... try again?")
            play = False    
            return play
                  
    print(out)
    return play
    
def whoopsie():
    """Used to print out a statement that will tell the user their input had an error."""
    whoopsies = ['Maybe you had a typo?', 'Might want to try that entry again!', 'If you need a new card, input "draw"!']
    out_msg = "That doesn\'t seem right... " + random.choice(whoopsies) + '\n'
    print(out_msg)
    return out_msg

def turn_print(turns, computer_hand, player_hand, curr_card): 
    """Used to print out all the relevant information for each turn."""
    print('\nTurn:', turns, '\n')
    print("Computer's cards:", len(computer_hand))
    print('Current card:', curr_card)
    print('Your hand:', player_hand)

#necessary to run
game = UnoGame()
the_deck = game.deck_gen()
player_hand = game.deal()
computer_hand = game.deal()