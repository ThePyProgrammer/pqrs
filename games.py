from random import randint, choice
import random

def guessinggame(maxn=100):
    guesses = 0
    userans = int(input("\nI have guessed a number from 1 to "+str(maxn)+"(inclusive). Guess: "))
    actualans = randint(1, maxn)
    while userans != actualans:
        guesses += 1
        if userans > actualans:
            userans = int(input("Your guess was Too High. Guess: "))
        elif userans < actualans:
            userans = int(input("Your guess was Too Low. Guess: "))
    if userans == actualans:
        cont = str(input("Your guess was correct. \nIt took you a total of "+str(guesses)+" guesses! \nDo you want to play again? (Yes or No): "))
        if cont == "No":
            return 
        guessinggame()

def rpsls(maxpts=10):
    chars = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    print('Rules:\n1. You must enter one of the following characters:', ', '.join(chars), '\nThe computer will assign a random choice and the duel shall begin.')
    print('The rules are simple:', 'Scissors cuts Paper', 'Paper covers Rock', 'Rock crushes Lizard', 'Lizard poisons Spock', 'Spock smashes Scissors', 'Scissors decapitates Lizard', 'Lizard eats Paper', 'Paper disproves Spock', 'Spock vaporizes Rock', '(and as it always has) Rock crushes Scissors', sep='\n\t')
    rulessimplic = ['Scissors cuts Paper', 'Paper covers Rock', 'Rock crushes Lizard', 'Lizard poisons Spock', 'Spock smashes Scissors', 'Scissors decapitates Lizard', 'Lizard eats Paper', 'Paper disproves Spock', 'Spock vaporizes Rock', 'Rock crushes Scissors']
    lst = [(i.split()[0], i.split()[-1]) for i in rulessimplic]
    uipts = compts = 0
    while uipts < maxpts and compts < maxpts:
        uchar = input('Enter character: ')
        while uchar not in chars:
            uchar = input('Reenter your character: ')
        comchar = choice(chars)
        print('You have chosen:', uchar, '\nThe computer has chosen:', comchar)
        if (uchar, compchar) in lst:
            print('Yay! You won!')
            uipts += 1
        else:
            print('Aww! You lost!')
            compts += 1
        print('Current Score: You: ', uipts, ', Computer: ', compts, '.', sep='')
    
    if uipts > compts:
        print('You have won with a total of ', uipts, '!', sep='')
        print('Good Job!')
    else:
        print('The Computer has won with a total of ', compts, '!', sep='')
        print("It's ok. You'll do better next time.")
    return 

def rps(maxpts=10):
    chars = ['Rock', 'Paper', 'Scissors']
    print('Rules:\n1. You must enter one of the following characters:', ', '.join(chars), '\nThe computer will assign a random choice and the duel shall begin.')
    print('The rules are simple:', 'Scissors cuts Paper', 'Paper covers Rock', '(and as it always has) Rock crushes Scissors', sep='\n\t')
    rulesdict = {'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock'}
    uipts = compts = 0
    while uipts < maxpts and compts < maxpts:
        uchar = input('Enter character: ')
        while uchar not in chars:
            uchar = input('Reenter your character: ')
        comchar = choice(chars)
        print('You have chosen:', uchar, '\nThe computer has chosen:', comchar)
        if rulesdict[uchar] == comchar:
            print('Yay! You won!')
            uipts += 1
        else:
            print('Aww! You lost!')
            compts += 1
        print('Current Score: You: ', uipts, ', Computer: ', compts, '.', sep='')
    
    if uipts > compts:
        print('You have won with a total of ', uipts, '!', sep='')
        print('Good Job!')
    else:
        print('The Computer has won with a total of ', compts, '!', sep='')
        print("It's ok. You'll do better next time.")
    return 

