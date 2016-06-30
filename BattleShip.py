## BATTLESHIP
from random import randint

ColTrans = {
'a': 0,
'b': 1,
'c': 2,
'd': 3,
'e': 4,
'f': 5,
'g': 6,
'h': 7,
'i': 8,
'j': 9
}



hitcheck = {

'ship1a': False,
'ship1b': False,

'ship2a': False,
'ship2b': False,
'ship2c': False,

'ship3a': False,
'ship3b': False,
'ship3c': False,

'ship4a': False,
'ship4b': False,
'ship4c': False,
'ship4d': False,

'ship5a': False,
'ship5b': False,
'ship5c': False,
'ship5d': False,
'ship5e': False
}

misscheck = {}

ships = 5


def InitPositions():
    ships = ['ship1','ship2','ship3','ship4','ship5']
    success = False
    positions = {}
    while success == False:
        x = 0
        for item in ships:
            positions[item + 'a'] = [randint(0,9), randint(0,9)]
            
            dir = randint(0,1)
            pos2 = randint(0,1)
            pos3 = randint(0,1)
            pos4 = randint(0,1)
            pos5 = randint(0,1)

            if dir == 0: ## Horizontal

                if pos2 == 0: ## To the Left
                    positions[item +'b'] = [positions[item + 'a'][0],positions[item + 'a'][1] - 1]
                else:
                    positions[item + 'b'] = [positions[item + 'a'][0],positions[item + 'a'][1] + 1]
                

            else:
            
                if pos2 == 0:
                    positions[item + 'b'] = [positions[item + 'a'][0] - 1, positions[item + 'a'][1]]
                else:
                    positions[item + 'b'] = [positions[item + 'a'][0] + 1, positions[item + 'a'][1]]
            if '1' not in item:
                if dir == 0:
                    if pos2 == 0:
                        if pos3 == 0:
                            positions[item + 'c'] = [positions[item + 'b'][0], positions[item + 'b'][1] - 1]
                        else:
                            positions[item + 'c'] = [positions[item + 'b'][0], positions[item + 'b'][1] + 2]
                    else:
                        if pos3 == 0:
                            positions[item + 'c'] = [positions[item + 'b'][0], positions[item + 'b'][1] - 2]
                        else:
                            positions[item + 'c'] = [positions[item + 'b'][0], positions[item + 'b'][1] + 1]
                else:
                    if pos2 == 0:
                        if pos3 == 0:
                            positions[item + 'c'] = [positions[item + 'b'][0] - 1, positions[item + 'b'][1]]
                        else:
                            positions[item + 'c'] = [positions[item + 'b'][0] + 2, positions[item + 'b'][1]]
                    else:
                        if pos3 == 0:
                            positions[item + 'c'] = [positions[item + 'b'][0] - 2, positions[item + 'b'][1]]
                        else:
                            positions[item + 'c'] = [positions[item + 'b'][0] + 1, positions[item + 'b'][1]]
            if '4' in item or '5' in item:
                if dir == 0:
                    if pos3 == 0:
                        if pos4 == 0:
                            positions[item + 'd'] = [positions[item + 'c'][0], positions[item + 'c'][1] - 1]
                        else:
                            positions[item + 'd'] = [positions[item + 'c'][0], positions[item + 'c'][1] + 3]
                    else:
                        if pos4 == 0:
                            positions[item + 'd'] = [positions[item + 'c'][0], positions[item + 'c'][1] - 3]
                        else:
                            positions[item + 'd'] = [positions[item + 'c'][0], positions[item + 'c'][1] + 1]
                else:
                    if pos3 == 0:
                        if pos4 == 0:
                            positions[item + 'd'] = [positions[item + 'c'][0] - 1, positions[item + 'c'][1]]
                        else:
                            positions[item + 'd'] = [positions[item + 'c'][0] + 3, positions[item + 'c'][1]]
                    else:
                        if pos4 == 0:
                            positions[item + 'd'] = [positions[item + 'c'][0] - 3, positions[item + 'c'][1]]
                        else:
                            positions[item + 'd'] = [positions[item + 'c'][0] + 1, positions[item + 'c'][1]]

            if '5' in item:
                if dir == 0:
                    if pos4 == 0:
                        if pos5 == 0:
                            positions[item + 'e'] = [positions[item + 'd'][0], positions[item + 'd'][1] - 1]
                        else:
                            positions[item + 'e'] = [positions[item + 'd'][0], positions[item + 'd'][1] + 4]
                    else:
                        if pos5 == 0:
                            positions[item + 'e'] = [positions[item + 'd'][0], positions[item + 'd'][1] - 4]
                        else:
                            positions[item + 'e'] = [positions[item + 'd'][0], positions[item + 'd'][1] + 1]
                else:
                    if pos4 == 0:
                        if pos5 == 0:
                            positions[item + 'e'] = [positions[item + 'd'][0] - 1, positions[item + 'd'][1]]
                        else:
                            positions[item + 'e'] = [positions[item + 'd'][0] + 4, positions[item + 'd'][1]]
                    else:
                        if pos5 == 0:
                            positions[item + 'e'] = [positions[item + 'd'][0] - 4, positions[item + 'd'][1]]
                        else:
                            positions[item + 'e'] = [positions[item + 'd'][0] + 1, positions[item + 'd'][1]]
            
        for item in positions:
            c = 0
            check1 = positions[item][0]
            check2 = positions[item][1]
            if check1 == -1 or check1 == 10 or check2 == -1 or check2 == 10:
                x = 100
            
            
            for thing in positions:
                if positions[item] == positions[thing]:
                    c += 1
            if c > 1:
                x = 100
        if x != 100:
            success = True
    return positions

