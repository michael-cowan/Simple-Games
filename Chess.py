### FULLY FUNCTIONAL COMMAND-BASED CHESS GAME THAT PRINTS INTO PYTHON SHELL

whitepieces = {
'pawn1' : ['     ','  O  ',' OOO ','  1  '],
'pawn2' : ['     ','  O  ',' OOO ','  2  '],
'pawn3' : ['     ','  O  ',' OOO ','  3  '],
'pawn4' : ['     ','  O  ',' OOO ','  4  '],
'pawn5' : ['     ','  O  ',' OOO ','  5  '],
'pawn6' : ['     ','  O  ',' OOO ','  6  '],
'pawn7' : ['     ','  O  ',' OOO ','  7  '],
'pawn8' : ['     ','  O  ',' OOO ','  8  '],
'rook1' : ['     ','O O O','OOOOO',' O1O '],
'rook2' : ['     ','O O O','OOOOO',' O2O '],
'knight1' : ['  OO ','  OOO','OOOO ','O 1O '],
'knight2' : ['  OO ','  OOO','OOOO ','O 2O '],
'bishop1' : ['  O  ',' O O ','  O  ',' O1O '],
'bishop2' : ['  O  ',' O O ','  O  ',' O2O '],
'queen' : ['O O O',' OOO ',' O O ',' O O '],
'king' : ['  O  ','OOOOO','  O  ',' OOO '],
'newrook' : ['     ','O O O','OOOOO',' NEW '],
'newknight' : ['  OO ','  OOO','OOOO ','ONEW '],
'newbishop' : ['  O  ',' O O ','  O  ',' NEW '],
'newqueen' : ['O O O',' OOO ',' O O ',' NEW ']
}

blackpieces = {
'pawn1' : ['     ','  X  ',' XXX ','  1  '],
'pawn2' : ['     ','  X  ',' XXX ','  2  '],
'pawn3' : ['     ','  X  ',' XXX ','  3  '],
'pawn4' : ['     ','  X  ',' XXX ','  4  '],
'pawn5' : ['     ','  X  ',' XXX ','  5  '],
'pawn6' : ['     ','  X  ',' XXX ','  6  '],
'pawn7' : ['     ','  X  ',' XXX ','  7  '],
'pawn8' : ['     ','  X  ',' XXX ','  8  '],
'rook1' : ['     ','X X X','XXXXX',' X1X '],
'rook2' : ['     ','X X X','XXXXX',' X2X '],
'knight1' : ['  XX ','  XXX','XXXX ','X 1X '],
'knight2' : ['  XX ','  XXX','XXXX ','X 2X '],
'bishop1' : ['  X  ',' X X ','  X  ',' X1X '],
'bishop2' : ['  X  ',' X X ','  X  ',' X2X '],
'queen' : ['X X X',' XXX ',' X X ',' X X '],
'king' : ['  X  ','XXXXX','  X  ',' XXX '],
'newrook' : ['     ','X X X','XXXXX',' NEW '],
'newknight' : ['  XX ','  XXX','XXXX ','XNEW '],
'newbishop' : ['  X  ',' X X ','  X  ',' NEW '],
'newqueen' : ['X X X',' XXX ',' X X ',' NEW ']
}

spaces = {
'whitespace' : '     ',
'blackspace' : '.....'
}

########## STARTING POSITIONS

# piece[row,col]


positions = {

'blackpawn1' : [1,0],
'blackpawn2' : [1,1],
'blackpawn3' : [1,2],
'blackpawn4' : [1,3],
'blackpawn5' : [1,4],
'blackpawn6' : [1,5],
'blackpawn7' : [1,6],
'blackpawn8' : [1,7],

'whitepawn1' : [6,0],
'whitepawn2' : [6,1],
'whitepawn3' : [6,2],
'whitepawn4' : [6,3],
'whitepawn5' : [6,4],
'whitepawn6' : [6,5],
'whitepawn7' : [6,6],
'whitepawn8' : [6,7],

'blackrook1' : [0,0],
'blackrook2' : [0,7],

'whiterook1' : [7,0],
'whiterook2' : [7,7],

'blackknight1' : [0,1],
'blackknight2' : [0,6],

'whiteknight1' : [7,1],
'whiteknight2' : [7,6],

'blackbishop1' : [0,2],
'blackbishop2' : [0,5],

'whitebishop1' : [7,2],
'whitebishop2' : [7,5],

'blackqueen' : [0,3],
'whitequeen' : [7,3],

'blackking' : [0,4],
'whiteking' : [7,4],

'blacknewrook' : [500,500],
'blacknewknight' : [500,500],
'blacknewbishop' : [500,500],
'blacknewqueen' : [500,500],

'whitenewrook' : [500,500],
'whitenewknight' : [500,500],
'whitenewbishop' : [500,500],
'whitenewqueen' : [500,500]

}