def rpslssbwg(maxpts=10):
    chars = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock', 'Spider-Man', 'Batman', 'Wizard', 'Glock']
    print('Rules:\n1. You must enter one of the following characters:', ', '.join(chars), '\nThe computer will assign a random choice and the duel shall begin.')
    print('The rules are simple:', 'Scissors cuts Paper', 'Paper covers Rock', 'Rock crushes Lizard', 'Lizard poisons Spock', 'Spock zaps Wizard', 'Wizard stuns Batman', 'Batman scares Spider-Man', 'Spider-Man disarms Glock', 'Glock breaks Rock', 'Rock interrupts Wizard', 'Wizard burns Paper', 'Paper disproves Spock', 'Spock befuddles Spider-Man', 'Spider-Man defeats Lizard', 'Lizard confuses Batman (because he looks like Killer Croc)', 'Batman dismantles Scissors', 'Scissors cuts Wizard', 'Wizard transforms Lizard', 'Lizard eats Paper', 'Paper jams Glock', 'Glock kills Batman\'s mom', 'Batman hangs Spock', 'Spock smashes Scissors', 'Scissors cuts Spider-Man', 'Spider-Man annoys Wizard', 'Wizard melts Glock', 'Glock dents Scissors', 'Scissors decapitates Lizard', 'Lizard is too small for Glock', 'Glock shoots Spock', 'Spock vaporisers Rock', '(and as it always has) Rock crushes Scissors', sep='\n\t')          
    uipts = compts = 0
    tup = ('Scissors cuts Paper', 'Paper covers Rock', 'Rock crushes Lizard', 'Lizard poisons Spock', 'Spock zaps Wizard', 'Wizard stuns Batman', 'Batman scares Spider-Man', 'Spider-Man disarms Glock', 'Glock breaks Rock', 'Rock interrupts Wizard', 'Wizard burns Paper', 'Paper disproves Spock', 'Spock befuddles Spider-Man', 'Spider-Man defeats Lizard', 'Lizard confuses Batman', 'Batman dismantles Scissors', 'Scissors cuts Wizard', 'Wizard transforms Lizard', 'Lizard eats Paper', 'Paper jams Glock', 'Glock kills Batman', 'Batman hangs Spock', 'Spock smashes Scissors', 'Scissors cuts Spider-Man', 'Spider-Man annoys Wizard', 'Wizard melts Glock', 'Glock dents Scissors', 'Scissors decapitates Lizard', 'Lizard is too small for Glock', 'Glock shoots Spock', 'Spock vaporisers Rock', 'Rock crushes Scissors')
    lst = [(i.split()[0], i.split()[-1]) for i in tup]
    while uipts < maxpts and compts < maxpts:
        uchar = input('Enter character: ')
        while uchar not in chars:
            uchar = input('Reenter your character: ')
        comchar = choice(chars)
        print('You have chosen:', uchar, '\nThe computer has chosen:', comchar)
        if (uchar, compchar) in lst:
            print('Yay! You won!')
            uipts += 1
        else:
            print('Aww! You lost!')
            compts += 1
        print('Current Score: You: ', uipts, ', Computer: ', compts, '.', sep='')
    
    if uipts > compts:
        print('You have won with a total of ', uipts, '!', sep='')
        print('Good Job!')
    else:
        print('The Computer has won with a total of ', compts, '!', sep='')
        print("It's ok. You'll do better next time.")
    return 

