from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
from random import shuffle

sign = 0

# Создаёт пустую доску
global board
board = [[" " for x in range(10)] for y in range(10)]


# Чек на проигрышь, учитывая заданные правила
def loser(lit):
    for y in range(6):  # check \ diagonals
        for x in range(6):
            if all([board[y + i][x + i] == lit for i in range(5)]):
                return True
    for y in range(4, 10):  # check / diagonals
        for x in range(6):
            if all([board[y - i][x + i] == lit for i in range(5)]):
                return True
    for y in range(10):  # check horizontals
        for x in range(6):
            if all([board[y][x + i] == lit for i in range(5)]):
                return True
    for y in range(6):  # check verticals
        for x in range(10):
            if all([board[y + i][x] == lit for i in range(5)]):
                return True
    return False


# Конфигурация символов на кнопке при игре с другим игроком
def get_text(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    if loser("X"):
        gb.destroy()
        box = messagebox.showinfo("Loser", "Player X lose the match")
    elif loser("O"):
        gb.destroy()
        box = messagebox.showinfo("Loser", "Player O lose the match")
    elif isfull():
        gb.destroy()
        box = messagebox.showinfo("Tie Game", "Tie Game")


# Чек на возможность "заполнения" кнопки
def isfree(i, j):
    return board[i][j] == " "


# Чек на заполнение всех полей
def isfull():
    flag = True
    for i in board:
        if i.count(' ') > 0:
            flag = False
    return flag


# GUI для игры с другим игроком
def gameboard_pl(game_board, l1, l2):
    global button
    button = []
    for i in range(10):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(10):
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()


# Выбор хода бота
def pc():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    if not possiblemove:
        return
    else:
        shuffle(possiblemove)
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                return i


# Конфигурация символов на кнопке при игре с ботом
def get_text_pc(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if loser("X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Loser", "Player lose the match")
    elif loser("O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Loser", "Computer lose the match")
    elif isfull():
        gb.destroy()
        x = False
        box = messagebox.showinfo("Tie Game", "Tie Game")
    if (x):
        if sign % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2)


# GUI для игры с ботом
def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(10):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(10):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()


# Инициализация игры с ботом
def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Computer : O",
                width=10, state=DISABLED)

    l2.grid(row=2, column=1)
    gameboard_pc(game_board, l1, l2)


# Инициализация игры с другим игроком
def withplayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player 1 : X", width=10)

    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Player 2 : O",
                width=10, state=DISABLED)

    l2.grid(row=2, column=1)
    gameboard_pl(game_board, l1, l2)


# main function
def play():
    menu = Tk()
    menu.geometry("250x150")
    menu.title("Tic Tac Toe")
    wpc = partial(withpc, menu)
    wpl = partial(withplayer, menu)

    head = Button(menu, text="---Welcome to tic-tac-toe---",
                  activeforeground='gray60',
                  activebackground="black", bg="gray60",
                  fg="black", width=500, font='summer', bd=5)

    B1 = Button(menu, text="Single Player", command=wpc,
                activeforeground='gray60',
                activebackground="gray60", bg="gray60",
                fg="black", width=500, font='black', bd=5)

    B2 = Button(menu, text="Multi Player", command=wpl, activeforeground='gray60',
                activebackground="gray60", bg="gray60", fg="black",
                width=500, font='black', bd=5)

    B3 = Button(menu, text="Exit", command=menu.quit, activeforeground='gray60',
                activebackground="gray60", bg="gray60", fg="black",
                width=500, font='black', bd=5)
    head.pack(side='top')
    B1.pack(side='top')
    B2.pack(side='top')
    B3.pack(side='top')
    menu.mainloop()


if __name__ == '__main__':
    play()
