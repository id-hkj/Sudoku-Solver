from tkinter import *
from tkinter import ttk
from Functions import Solve, Mark
from time import time
import re
from os import path
asols = []
root = Tk()
root.title('Sudoku')
root.geometry('970x300-500+250')
root.resizable(FALSE,FALSE)

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
user = [[],[],[],[],[],[],[],[],[]]
howm = 5000
def topset():
    global howm
    if numm.get() == '' or int(numm.get()) == 0:
        howm = 5000
    else:
        howm = numm.get()
    custom.destroy()

def save():
    check = Toplevel()
    check.geometry('250x50+'+str(root.winfo_rootx()+300)+'+'+str(root.winfo_rooty()+50))
    framez = Frame(check)
    framez.grid(column=0,row=0)
    def No():
        check.destroy()
    def Yes():
        with open(path.join(path.dirname(path.abspath(__file__)), "board.txt"), 'w') as f:
            f.write(str(Solveinit(board)))
        root.destroy()
    ttk.Label(framez,text='Are you sure you want to close this program?').grid(row=1,column=0)
    new=Frame(framez)
    new.grid(column=0,row=2)
    ttk.Button(new, text="Yes",command=Yes).grid(row=2,column=0)
    ttk.Button(new, text="Cancel",command=No).grid(row=2,column=1)

def resetB():
    for i in range(9):
        for j in range(9):
            board[i][j].set('')
            Answer[i][j]['text'] = ''
            Answer[i][j].config(background='')

    val_1.set(' milliseconds')
    val_2.set('')
    val_3.set('')
    val_5.set('')

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
            Answer[int(square[0])][int(square[1])].config(background='red')

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
        val_5.set(str('ERROR ALERT!!!\nYou entered in the Sudoku \nincorrectly'))
        displayinit(newb,increase)
    elif str(nowsolved) == 'ERROR':
        message.config(foreground="red")
        val_1.set('')
        val_2.set('')
        val_3.set('')
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
            val_5.set('')
        else:
            message.config(foreground="red")
            val_1.set(str(millisecs) + ' milliseconds')
            val_2.set('')
            val_3.set('')
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
        val_5.set(str('All checks out!'))
        displayinit(newb)
    else:
        message.config(foreground="red")
        val_1.set(str(millisecs) + ' milliseconds')
        val_2.set('')
        val_3.set('')
        val_5.set(str('ERROR ALERT!!!\nYou have made a mistake!'))
        displayinit(newb,wrong)

def howmny():
    global asols
    asols = []
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
    message.config(foreground="green")
    per('strt')
    if num == howm:
        val_5.set('The current board has\n' + str(num) + ' or more solutions.')
    else:
        val_5.set('The current board has\n' + str(num) + ' solutions.')

def HowMany(Boards):
    Board=Boards
    Change_Squares = []
    for i in range(9):
        for j in range (9):
            if Board[i][j] == '0':
                Change_Squares.append(str(i) + str(j))
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
            global asols
            asols.append(str(Board))
            if int(p['value']) < 950:
                p['value'] = 5 + round(num/(round(int(howm)/1000) + 1))
                new.update()
        if num == howm:
            works = False
    p['value'] = 960
    return num,back,inc

def only_numbers(char):
    if (re.match('^[1-9]*$', char) is not None and len(char) <= 1):
        if not(len(char) == 0):
            tab(7)
        return True
    elif char=='0':
        tab(4)
    else:
        return False

def tick(char):
    return re.match('^[0-9]*$', char) is not None and len(char) < 7
def yess(char):
    for ch in char:
        if int(ch) == 0:
            return True
        else:
            break
    if char == '':
        return True
    else:
        if re.match('^[0-9]*$', char) is not None and int(char) <= int(len(asols)):
            per(char)
            return True
        else:
            return False
