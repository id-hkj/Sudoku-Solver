#TODO:
#UI
#In UI functions of suduko app are as folllows
#1. Solve
#2. Check
#3. How many solutions?
import time

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
start_time = time.time()
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
                    for m in range(3):
                        for n in range(3):
                            if str(Board1[m + (3*k)][n + (3*l)]) == str(Val):
                                if (m + (3*k) == Row) and (n + (3*l) == Column):
                                    pass
                                else:
                                    return False
                    return True
increase = 0
backtrack = 0
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
            backtrack += 1
            break
        else:
            Board1[Row][Column] = int(Curr_Val + 1)
            works = Check(Row, Column, int(Curr_Val + 1))
        
        if works:
            break
        else:
            increase += 1
            continue
    i += 1
i = 0
while i < 9:
    for j in range(9):
        if Check(i, j, Board1[i][j]):
            continue
        else:
            i = 10
            print('ERROR!!!!!')
            break
    i += 1

end_time = time.time()
print()
for i in range (9):
    Row = Board1[i]
    Row = str(str(Row[0]) + str(Row[1]) + str(Row[2]) + str(Row[3]) + str(Row[4]) + str(Row[5]) + str(Row[6]) + str(Row[7]) + str(Row[8]))
    print(Row)
print('\nThis solve took ' + str(round(((end_time - start_time) * 1000), 0)) + ' milliseconds.')
print('This solve increased numbers ' + str(increase) + ' times')
print('This solve backtracked ' + str(backtrack) + ' times.')

x = input('\nPress Enter/Return to close')