castle = {
'wkingmove' : False,
'bkingmove' : False,
'wrook1check' : False,
'wrook2check' : False,
'brook1check' : False,
'brook2check' : False,
'bcastle' : False,
'wcastle' : False
}

coldict = {
'a' : 0,
'b' : 1,
'c' : 2,
'd' : 3,
'e' : 4,
'f' : 5,
'g' : 6,
'h' : 7
}


startingpositions = positions.copy()

def MoveCheck(positions,a,b,oldrow,oldcol,piece,castle,enpassant):
    
    x = True

    #### Rook Movement Limitations ####

    if 'rook' in piece:
    
        
        if a == oldrow and b != oldcol:
        
            colrange = RangeFinder(b,oldcol)
            
            for item in positions:
            
                if positions[item][1] in colrange and positions[item][0] == oldrow:
                    x = False
            
        
        elif a != oldrow and b == oldcol:
        
            rowrange = RangeFinder(a,oldrow)
            
            for item in positions:
            
                if positions[item][0] in rowrange and positions[item][1] == oldcol:
                    x = False
                    
            
        if ((a == oldrow and b != oldcol) or (a != oldrow and b == oldcol)) and x != 100:
            pass
        else:
            x = False                                       

                                

                                
    #### Knight Movement Limitations
    
    elif 'knight' in piece:
        
        if abs(a-oldrow) == 2 and abs(b-oldcol) == 1:
            pass
                
        elif abs(b-oldcol) == 2 and abs(a-oldrow) == 1:
            pass
                
        else:
            x = False                           
    
    
    
    ##### Bishop Movement Limitations #####
    
    elif 'bishop' in piece:
    
        colrange = RangeFinder(b,oldcol)
        rowrange = RangeFinder(a,oldrow)
        
        if abs(oldrow-a) == abs(oldcol-b):
            pass
        else:
            x = False
    
        for item in positions:
            
            if abs(oldrow - positions[item][0]) == abs(oldcol - positions[item][1]) and positions[item][0] in rowrange and positions[item][1] in colrange:
                x = False
    
                                
    ##### Queen Movement Limitations
    
    elif 'queen' in piece:
        q = 0

        colrange = RangeFinder(b,oldcol)
        rowrange = RangeFinder(a,oldrow)


        if a == oldrow and b != oldcol:
            q = 100
            for item in positions:
            
                if positions[item][1] in colrange and positions[item][0] == oldrow:
                    x = False
                
        elif a != oldrow and b == oldcol:
            q = 100
            for item in positions:
            
                if positions[item][0] in rowrange and positions[item][1] == oldcol:
                    x = False

        
        if abs(a-oldrow) == abs(b-oldcol):
            q = 100
            for item in positions:
                
                if abs(oldrow - positions[item][0]) == abs(oldcol - positions[item][1]) and positions[item][0] in rowrange and positions[item][1] in colrange:
                    x = False

        if q != 100:
            x = False
                            
    
    
    #### King Movement Limitations ####

    elif 'king' in piece:
        
        king = 0
        
        if abs(oldrow-a) == 1:
            if abs(oldcol-b) == 1 or oldcol-b == 0:
                king = 100
        
        elif abs(oldcol-b) == 1:
            if abs(oldrow-a) == 1 or oldrow-a == 0:
                king = 100
        
        if castle['bkingmove'] == False and 'black' in piece and castle['bcastle'] == False:
            if castle['brook1check'] == False and [a,b] == [0,2]:
                for item in positions:
                    if positions[item] == [0,3] or positions[item] == [0,2] or positions[item] == [0,1]:
                        king = 50
                if king != 50:
                    king = 100
            
            elif castle['brook2check'] == False and [a,b] == [0,6]:
                for item in positions:
                    if positions[item] == [0,6] or positions[item] == [0,5]:
                        king = 50
                if king != 50:
                    king = 100
        elif castle['wkingmove'] == False and 'white' in piece and castle['wcastle'] == False:
            if castle['wrook1check'] == False and [a,b] == [7,2]:
                for item in positions:
                    if positions[item] == [7,3] or positions[item] == [7,2] or positions[item] == [7,1]:
                        king = 50
                if king != 50:
                    king = 100          
            
            elif castle['wrook2check'] == False and [a,b] == [7,6]:
                for item in positions:
                    if positions[item] == [7,6] or positions[item] == [7,5]:
                        king = 50
                if king != 50:
                    king = 100
        
        if king != 100:
            x = False   
            
    #### Pawn Movement Limitations ####
    
    elif 'pawn' in piece:
    
        if 'white' in piece:
            
            if oldrow == 6 and [a,b] == [4,oldcol]:
                for item in positions:
                    if positions[item] == [5,oldcol]:
                        x = False
                    elif positions[item] == [a,b]:
                        x = False
            elif [a,b] == [oldrow-1,oldcol]:
                for item in positions:
                    if positions[item] == [a,b]:
                        x = False
            elif a == oldrow-1 and abs(oldcol-b) == 1:
                j = 0
                for item in positions:
                    if 'black' in item and positions[item] == [a,b]:
                        j = 100
                    elif item == actingpiece and positions[item] == [a+1,b] and enpassant == True:
                        j = 100
                if j != 100:
                    x = False
            else:
                x = False
        else:
        
            if oldrow == 1 and [a,b] == [3,oldcol]:
                for item in positions:
                    if positions[item] == [2,oldcol]:
                        x = False
                    elif positions[item] == [a,b]:
                        x = False
            elif [a,b] == [oldrow+1,oldcol]:
                for item in positions:
                    if positions[item] == [a,b]:
                        x = False
            elif a == oldrow+1 and abs(oldcol-b) == 1:
                j = 0
                for item in positions:
                    if 'white' in item and positions[item] == [a,b]:
                        j = 100
                    elif item == actingpiece and positions[item] == [a-1,b] and enpassant == True:
                        j = 100

                if j != 100:
                    x = False   
            else:
                x = False
        
    if 'black' in piece:
        for item in positions:
            if item != piece and 'black' in item and positions[item] == [a,b]:
                x = False
    if 'white' in piece:
        for item in positions:
            if item != piece and 'white' in item and positions[item] == [a,b]:
                x = False
    return x

