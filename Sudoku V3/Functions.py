def Check(Row, Column, Val, Board):
    #ROW
    for k in range(9):
        if str(Board[Row][k]) == str(Val):
            if k == Column:
                pass
            else:
                return False
    
    #COLUMN
    for k in range(9):
        if str(Board[k][Column]) == str(Val):
            if k == Row:
                pass
            else:
                return False
    
    #Determine Square
    for k in range(3):
        if (Row == k*3) or (Row == k*3 + 1) or (Row == k*3 + 2):
            for l in range(3):
                if (Column == l*3) or (Column == l*3 + 1) or (Column == l*3 + 2):
                    #Check Square
                    for m in range(3):
                        for n in range(3):
                            if str(Board[m + (3*k)][n + (3*l)]) == str(Val):
                                if (m + (3*k) == Row) and (n + (3*l) == Column):
                                    pass
                                else:
                                    return False
                    return True

def Solve(Boards,*args):
    Board = Boards
    correct, where = Mark(Board)
    if not correct:
        return 'NotSolve', where, 'NotSolve'

    #Determining which squares need to be changed
    if args:
        Change_Squares = args[0]
        i = int(args[1])
    else:
        Change_Squares = []
        for i in range(9):
            for j in range (9):
                if Board[i][j] == '0':
                    Change_Squares.append(str(i) + '.' + str(j))
        i = 0

    increase = 0
    backtrack = 0
    while i < len(Change_Squares):
        for j in range(11):
            #Get location and value of square
            if i < 0:
                return 'ERROR','ERROR','ERROR'
            Location = Change_Squares[i].split('.')
            Row = int(Location[0])
            Column = int(Location[1])
            Curr_Val = int(Board[Row][Column])
            
            if int(Curr_Val) >= 9:
                Board[Row][Column] = '0'
                i -= 2
                backtrack += 1
                break
            else:
                Board[Row][Column] = int(Curr_Val + 1)
                works = Check(Row, Column, int(Curr_Val + 1), Board)
            
            if works:
                break
            else:
                increase += 1
                continue
        i += 1
    return Board,increase,backtrack

def Mark(Board):
    i = 0
    while i < 9:
        for j in range(9):
            if Board[i][j] == '0':
                pass
            else:
                if Check(i, j, Board[i][j], Board):
                    continue
                else:
                    return False,(str(i) + '.' + str(j))
        i += 1
    return True,'no'