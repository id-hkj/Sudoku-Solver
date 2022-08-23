from distutils.cmd import Command
from tkinter import *
from tkinter import ttk
from turtle import width
from Functions import Solve, Mark
from time import time,sleep
import re

root = Tk()
root.title('Sudoku')
root.geometry('970x300-500+250')

board = [[StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()],
    [StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()],
    [StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()],
    [StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()],
    [StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()],
    [StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()],
    [StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()],
    [StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()],
    [StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]]

Answer = [[],[],[],[],[],[],[],[],[]]
howm = 5000
def topset():
    global howm
    howm = round(float(numm.get()))
    custom.destroy()

def resetB():
    print(howm)
    for i in range(9):
        for j in range(9):
            board[i][j].set('')
            Answer[i][j]['text'] = ''
            Answer[i][j].config(background='')

    val_1.set(' milliseconds')
    val_2.set('')
    val_3.set('')
    val_4.set('')
    val_5.set('')

def Mimic():
    for i in range(9):
        for j in range(9):
            if Answer[i][j]['text'] == '':
                board[i][j].set('')
            else:
                board[i][j].set(Answer[i][j]['text'])

def Solveinit(board):
    new = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]
    for i in range(9):
        for j in range(9):
            new[i][j] = str(board[i][j].get())
            if new[i][j] == '':
                new[i][j] = '0'
    return new

def displayinit(boarder,*args):
    for i in range(9):
        for j in range(9):
            if int(boarder[i][j]) == 0:
                Answer[i][j].configure(text='')
                Answer[i][j].config(background='')
            else:
                Answer[i][j].configure(text= int(boarder[i][j]))
                Answer[i][j].config(background='')
    if args:
        for square in args[0]:
            Location=square.split('.')
            Answer[int(Location[0])][int(Location[1])].config(background='red')

def Solver():
    start = float(time())
    boards = board
    newb = Solveinit(boards)
    nowsolved, increase, backtrack = Solve(newb)
    if str(nowsolved) == 'NotSolve':
        message.config(foreground="red")
        val_1.set('')
        val_2.set('')
        val_3.set('')
        val_4.set('')
        val_5.set(str('ERROR ALERT!!!\nYou entered in the Sudoku \nincorrectly'))
        displayinit(newb,increase)
    elif str(nowsolved) == 'ERROR':
        message.config(foreground="red")
        val_1.set('')
        val_2.set('')
        val_3.set('')
        val_4.set('')
        val_5.set(str('ERROR ALERT!!!\nThis Sudoku is unsolvable'))
    else:
        maybe,wrong = Mark(nowsolved)
        end = float(time())
        millisecs = round((end - start)*1000)        
        if maybe:
            displayinit(nowsolved)
            val_1.set(str(millisecs) + ' milliseconds')
            val_2.set(str(backtrack))
            val_3.set(str(increase))
            val_4.set('')
            val_5.set('')
        else:
            message.config(foreground="red")
            val_1.set(str(millisecs) + ' milliseconds')
            val_2.set('')
            val_3.set('')
            val_4.set('')
            val_5.set(str('ERROR ALERT!!!\nSomething went wrong when solving the sudoku.'))

def Working():
    start = float(time())
    boards = board
    newb = Solveinit(boards)
    maybe,wrong = Mark(newb)
    end = float(time())
    millisecs = round((end - start)*1000)
    
    if maybe:
        message.config(foreground="green")
        val_1.set(str(millisecs) + ' milliseconds')
        val_2.set('')
        val_3.set('')
        val_4.set('')
        val_5.set(str('All checks out!'))
        displayinit(newb)
    else:
        message.config(foreground="red")
        val_1.set(str(millisecs) + ' milliseconds')
        val_2.set('')
        val_3.set('')
        val_4.set('')
        val_5.set(str('ERROR ALERT!!!\nYou have made a mistake!'))
        displayinit(newb,wrong)

def howmny():
    global new
    new = Toplevel(root)
    new.geometry('250x50')
    global p
    p=ttk.Progressbar(new,orient=HORIZONTAL, length=200, mode='determinate', maximum=1000)
    p.grid(row=1,column=1,pady=15,padx=25)
    root.update()
    val_5.set('')
    start = float(time())
    boards = board
    p['value'] = 2
    new.update()
    newb = Solveinit(boards)
    p['value'] = 5
    new.update()
    num,back,inc = HowMany(newb)
    p['value'] = 980
    new.update()
    end = float(time())
    p['value'] = 1000
    new.destroy()
    millisecs = round((end - start))
    val_1.set(str(millisecs) + ' seconds')
    val_2.set(str(back))
    val_3.set(str(inc))
    if num == howm:
        val_4.set(str(num) + ' or More')
    else:
        val_4.set(str(num))

def HowMany(Boards):
    Board=Boards
    Change_Squares = []
    for i in range(9):
        for j in range (9):
            if Board[i][j] == '0':
                Change_Squares.append(str(i) + '.' + str(j))
    global howm
    works = True
    num=0
    back=0
    inc=0
    while works:
        if num == 0:
            Counter,a,b = Solve(Board,Change_Squares,0)
        else:
            Counter,a,b = Solve(Board,Change_Squares,int(len(Change_Squares)-1))
        if str(Counter) == 'NotSolve':
            works = False
        elif str(Counter) == 'ERROR':
            works = False
        else:
            num += 1
            Board = Counter
            inc += a
            back += b
            if int(p['value']) < 950:
                p['value'] = 5 + round(num/(round(howm/1000) + 1))
                new.update()
        if num == howm:
            works = False
    p['value'] = 960
    return num,back,inc