def WhiteCheck(positions):  
    whitecheck = False
    [a,b] = positions['whiteking']
    for item in positions:
        if 'black' in item:
            [oldrow,oldcol] = positions[item]
            whitecheck = MoveCheck(positions,a,b,oldrow,oldcol,item,castle,enpassant)
        if whitecheck == True:
            break
    return whitecheck
    
def BlackCheck(positions):
    blackcheck = False
    [a,b] = positions['blackking']
    for item in positions:
        if 'white' in item:
            [oldrow,oldcol] = positions[item]
            blackcheck = MoveCheck(positions,a,b,oldrow,oldcol,item,castle,enpassant)
        if blackcheck == True:
            break
    return blackcheck

def BlackMate(positions):
    moves=[]
    BlackMate = True
    for item in positions:
        if 'black' in item:
            for row in xrange(8):
                for col in xrange(8):
                    [oldrow,oldcol] = positions[item]
                    [a,b] = [row,col]
                    movecheck = MoveCheck(positions,a,b,oldrow,oldcol,item,castle,enpassant)
                    if movecheck == True:
                        checkpositions = positions.copy()
                        checkpositions[item] = [a,b]
                        for thing in checkpositions:
                            if 'white' in thing and checkpositions[thing] == checkpositions[item]:
                                checkpositions[thing] = [100,100]
                        MateCheck = BlackCheck(checkpositions)
                        if not MateCheck and item[5:] not in moves:
                            moves.append(item[5:])
                            BlackMate=False
    if BlackMate == False:
        print '                 BLACK IS IN CHECK!'
        BlackMate = False
    return BlackMate,moves
                                        
def WhiteMate(positions):
    moves=[]
    WhiteMate = True
    for item in positions:
        if 'white' in item:
            for row in xrange(8):
                for col in xrange(8):
                    [oldrow,oldcol] = positions[item]
                    [a,b] = [row,col]
                    movecheck = MoveCheck(positions,a,b,oldrow,oldcol,item,castle,enpassant)
                    if movecheck == True:
                        checkpositions = positions.copy()
                        checkpositions[item] = [a,b]
                        for thing in checkpositions:
                            if 'black' in thing and checkpositions[thing] == [a,b]:
                                checkpositions[thing] = [100,100]
                        MateCheck = WhiteCheck(checkpositions)
                        if not MateCheck and item[5:] not in moves:
                            moves.append(item[5:])
                            WhiteMate=False
    if WhiteMate == False:
        print '                 WHITE IS IN CHECK!'
        WhiteMate = False
    return WhiteMate,moves

def PrintBoard(whitepieces,blackpieces,spaces,positions,turn):
    print '\n', "'O' = White        pieces: pawn#, rook#, knight#, bishop#, queen, king"
    print "'X' = Black         extra commands: castle, quit, restart, & undo"
    print '       _________________________________________________________________'
    for row in xrange(8):
        if row != 0:
            print '       |_______|_______|_______|_______|_______|_______|_______|_______|'
        a = 8 - row
        for mrow in xrange(4):
            for col in xrange(8):
                t = 0
                if col == 0:
                    if mrow == 2:
                        print '     %s |' % a,
                    else:
                        print '       |',
                for item in whitepieces:
                    if positions['white' + item] == [row,col]:
                        t = 1
                        if (row % 2 == 0 and col % 2 == 1) or (row % 2 == 1 and col % 2 == 0):
                            print whitepieces[item][mrow].replace(' ','.'),
                        else:
                            print whitepieces[item][mrow],
                    elif positions['black' + item] == [row,col]:
                        t = 1
                        if (row % 2 == 0 and col % 2 == 1) or (row % 2 == 1 and col % 2 == 0):
                            print blackpieces[item][mrow].replace(' ','.'),
                        else:
                            print blackpieces[item][mrow],
                if t == 0:
                    if (row % 2 == 0 and col % 2 == 0) or (row % 2 == 1 and col % 2 == 1):
                        print spaces['whitespace'],
                    else:
                        print spaces['blackspace'],
                print '|',
            print
    print '       |_______|_______|_______|_______|_______|_______|_______|_______|'
    print '           a       b       c       d       e       f       g       h', '\n'