def soclose(gimme):
    res = asols[gimme].strip('][').split('], [')
    for i in range(9):
        res[i] = res[i].split(', ')
    for i in range(9):
        for j in range(9):
            try:
                neww = res[i][j].split("'")
                res[i][j] = neww[1]
            except:
                pass
    return res

def per(peram):
    try:
        now = int(HowDisp.get())
    except:
        now = '1'
    if len(asols) > 0:
        if peram == 'strt':
            HowDisp.set(str(1))
            displayinit(soclose(0))
        elif peram == 'end':
            HowDisp.set(str(len(asols)))
            displayinit(soclose(int(len(asols) - 1)))
        elif peram == 'nxt':
            if int(now) == len(asols):
                HowDisp.set(str(1))
                displayinit(soclose(0))
            else:
                HowDisp.set(str(now + 1))
                displayinit(soclose(int(now)))
        elif peram == 'prv':
            if int(now) == 1:
                HowDisp.set(str(len(asols)))
                displayinit(soclose(int(len(asols) - 1)))
            else:
                HowDisp.set(str(now - 1))
                displayinit(soclose(int(now - 2)))
        else:
            displayinit(soclose(int(int(peram) - 1)))
def help():
    global numm
    numm=StringVar()
    global custom
    custom = Toplevel(root)
    custom.geometry('500x200')
    custom.title('How Many Customisation')
    bigf= Frame(custom)
    bigf.grid(row=0,column=0,padx=5,pady=5)
    ttk.Label(bigf,text='This shows how many outcomes a given sudoku can have.\nHowever, if your sudoku has more than 5000 solutions, we will stop the calculation.\nThis is because a sudoku can have up to 6,670,903,752,021,072,936,960 solutions.\nIf we looked through all those, you may be waiting for the program to finish for a couple\nyears. Or decades.').grid(column=1,row=1)
    ttk.Label(bigf,text='If you would like to change the maximum solutions we will look at,\nenter a value between 1 and 999 999 below.').grid(column=1,row=2,sticky=(W))
    validations = (framegrid.register(tick),'%P')
    x = ttk.Entry(bigf,width=10,textvariable=numm, validate="key", validatecommand=validations)
    x.grid(row=5,column=1,pady=1,padx=2)
    numm.set(howm)
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
                user[k + (3*i)].append(x)

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

if path.exists(path.join(path.dirname(path.abspath(__file__)), "board.txt")):
    with open(path.join(path.dirname(path.abspath(__file__)), "board.txt"), 'r') as f:
        asols.append(f.read())
        nowsy = soclose(0)
        for i in range(9):
            for j in range(9):
                if nowsy[i][j] == '0':
                    pass
                else:
                    board[i][j].set(nowsy[i][j])

def coords(wid):
    wid = str(wid)
    if wid[7] == '.':
        try:
            for i in range(3):
                for j in range(3):
                    if int(wid[14]) == 3*i + j + 1:
                        return str(i) + str(j)
        except:
            return '00'
    elif wid[8] == '.':
        for i in range(3):
            for j in range(3):
                if int(wid[7]) == int(3*i + j + 1):
                    for k in range(3):
                        for l in range(3):
                            try:
                                if int(wid[15]) == 3*k + l + 1:
                                    return str(k + (3*i)) + str(l + (3*j))
                            except:
                                return str(3*i) + str(3*j)
    else:
        return ''
def up(event):
    widget = root.focus_get()
    cos = coords(widget)
    if cos[0] == '0':
        pass
    else:
        user[int(cos[0])-1][int(cos[1])].focus_set()
def dn(event):
    widget = root.focus_get()
    cos = coords(widget)
    if cos[0] == '8':
        pass
    else:
        user[int(cos[0])+1][int(cos[1])].focus_set()
def lf(event):
    widget = root.focus_get()
    cos = coords(widget)
    if cos[1] == '0':
        pass
    else:
        user[int(cos[0])][int(cos[1])-1].focus_set()
