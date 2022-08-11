#Mapping out the board
Board1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

for i in range (9):
    Row = input('Please Enter Row ' + str(i + 1) + '. ')
    Board1[i] = Row.split(',')

#Determining which squares need to be changed
Change_Squares = []
for i in range(9):
    for j in range (9):
        if Board1[i][j] == '0':
            Change_Squares.append(str(i) + '.' + str(j))

#Checking Alg
def Check(Row, Column, Val):
    #ROW
    for k in range(9):
        if str(Board1[Row][k]) == str(Val):
            if k == Column:
                pass
            else:
                return False
    
    #COLUMN
    for k in range(9):
        if str(Board1[k][Column]) == str(Val):
            if k == Row:
                pass
            else:
                return False
    
    #Determine Square
    for k in range(3):
        if (Row == k*3) or (Row == k*3 + 1) or (Row == k*3 + 2):
            for l in range(3):
                if (Column == l*3) or (Column == l*3 + 1) or (Column == l*3 + 2):
                    Square_Num = 3*k + l + 1
    #Check Square
    if Square_Num == 1:
        for k in range(3):
            for l in range(3):
                if str(Board1[k][l]) == str(Val):
                    if (k == Row) and (l == Column):
                        pass
                    else:
                        return False
        return True
    elif Square_Num == 2:
        for k in range(3):
            for l in range(3):
                if str(Board1[k][l+3]) == str(Val):
                    if (k == Row) and (l + 3 == Column):
                        pass
                    else:
                        return False
        return True
    elif Square_Num == 3:
        for k in range(3):
            for l in range(3):
                if str(Board1[k][l+6]) == str(Val):
                    if (k == Row) and (l + 6 == Column):
                        pass
                    else:
                        return False
        return True
    elif Square_Num == 4:
        for k in range(3):
            for l in range(3):
                if str(Board1[k+3][l]) == str(Val):
                    if (k + 3 == Row) and (l == Column):
                        pass
                    else:
                        return False
        return True
    elif Square_Num == 5:
        for k in range(3):
            for l in range(3):
                if str(Board1[k+3][l+3]) == str(Val):
                    if (k + 3 == Row) and (l + 3 == Column):
                        pass
                    else:
                        return False
        return True
    elif Square_Num == 6:
        for k in range(3):
            for l in range(3):
                if str(Board1[k+3][l+6]) == str(Val):
                    if (k + 3 == Row) and (l + 6 == Column):
                        pass
                    else:
                        return False
        return True
    elif Square_Num == 7:
        for k in range(3):
            for l in range(3):
                if str(Board1[k+6][l]) == str(Val):
                    if (k + 6 == Row) and (l == Column):
                        pass
                    else:
                        return False
        return True
    elif Square_Num == 8:
        for k in range(3):
            for l in range(3):
                if str(Board1[k+6][l+3]) == str(Val):
                    if (k + 6 == Row) and (l + 3 == Column):
                        pass
                    else:
                        return False
        return True
    elif Square_Num == 9:
        for k in range(3):
            for l in range(3):
                if str(Board1[k+6][l+6]) == str(Val):
                    if (k + 6 == Row) and (l + 6 == Column):
                        pass
                    else:
                        return False
        return True

i = 0
while i < len(Change_Squares):
    for j in range(11):
        #Get location and value of square
        Location = Change_Squares[i].split('.')
        Row = int(Location[0])
        Column = int(Location[1])
        Curr_Val = int(Board1[Row][Column])
        
        if int(Curr_Val) >= 9:
            Board1[Row][Column] = '0'
            i -= 2
            break
        else:
            Board1[Row][Column] = int(Curr_Val + 1)
            works = Check(Row, Column, int(Curr_Val + 1))

        if works:
            break
        else:
            continue
    i += 1
for i in range (9):
    Row = Board1[i]
    Row = str(str(Row[0]) + str(Row[1]) + str(Row[2]) + str(Row[3]) + str(Row[4]) + str(Row[5]) + str(Row[6]) + str(Row[7]) + str(Row[8]))
    print(Row)