def obsession():
    # remember to import the libraries needed
    # Use one list or more to represent the status
    # of the rings for both players. 
    Rings = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] # Player 0-pos then Player 1-pos
    # to display the status of rings of both player based 
    def display_rings():
        
        print("-----------player1-----------") #Player 1 side
        for count in range(1, 11): #labels
            print(format(str(count), '3s'),end = '')
        print('')
        
        for j in range(3): # The line, like the ring position
            for i in range(10): # Position 1 to 10
                if Rings[1][i] == j:
                    print(format("O", "3s"), end = "") # O for ring
                else:
                    print(format(".", "3s"), end = "") # . for empty
            print('\n', end = '') #making a new line

        print('') #line seperating the sides
        
        for j in range(2, -1, -1): #ring position
            for i in range(10): # which ring
                if Rings[0][i] == j:
                    print(format("O", "3s"), end = "") # O for ring
                else:
                    print(format(".", "3s"), end = "") # . for empty
            print('\n', end = '') #making a new line
            
        for count in range(1, 11):
            print(format(str(count), '3s'),end = '')
        print('')

        print("-----------player0-----------")
        
        
    # to display whose turn
    def display_player1():
            print("*******************************")
            print("*              ___            *")
            print("*             /__ |           *")
            print("*               | |           *")
            print("*               | |           *")
            print("*it is player   |_|'s turn.   *")
            print("*******************************")

    def display_player0():
            print("*******************************")
            print("*              _____          *")
            print("*             /  _  \         *")
            print("*            /  / \  \        *")
            print("*            \  \_/  /        *")
            print("*it is player \_____/'s turn. *")
            print("*******************************")

    # to decide who starts the game
    def start_game():
        '''
        1) Randomly make 2 numbers for players
        2) Check if there is a 'winner'
        3) Return the one with teh greater num
        '''
        print('Both players roll dice...')
        dice0 = random.randint(1, 6) # Dice num for 0
        dice1 = random.randint(1, 6) # Dice num for 1
        print("Player 0's die is " + str(dice0), "Player 1's die is " + str(dice1), sep = '\n') # Player die number printed
        while dice0 == dice1: #If it is the same
            print('so they roll again...')
            dice0 = random.randint(1, 6) # New dice num for 0
            dice1 = random.randint(1, 6) # New dice num for 1
            print("Player 0' die is " + str(dice0), "Player 1' die is " + str(dice1), sep = '\n') # Player die number printed
        if dice1 > dice0:
            print('Player 1 starts the game first')
            return 1
        else:
            print('Player 0 starts the game first')
            return 0

    # to randomly generate 2 six-sided dice throws 
    def roll():
        return [random.randint(1, 6), random.randint(1, 6)]

    # to read in the user input and to validate the input
    def read_input(dice, current_player, player0_positions, player1_positions):
        while True:
            whose_ring = input('Whose ring to move? 0 for player 0 and 1 for player 1. \n')
            while whose_ring != '0' and whose_ring != '1': #Getting Whose_Ring value
                print('Please enter integer 0 or 1 for the value of the player. ')
                whose_ring = input('Whose ring to move? 0 for player 0 and 1 for player 1. \n')
            whose_ring = int(whose_ring)

            valid = [str(x) for x in dice] + [str(sum(dice))] #vaild positions
            valid = [str(x) for x in valid if int(x) in range(1,11)]
            position = input('Which position to move? \n')
            while position not in valid: #Getting position value
                print('please enter the valid value for the position')
                position = input('Which position to move? \n')
            position = int(position)
        
            if whose_ring != current_player: #if moving opponent's
                if (whose_ring == 0 and player0_positions[position - 1] == 1) \
                   or (whose_ring == 1 and player1_positions[position - 1] == 1) :
                    return whose_ring, position
                print('That position can not be moved down.')
                
            else: #if moving self
                if (whose_ring == 1 and player1_positions[position - 1] == 0) \
                   or (whose_ring == 0 and player0_positions[position - 1] == 0) :
                    return whose_ring, position
                print('That position can not be moved up.') 
                
    # simulate the action of the action(s) 
    def one_turn(current_player):
        display_rings() #The Rings
        print('\n**************', '*   Roll...  *', '************** ', sep = '\n')
        dice = roll()
        print('the two dice are ' + str(dice[0]) + ' and ' + str(dice[1]) + ' .')
        if sum(dice) > 10:
             valid_moves = [ [ num for num in dice if Rings[current_player][num - 1] == 0],  [ num for num in dice if Rings[1 - current_player][num - 1] == 1 ] ]
        else:
            valid_moves = [ [ num for num in (dice + [sum(dice)]) if Rings[current_player][num - 1] == 0],  [ num for num in (dice + [sum(dice)])if Rings[1 - current_player][num - 1] == 1 ] ]
            
        #valid moves = [[self], [opponent]]
        while len(valid_moves[0]) > 0 or len(valid_moves[1]) > 0:
                whose_ring, position = read_input(dice, current_player, Rings[0], Rings[1])
                Rings[whose_ring][position - 1] = 1 - Rings[whose_ring][position - 1]
                if position == sum(dice):
                    dice = []
                    break
                elif dice == []:
                    break
                else:
                    dice.remove(position)
                valid_moves = [ [ num for num in (dice + [sum(dice)]) if Rings[current_player][num - 1] == 0],  [ num for num in (dice + [sum(dice)])if Rings[1 - current_player][num - 1] == 1 ] ]

        for pos in Rings[current_player]:
            if pos == 0:
                return dice
        return [-1]
    # to put everything together
    def gameplay():
        player = start_game()
        while True:
            if player == 0:
                display_player0()
            else:
                display_player1()
            if one_turn(player) == [-1]:
                winner = player
                break
            input('There is no valid move. This turn is finishing. Press anyting to continue ')
            player = 1 - player # Other Player
            for index in range(10):
                if Rings[player][index] == 1:
                    Rings[player][index] = 2
        display_rings()
        print('player', str(winner), 'is the winner!') 
        
    gameplay()
    return 