def SwitchTurn(turn):
## Switching Turns
    if turn == 'White':
        turn = 'Black'
    elif turn == 'Black':
        turn = 'White'
    print "%s's Turn to Move" % str(turn)
    print
    return turn

def RangeFinder(new,old):
    rangefound = [0]
    if new < old:
        rangefound = range(new+1,old)
    if new > old:
        rangefound = range(old+1,new)
    return rangefound

def Winner(blackmate,whitemate):
    if whitemate == True:
        print 'CHECKMATE! CONGRATULATIONS! BLACK HAS WON THE GAME!'
        
    elif blackmate == True:
        print 'CHECKMATE! CONGRATULATIONS! WHITE HAS WON THE GAME!' 

turn = 'White'
oldpositions = positions.copy()
checkpositions = positions.copy()
boardrowrange = '12345678'
boardcolrange = 'abcdefgh'
actingpiece = ''
checkcheck = enpassant = nextmove = oldenpassant = oldnextmove = False
oldcastle = castle.copy()
startingcastle = castle.copy()


count = 0
blackmate = whitemate = False
while blackmate == False and whitemate == False:
    if count == 2:
        raw_input('         Please Press Enter')

    print
    PrintBoard(whitepieces, blackpieces, spaces, positions, turn)
    blackcheck = BlackCheck(positions)
    whitecheck = WhiteCheck(positions)
    if blackcheck == True:
        blackmate,moves = BlackMate(positions)
        print 'Pieces you can move: ',
        for m in moves:
            print m+' ',
        print
    if whitecheck == True:
        whitemate,moves = WhiteMate(positions)
        print 'Pieces you can move: ',
        for m in moves:
            print m+' ',
        print
    if count == 100:
        print
        print 'Game Ended'
        break
    print "%s's Turn to Move" % str(turn)   
    print
    count = 0
    
    while count < 2 and blackmate != True and whitemate != True:
    
        x = 0
        piece = raw_input('Choose Piece to Move:  ').lower().replace(' ','')
            
        
        if piece == 'undo':
            count = 0
            enpassant = oldenpassant
            nextmove = oldnextmove
            castle = oldcastle.copy()
            if positions == oldpositions:
                x = 100
            positions = oldpositions.copy()
            PrintBoard(whitepieces, blackpieces, spaces, positions, turn)
            blackcheck = BlackCheck(positions)
            whitecheck = WhiteCheck(positions)
            
            if blackcheck == True:
                blackmate,moves = BlackMate(positions)
                print 'Pieces you can move: ',
                for m in moves:
                    print m+' ',
                print
            if whitecheck == True:
                whitemate,moves = WhiteMate(positions)
                print 'Pieces you can move: ',
                for m in moves:
                    print m+' ',
                print
            if whitemate != True and blackmate != True and x != 100:
                turn = SwitchTurn(turn)
            else:
                print "%s's Turn to Move" % str(turn)   
                print               
            
        elif piece == 'restart':
            yn = raw_input('Are you sure you want to restart? (y or n): ').lower().replace(' ','')
            
            if yn == 'y' or yn == 'yes':
                oldpositions = positions.copy()
                oldcastle = castle.copy()
                oldenpassant = enpassant
                oldnextmove = nextmove
                positions = startingpositions.copy()
                castle = startingcastle.copy()
                turn = 'White'
                PrintBoard(whitepieces, blackpieces, spaces, positions, turn)
                print "%s's Turn to Move" % str(turn)   
                print
            else:
                x = 100
                count += 1
        
        elif piece == 'quit':
            yn = raw_input('Are you sure you want to quit the game? (y or n): ').lower().replace(' ','')
            
            if yn == 'y' or yn == 'yes':
                count = x = 100
            else:
                count += 1
                x = 100
        
            
        elif piece == 'castle':
        
            direction = raw_input('Which way would you like to castle? (Left or Right): ').lower()
            if turn == 'White':
                if castle['wcastle'] == True:
                    print 'You have Already Castled'
                    count += 1
                    x = 100
                    
                elif castle['wkingmove'] == True:
                    print 'Already Moved the King'
                    count += 1
                    x = 100
                elif direction == 'right':
                    z = 0
                    for items in positions:
                        if positions[items] == [7,5] or positions[items] == [7,6]:
                            z += 1
                    if z != 0:
                        if z == 1:
                            print 'Piece in the Way'
                        else:
                            print '%s Pieces in the Way' % z
                            
                        count += 1
                        x = 100
                        
                    if x == 100:
                        pass                
                    elif castle['wrook2check'] == True:
                        print 'Already Moved Rook2'
                        count += 1
                        x = 100
                    else:
                        checkpositions = positions.copy()
                        checkpositions['whiteking'] = [7,6]
                        checkpositions['whiterook2'] = [7,5]
                        checkcheck = WhiteCheck(checkpositions)
                        if checkcheck == True:
                            print 'This Move Will Leave You in Check'
                            count += 1
                            x = 100
                        else:
                            oldcastle = castle.copy()
                            oldpositions = positions.copy()
                            positions = checkpositions.copy()
                            castle['wcastle'] = True
                        
                elif direction == 'left':
                    z = 0
                    for items in positions:
                        if positions[items] == [7,1] or positions[items] == [7,2] or positions[items] == [7,3]:
                            z += 1
                    if z != 0:
                        if z == 1:
                            print 'Piece in the Way'
                        else:
                            print '%s Pieces in the Way' % z
                            
                        count += 1
                        x = 100
                        
                        
                    if x == 100:
                        pass
                    elif castle['wrook1check'] == True:
                        print 'Already Moved Rook1'
                        count += 1
                        x = 100
                    else:
                        checkpositions = positions.copy()
                        checkpositions['whiteking'] = [7,2]
                        checkpositions['whiterook1'] = [7,3]
                        checkcheck = WhiteCheck(checkpositions)
                        if checkcheck == True:
                            print 'This Move Will Leave You in Check'
                            count += 1
                            x = 100
                        else:
                            oldcastle = castle.copy()
                            oldpositions = positions.copy()
                            positions = checkpositions.copy()
                            castle['wcastle'] = True
                else:
                    print 'Incorrect Input'
                    count += 1
                    x = 100
                        
            if turn == 'Black':
                if castle['bcastle'] == True:
                    print 'You Have Already Castled'
                    count += 1
                    x = 100
                elif castle['bkingmove'] == True:
                    print 'Already Moved the King'
                    count += 1
                    x = 100
                elif direction == 'right':
                    z = 0
                    for items in positions:
                        if positions[items] == [0,5] or positions[items] == [0,6]:
                            z += 1
                    if z != 0:
                        if z == 1:
                            print 'Piece in the Way'
                        else:
                            print '%s Pieces in the Way' % z
                            
                        count += 1
                        x = 100
                        
                        
                    if x == 100:
                        pass                
                    elif castle['brook2check'] == True:
                        print 'Already Moved Rook2'
                        count += 1
                        x = 100
                    else:
                        checkpositions = positions.copy()
                        checkpositions['blackking'] = [0,6]
                        checkpositions['blackrook2'] = [0,5]
                        checkcheck = BlackCheck(checkpositions)
                        if checkcheck == True:
                            print 'This Move Will Leave You in Check'
                            count += 1
                            x = 100
                        else:
                            oldcastle = castle.copy()
                            oldpositions = positions.copy()
                            positions = checkpositions.copy()
                            castle['bcastle'] = True
                        
                elif direction == 'left':
                    z = 0
                    for items in positions:
                        if positions[items] == [0,1] or positions[items] == [0,2] or positions[items] == [0,3]:
                            z += 1
                    if z != 0:
                        if z == 1:
                            print 'Piece in the Way'
                        else:
                            print '%s Pieces in the Way' % z
                            
                        count += 1
                        x = 100
                        
                        
                    if x == 100:
                        pass
                    elif castle['brook1check'] == True:
                        print 'Already Moved Rook1'
                        count += 1
                        x = 100
                    else:
                        checkpositions = positions.copy()
                        checkpositions['blackking'] = [0,2]
                        checkpositions['blackrook1'] = [0,3]
                        checkcheck = BlackCheck(checkpositions)
                        if checkcheck == True:
                            print 'This Move Will Leave You in Check'
                            count += 1
                            x = 100
                        else:
                            oldcastle = castle.copy()
                            oldpositions = positions.copy()
                            positions = checkpositions.copy()
                            castle['bcastle'] = True

            if x != 100:
                PrintBoard(whitepieces, blackpieces, spaces, positions, turn)
                blackcheck = BlackCheck(positions)
                whitecheck = WhiteCheck(positions)
                if blackcheck == True:
                    blackmate,moves = BlackMate(positions)
                    print 'Pieces you can move: ',
                    for m in moves:
                        print m+' ',
                    print
                if whitecheck == True:
                    whitemate,moves = WhiteMate(positions)
                    print 'Pieces you can move: ',
                    for m in moves:
                        print m+' ',
                    print
                turn = SwitchTurn(turn)
                x = 100
                
                
        elif 'white' + piece in positions or 'black' + piece in positions:
        
            if turn == 'White':
            
                if 'white' + piece in positions:
                    if positions['white' + piece] == [100,100]:
                        print 'Piece has already been taken'
                        count += 1
                        x = 100
                        
                    elif positions['white' + piece] == [200,200]:
                        print 'Already Promoted This Pawn'
                        count += 1
                        x = 100
                    
                    else:
                        spot = raw_input('New Position (e.g. f7):  ').lower().replace(' ','')
                        
                        if len(spot) == 2 and spot[0] in boardcolrange and spot[1] in boardrowrange:
                            a =  8 - int(spot[1]) 
                            for item in coldict:
                                if spot[0] == item:
                                    b = coldict[item]
                            oldrow = oldpositions['white' + piece][0]
                            oldcol = oldpositions['white' + piece][1]                           
                        else:
                            print 'Needs to be a Letter Followed by a Number'
                            count += 1
                            x = 100
                
            else:
                    
                if 'black' + piece in positions:
                
                    if positions['black' + piece] == [100,100]:
                        print 'Piece has already been taken'
                        count += 1
                        x = 100
                    
                    elif positions['black' + piece] == [200,200]:
                        print 'Already Promoted This Pawn'
                        count += 1
                        x = 100
                        
                    else:
                        spot = raw_input('New Position (e.g. f7):  ').lower().replace(' ','')
                        
                        if len(spot) == 2 and spot[0] in boardcolrange and spot[1] in boardrowrange:
                            a =  8 - int(spot[1]) 
                            for item in coldict:
                                if spot[0] == item:
                                    b = coldict[item]
                            oldrow = oldpositions['black' + piece][0]
                            oldcol = oldpositions['black' + piece][1]                           
                        else:
                            print 'Needs to be a Letter Followed by a Number'
                            count += 1
                            x = 100
            
            if x != 100:
                
                #### Rook Movement Limitations ####

                if 'rook' in piece:
                
                    j = 0

                    if a == oldrow and b != oldcol:
                    
                        colrange = RangeFinder(b,oldcol)
                        
                        for item in positions:
                        
                            if positions[item][1] in colrange and positions[item][0] == oldrow:
                                j += 1
                                x = 100
                        
                    
                    elif a != oldrow and b == oldcol:
                    
                        rowrange = RangeFinder(a,oldrow)
                        
                        for item in positions:
                        
                            if positions[item][0] in rowrange and positions[item][1] == oldcol:
                                j += 1
                                x = 100
                                
                    if j == 1:
                        print 'Piece in the Way'
                        count += 1
                    elif j != 0:
                        print '%s Pieces in the Way' % j
                        count += 1
                    if ((a == oldrow and b != oldcol) or (a != oldrow and b == oldcol)) and x != 100:
                        oldcastle = castle.copy()
                        if '1' in piece:
                            if turn == 'White':
                                castle['wrook1check'] = True
                            else:
                                castle['brook1check'] = True
                        if '2' in piece:
                            if turn == 'White':
                                castle['wrook2check'] = True
                            else:
                                castle['brook2check'] = True
                    elif x != 100:
                        print 'Not a Legal Move'
                        count += 1
                        x = 100                                     

                                            

                                            
                #### Knight Movement Limitations
                
                elif 'knight' in piece:
                    
                    if abs(a-oldrow) == 2 and abs(b-oldcol) == 1:
                        pass
                            
                    elif abs(b-oldcol) == 2 and abs(a-oldrow) == 1:
                        pass
                            
                    else:
                        print 'Not a Legal Move'
                        count += 1
                        x = 100                         
                
                
                
                ##### Bishop Movement Limitations #####
                
                elif 'bishop' in piece:
                
                    j = 0
                    colrange = RangeFinder(b,oldcol)
                    rowrange = RangeFinder(a,oldrow)
                    
                    if abs(oldrow-a) == abs(oldcol-b):
                        pass
                    else:
                        print 'Not a Legal Move'
                        count += 1
                        x = 100
                        
                    if x != 100:
                        for item in positions:
                            
                            if abs(oldrow - positions[item][0]) == abs(oldcol - positions[item][1]) and positions[item][0] in rowrange and positions[item][1] in colrange:
                                j += 1
                                x = 100
                    
                    if j == 1:
                        print 'Piece in the Way'
                        count += 1

                    elif j != 0:
                        print '%s Pieces in the Way' % j
                        count += 1

                
                
                                            
                ##### Queen Movement Limitations
                
                elif 'queen' in piece:
                    q = 0
                    j = 0
                    colrange = RangeFinder(b,oldcol)
                    rowrange = RangeFinder(a,oldrow)


                    if a == oldrow and b != oldcol:
                        q = 100
                        for item in positions:
                        
                            if positions[item][1] in colrange and positions[item][0] == oldrow:
                                j += 1
                                x = 100
                            
                    elif a != oldrow and b == oldcol:
                        q = 100
                        for item in positions:
                        
                            if positions[item][0] in rowrange and positions[item][1] == oldcol:
                                j += 1
                                x = 100
                                
                    if j == 1:
                        print 'Piece in the Way'
                        count += 1

                    elif j != 0:
                        print '%s Pieces in the Way' % j
                        count += 1
                    
                    if abs(a-oldrow) == abs(b-oldcol):
                        q = 100
                        for item in positions:
                            
                            if abs(oldrow - positions[item][0]) == abs(oldcol - positions[item][1]) and positions[item][0] in rowrange and positions[item][1] in colrange:
                                j += 1
                                x = 100
                        
                        if j == 1:
                            print 'Piece in the Way'
                            count += 1

                        elif j != 0:
                            print '%s Pieces in the Way' % j
                            count += 1  
                            
                    if q != 100:
                        print 'Not a Legal Move'
                        count += 1
                        x = 100
                                        
                
                
                #### King Movement Limitations ####

                elif 'king' in piece:
                    
                    king = 0
                    
                    if abs(oldrow-a) == 1:
                        if abs(oldcol-b) == 1 or oldcol-b == 0:
                            king = 100
                    
                    elif abs(oldcol-b) == 1:
                        if abs(oldrow-a) == 1 or oldrow-a == 0:
                            king = 100
                    
                    if king != 100:
                        print 'Not a Legal Move'
                        count += 1
                        x = 100 
                    else:
                        oldcastle = castle.copy()
                        if turn == 'White':
                            castle['wkingmove'] = True
                        else:
                            castle['bkingmove'] = True
                        
                #### Pawn Movement Limitations ####
                
                elif 'pawn' in piece:
                
                    if turn == 'White':
                        
                        if oldrow == 6 and [a,b] == [4,oldcol]:
                            for item in positions:
                                if positions[item] == [5,oldcol]:
                                    print 'Piece in the Way'
                                    count += 1
                                    x = 100
                                elif positions[item] == [a,b]:
                                    print 'Piece Already There'
                                    count += 1
                                    x = 100
                            if x != 100:
                                enpassant = True
                                
                                actingpiece = 'white' + piece
                        elif [a,b] == [oldrow-1,oldcol]:
                            for item in positions:
                                if positions[item] == [a,b]:
                                    print 'Piece Already There'
                                    count += 1
                                    x = 100
                        elif a == oldrow-1 and abs(oldcol-b) == 1:
                            j = 0
                            for item in positions:
                                if 'black' in item and positions[item] == [a,b]:
                                    j = 100
                                elif item == actingpiece and positions[item] == [a+1,b] and enpassant == True:
                                    j = 100
                                    
                            if j != 100:
                                print 'Not a Legal Move'
                                count += 1
                                x = 100
                        else:
                            print 'Not a Legal Move'
                            count += 1
                            x = 100
                    else:
                    
                        if oldrow == 1 and [a,b] == [3,oldcol]:
                            for item in positions:
                                if positions[item] == [2,oldcol]:
                                    print 'Piece in the Way'
                                    count += 1
                                    x = 100
                                elif positions[item] == [a,b]:
                                    print 'Piece Already There'
                                    count += 1
                                    x = 100
                                if x != 100:
                                    enpassant = True
                                    
                                    actingpiece = 'black' + piece
                        elif [a,b] == [oldrow+1,oldcol]:
                            for item in positions:
                                if positions[item] == [a,b]:
                                    print 'Piece Already There'
                                    count += 1
                                    x = 100
                        elif a == oldrow+1 and abs(oldcol-b) == 1:
                            j = 0
                            for item in positions:
                                if 'white' in item and positions[item] == [a,b]:
                                    j = 100
                                elif item == actingpiece and positions[item] == [a-1,b] and enpassant == True:
                                    j = 100
                            if j != 100:
                                print 'Not a Legal Move'
                                count += 1
                                x = 100     
                        else:
                            print 'Not a Legal Move'
                            count +=1
                            x = 100
                    
                    if x != 100:
                        if turn == 'White' and a == 0:
                                newpiece = raw_input('Turn Pawn into: ').lower()
                                if newpiece == 'rook':
                                    checkpositions = positions.copy()
                                    checkpositions['whitenewrook'] = [a,b]
                                    checkpositions['white' + piece] = [200,200]
                                    x = 50
                                elif newpiece == 'knight':
                                    checkpositions = positions.copy()
                                    checkpositions['whitenewknight'] = [a,b]
                                    checkpositions['white' + piece] = [200,200]
                                    x = 50
                                elif newpiece == 'bishop':
                                    checkpositions = positions.copy()
                                    checkpositions['whitenewbishop'] = [a,b]
                                    checkpositions['white' + piece] = [200,200]
                                    x = 50
                                elif newpiece == 'queen':
                                    checkpositions = positions.copy()
                                    checkpositions['whitenewqueen'] = [a,b]
                                    checkpositions['white' + piece] = [200,200]
                                    x = 50
                                else:
                                    print 'Piece should be a Rook, Knight, Bishop, or Queen'
                                    count += 1
                                    x = 100
                                    
                                if x != 100:
                                    print "New Piece is Named new" + '%s' % newpiece
                                    raw_input()
                                    
                        elif turn == 'Black' and a == 7:
                                newpiece = raw_input('Turn Pawn into: ').lower()
                                if newpiece == 'rook':
                                    checkpositions = positions.copy()
                                    checkpositions['blacknewrook'] = [a,b]
                                    checkpositions['black' + piece] = [200,200]
                                    x = 50
                                elif newpiece == 'knight':
                                    checkpositions = positions.copy()
                                    checkpositions['blacknewknight'] = [a,b]
                                    checkpositions['black' + piece] = [200,200]
                                    x = 50
                                elif newpiece == 'bishop':
                                    checkpositions = positions.copy()
                                    checkpositions['blacknewbishop'] = [a,b]
                                    checkpositions['black' + piece] = [200,200]
                                    x = 50
                                elif newpiece == 'queen':
                                    checkpositions = positions.copy()
                                    checkpositions['blacknewqueen'] = [a,b]
                                    checkpositions['black' + piece] = [200,200]
                                    x = 50
                                else:
                                    print 'Piece should be a Rook, Knight, Bishop, or Queen'
                                    count += 1
                                    x = 100                                 
                                        
                                if x != 100:
                                    print "New Piece is Named new" + '%s' % newpiece
                                    raw_input()
            
            
            if x != 100:
                if turn == 'Black':
                    for item in positions:
                        if 'white' in item:
                            if [a,b] == positions[item]:
                                if x != 50:
                                    checkpositions = positions.copy()
                                checkpositions[item] = [100,100]
                                x = 50
                            if 'pawn' in piece and 'pawn' in item and positions[item] == [a-1,b] and enpassant == True:
                                if x != 50:
                                    checkpositions = positions.copy()
                                checkpositions[item] = [100,100]
                                x = 50
                        
                        if 'black' in item and [a,b] == positions[item] and positions['black' + piece] != [200,200]:
                            print 'One of your pieces is already there'
                            count += 1
                            x = 100
                else:
                    for item in positions:
                        if 'black' in item:
                            if [a,b] == positions[item]:
                                checkpositions = positions.copy()
                                checkpositions[item] = [100,100]
                                x = 50
                            if 'pawn' in piece and 'pawn' in item and positions[item] == [a+1,b] and enpassant == True:
                                checkpositions = positions.copy()
                                checkpositions[item] = [100,100]
                                x = 50
                                
                        if 'white' in item and [a,b] == positions[item] and positions['black' + piece] != [200,200]:
                            print 'One of your pieces is already there'
                            count += 1
                            x = 100         


                            
            if x != 100:
                if turn == 'Black':
                    if checkpositions['black' + piece] != [200,200]:
                        if x != 50:
                            checkpositions = positions.copy()
                        checkpositions['black' + piece] = [a,b]
                else:
                    if checkpositions['white' + piece] != [200,200]:
                        if x != 50:
                            checkpositions = positions.copy()
                        checkpositions['white' + piece] = [a,b]
            



            if turn == 'White' and x != 100:
                checkcheck = WhiteCheck(checkpositions)
                if checkcheck == True:
                    print 'This Move Will Leave You in Check'
                    count += 1
                    x = 100
            elif turn == 'Black' and x != 100:
                checkcheck = BlackCheck(checkpositions)
                if checkcheck == True:
                    print 'This Move Will Leave You in Check'
                    count += 1
                    x = 100
            
            
            if checkcheck == False and x != 100:
                count = 0
                oldpositions = positions.copy()
                positions = checkpositions.copy()
                PrintBoard(whitepieces, blackpieces, spaces, positions, turn)
                oldenpassant = enpassant
                oldnextmove = nextmove
                if enpassant == True:
                    if (turn == 'White' and actingpiece != 'white' + piece) or (turn == 'Black' and actingpiece != 'black' + piece):
                        enpassant = False
                
                    
                blackcheck = BlackCheck(positions)
                whitecheck = WhiteCheck(positions)
                
                if blackcheck == True:
                    blackmate,moves = BlackMate(positions)
                    print 'Pieces you can move: ',
                    for m in moves:
                        print m+' ',
                    print
                if whitecheck == True:
                    whitemate,moves = WhiteMate(positions)
                    print 'Pieces you can move: ',
                    for m in moves:
                        print m+' ',
                    print
                if whitemate != True and blackmate != True:
                    turn = SwitchTurn(turn)


                
        else:
            print 'Not an Acceptable Input'
            count += 1  
    if whitemate==True or blackmate==True:
        print
        Winner(blackmate,whitemate)
        g=raw_input('\nPlay again? (y/n):  ')
        if 'y' in g.lower():
            blackmate=whitemate=False
            oldpositions = positions.copy()
            oldcastle = castle.copy()
            oldenpassant = enpassant
            oldnextmove = nextmove
            positions = startingpositions.copy()
            castle = startingcastle.copy()
            turn = 'White'