def rt(event):
    widget = root.focus_get()
    cos = coords(widget)
    if cos[1] == '8':
        pass
    else:
        user[int(cos[0])][int(cos[1])+1].focus_set()
def stab(event):
    widget = root.focus_get()
    cos = coords(widget)
    if cos[1] == '0' and cos[0] == '0':
        user[8][8].focus_set()
    elif cos[1] == '0':
        user[int(cos[0])-1][8].focus_set()
    else:
        user[int(cos[0])][int(cos[1])-1].focus_set()
def tab(event):
    widget = root.focus_get()
    cos = coords(widget)
    if cos[1] == '8' and cos[0] == '8':
        user[0][0].focus_set()
    elif cos[1] == '8':
        user[int(cos[0])+1][0].focus_set()
    else:
        user[int(cos[0])][int(cos[1])+1].focus_set()

root.bind("<Up>", up)
root.bind("<Down>", dn)
root.bind("<Left>", lf)
root.bind("<Right>", rt)
root.bind_all("<Tab>", tab)
root.bind_all("<Shift-Tab>", stab)

user[4][4].focus_set()

img = PhotoImage(file=(path.join(path.dirname(path.abspath(__file__)), "question.png")))
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
ttk.Label(framegrid, text='Action Time: ').grid(column=4,row=1, sticky=(W))
ttk.Label(framegrid, text='Backtrack Number: ').grid(column=4,row=2, sticky=(W))
ttk.Label(framegrid, text='Increase Number: ').grid(column=4,row=3, sticky=(W))
ttk.Label(framegrid, textvariable=val_1).grid(column=5,row=1, sticky=(E))
ttk.Label(framegrid, textvariable=val_2).grid(column=5,row=2, sticky=(E))
ttk.Label(framegrid, textvariable=val_3).grid(column=5,row=3, sticky=(E))

val_5 = StringVar()

framegrid = ttk.Frame(master=root,width=195,height=90)
framegrid.grid(row=1,column=4, padx=5, pady=5)
framegrid.grid_propagate(False)
ttk.Label(framegrid, text='Messages: ').grid(column=4,row=2, columnspan=2)
message = ttk.Label(framegrid, textvariable=val_5)
message.grid(column=4,row=3, columnspan=2)

ttk.Button(root, text='Clear', command=resetB).grid(column=1,row=6, sticky=(W,E))

img1 = PhotoImage(file=(path.join(path.dirname(path.abspath(__file__)), "FIRST1.png")))
img2 = PhotoImage(file=(path.join(path.dirname(path.abspath(__file__)), "PREV1.png")))
img3 = PhotoImage(file=(path.join(path.dirname(path.abspath(__file__)), "NEXT1.png")))
img4 = PhotoImage(file=(path.join(path.dirname(path.abspath(__file__)), "LAST1.png")))
framegrid = ttk.Frame(root)
framegrid.grid(column=5,row=6,columnspan=3)
Button(framegrid, image=img1,command=lambda: per('strt'), highlightthickness = 0, bd = 0).grid(column=4,row=6,padx=3)
Button(framegrid, image=img2,command=lambda: per('prv'), highlightthickness = 0, bd = 0).grid(column=5,row=6)
ttk.Label(framegrid, text="Solution Nº: ").grid(column=6,row=6,padx=3)
Button(framegrid, image=img3,command=lambda: per('nxt'), highlightthickness = 0, bd = 0).grid(column=8,row=6,padx=3)
Button(framegrid, image=img4,command=lambda: per('end'), highlightthickness = 0, bd = 0).grid(column=9,row=6)
validations = (framegrid.register(yess),'%P')
HowDisp=StringVar()
HowDisp.set('')
ttk.Entry(framegrid,width=15,textvariable=HowDisp, validate="key", validatecommand=validations).grid(row=6,column=7)

root.protocol("WM_DELETE_WINDOW", save)
root.mainloop()