def printboard(positions,hitcheck, misscheck, ships):
    print '\n' * 4
    print '             1     2     3     4     5     6     7     8     9    10'
    print '         ______________________________________________________________'
    print '        |                                                              |'
    letters = ['a','b','c','d','e','f','g','h','i','j']
    for row in range(10):
        print '     %s  | ' % letters[row],
        for col in range(10):
            x = 0
            for item in positions:
                if positions[item] == [row, col] and hitcheck[item] == True:
                    print '  X  ',
                    x = 100
            for item in misscheck:
                if misscheck[item] == [row, col]:
                    print '  O  ',
                    x = 100
            if x != 100:
                print '  -  ',
            
            col += 1
        print '|'
        
        if row != 9:
            print '        |                                                              |'
            print '        |                                                              |'
        else:
            print '        |                                                              |'
            print '        |______________________________________________________________|'            
            print
        row += 1
    if ships != 0:
        print '          BATTLESHIP                      %s Ships Remaining' % ships
    print '\n' * 6

def show(positions):
    print '\n' * 6
    print '             1     2     3     4     5     6     7     8     9    10'
    print '         ______________________________________________________________'
    print '        |                                                              |'
    row = 0
    letters = ['a','b','c','d','e','f','g','h','i','j']
    while row < 10:
        col = 0
        print '     %s  | ' % letters[row],
        while col < 10:
            x = 0
            for item in positions:
                if positions[item] == [row, col]:
                    print '  S  ',
                    x = 100

            if x != 100:
                print '  -  ',
            
            col += 1
        print '|'
        
        if row != 9:
            print '        |                                                              |'
            print '        |                                                              |'
        else:
            print '        |                                                              |'
            print '        |______________________________________________________________|'            
            print
        row += 1
    print '\n' * 6
    
    
positions = InitPositions()
printboard(positions,hitcheck,misscheck,ships)

Winner = False

p = 0
moves = 0
quit_check=False
while Winner==False and quit_check==False:
    x = 0
    print ' Choose a letter and number to guess a position (e.g. f 7)'
    print
    guess = raw_input(' Your guess: ').lower()
    if guess.lower()=='quit':
        if 'y' in raw_input('Are you sure you want to quit? (y/n): ').lower():
            quit_check=True
            continue
        else:
            x=100
    if guess.lower() == 'show':
        show(positions)
        x = 100
        raw_input(' Please Press Enter')
        
    if '10' not in guess:
        guess = guess.replace('',' ')
    else:
        guess = guess.replace('10',' 10')
        
    try:    
        guess = guess.split()
    except:
        print ' Incorrect Input'
        x = 100
        raw_input(' Please Press Enter')
        
    if len(guess) != 2 and x != 100:
        print ' Incorrect Input'
        x = 100
        raw_input(' Please Press Enter')
        
    if x != 100 and guess[0] in 'a b c d e f g h i j' and guess[0] != ' ' and guess[1] in '1 2 3 4 5 6 7 8 9 10' and guess[1] != ' ':
    
        for thing in ColTrans:
            if guess[0] == thing:
                guess[0] = int(ColTrans[thing])
        guess[1] = int(guess[1]) - 1
        
        
        for item in misscheck:
            if misscheck[item] == guess:
                print ' You have already guessed there'
                x = 100
                raw_input()
        if x != 100:
            for item in positions:
                if guess == positions[item]:
                    x = 100
                    if hitcheck[item] == True:
                        print ' You have already guessed there'
                        raw_input()
                    else:
                        print ' That\'s a Hit!'
                        hitcheck[item] = True
                        moves += 1
                        raw_input()
                        if '1' in item:
                            if hitcheck['ship1a'] == hitcheck['ship1b']:
                                print ' You sank a battleship!'
                                ships -= 1
                                raw_input()
                        if '2' in item:
                            if hitcheck['ship2a'] == hitcheck['ship2b'] == hitcheck['ship2c']:
                                print ' You sank a battleship!'
                                ships -= 1
                                raw_input()
                        if '3' in item:
                            if hitcheck['ship3a'] == hitcheck['ship3b'] == hitcheck['ship3c']:
                                print ' You sank a battleship!'
                                ships -= 1
                                raw_input()
                        if '4' in item:
                            if hitcheck['ship4a'] == hitcheck['ship4b'] == hitcheck['ship4c'] == hitcheck['ship4d']:
                                print ' You sank a battleship!'
                                ships -= 1
                                raw_input()
                        if '5' in item:
                            if hitcheck['ship5a'] == hitcheck['ship5b'] == hitcheck['ship5c'] == hitcheck['ship5d'] == hitcheck['ship5e']:
                                print ' You sank a battleship!'
                                ships -= 1
                                raw_input()
        
                            
                    
        if x != 100:
            print ' Sorry You Missed'
            r = '%s' % p
            misscheck[r] = guess
            p += 1
            moves += 1
            raw_input()
    
    
    elif x != 100:
        print
        print ' Incorrect Input'
        print
        raw_input(' Please Press Enter')
    

    
            


    count = 0
    for item in hitcheck:
        if hitcheck[item] == False:
            count += 1
    if count == 0:
        Winner = True
    printboard(positions,hitcheck,misscheck,ships)
        
if quit_check:
    print '\n Game has been ended.'
else:
    print ' Congratulations! You finished the game in %s moves!' % moves        