def only_numbers(char):
    return re.match('^[1-9]*$', char) is not None and len(char) <= 1 
def help():
    global numm
    numm=StringVar()
    now=StringVar()
    global custom
    custom = Toplevel(root)
    custom.geometry('500x200')
    custom.title('How Many Customisation')
    bigf= Frame(custom)
    bigf.grid(row=0,column=0,padx=5,pady=5)
    ttk.Label(bigf,text='This shows how many outcomes a given sudoku can have.\nHowever, if your sudoku has more than 5000 solutions, we will stop the calculation.\nThis is because a sudoku can have up to 6,670,903,752,021,072,936,960 solutions.\nIf we looked through all those, you may be waiting for the programm to finish for a couple\nyears. Or decades.').grid(column=1,row=1)
    ttk.Label(bigf,text='If you would like to change the maximum solutions we will look at,\nplease move the slider below.').grid(column=1,row=2,sticky=(W))
    def update(val):
        now.set("Scale at " + str(round(float(val))))
    s = ttk.Scale(bigf, orient='horizontal', length=400, from_=100, to=1000000, variable=numm, command=update)
    s.grid(row=3,column=1, pady=5)
    s.set(howm)
    ttk.Label(bigf,textvariable=now).grid(column=1,row=4)
    custom.protocol("WM_DELETE_WINDOW", topset)

for i in range (3):
    for j in range(3):
        framegrid = ttk.Frame(master=root, relief=SUNKEN, borderwidth=1.5,width=112,height=72)
        framegrid.grid(row=i+1,column=j+1,padx=5,pady=5)
        framegrid.grid_propagate(False)
        validation = (framegrid.register(only_numbers),'%P')
        for k in range(3):
            for l in range(3):
                x = ttk.Entry(framegrid,width=4,textvariable=board[k + (3*i)][l + (3*j)], validate="key", validatecommand=validation)
                x.grid(row=int(k+(3*i)+2),column=int(l+(3*j)+2),pady=1,padx=2)

for i in range (3):
    for j in range(3):
        framegrid = ttk.Frame(master=root, relief=SUNKEN, borderwidth=1.5,width=123,height=75)
        framegrid.grid(row=i+1,column=j+5,padx=5,pady=5)
        framegrid.grid_propagate(False)
        for k in range(3):
            for l in range(3):
                y = ttk.Label(framegrid,text="",width=6)
                y.grid(row=int(k+(3*i)),column=int(l+(3*j)),pady=3)
                Answer[k + (3*i)].append(y)

img = PhotoImage(file="question.png")
framegrid = ttk.Frame(master=root)
framegrid.grid(row=2,column=4, padx=20)
ttk.Button(framegrid, text='Sudoku Solver', command=Solver).grid(column=4,row=1)
ttk.Button(framegrid, text='Sudoku Checker', command=Working).grid(column=4,row=2)
ttk.Button(framegrid, text='How Many Solutions?', command=howmny).grid(column=4,row=3)
ttk.Button(framegrid, image=img,command=help).grid(column=5,row=3)

val_1 = StringVar()
val_2 = StringVar()
val_3 = StringVar()
val_1.set(' milliseconds')

framegrid = ttk.Frame(root,width=195,height=72)
framegrid.grid(row=3,column=4, padx=5, pady=5)
framegrid.grid_propagate(False)
ttk.Label(framegrid, text='Time: ').grid(column=4,row=1, sticky=(W))
ttk.Label(framegrid, text='Backtrack Number: ').grid(column=4,row=2, sticky=(W))
ttk.Label(framegrid, text='Increase Number: ').grid(column=4,row=3, sticky=(W))
ttk.Label(framegrid, textvariable=val_1).grid(column=5,row=1, sticky=(E))
ttk.Label(framegrid, textvariable=val_2).grid(column=5,row=2, sticky=(E))
ttk.Label(framegrid, textvariable=val_3).grid(column=5,row=3, sticky=(E))

val_4 = StringVar()
val_5 = StringVar()

framegrid = ttk.Frame(master=root,width=195,height=90)
framegrid.grid(row=1,column=4, padx=5, pady=5)
framegrid.grid_propagate(False)
ttk.Label(framegrid, text='Solution Number: ').grid(column=4,row=1, sticky=(W))
ttk.Label(framegrid, text='Messages: ').grid(column=4,row=2, columnspan=2)
ttk.Label(framegrid, textvariable=val_4).grid(column=5,row=1, sticky=(E))
message = ttk.Label(framegrid, textvariable=val_5)
message.grid(column=4,row=3, columnspan=2)

ttk.Button(root, text='Clear', command=resetB).grid(column=1,row=6, sticky=(W,E))
ttk.Button(root, text='Mimic Grid 2', command=Mimic).grid(column=2,row=6, sticky=(W,E))
root.mainloop()