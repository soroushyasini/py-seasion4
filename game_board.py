from re import I
import sys
global draw
draw = 0
def quit():
    sys.exit("end of game")
game_board = [["-", "-", "-"], ["-", "-", "-"],["-", "-", "-"]]
def show():
    for row in game_board:
        for cell in row:
            print(cell, end="")
        print()
show()

def win():
    if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X" :
        print("PLAYER 1 is winner !")
        quit()
    if game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O" :
        print("PLAYER 2 is winner !")
        quit()
    if game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X" :
        print("PLAYER 1 is winner !")
        quit()
    if game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O" :
        print("PLAYER 2 is winner !")
        quit()
    if game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X" :
        print("PLAYER 1 is winner !")
        quit()
    if game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O" :
        print("PLAYER 2 is winner !")
        quit()
    #rows are checked.
    if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X" :
        print("PLAYER 1 is winner !")
        quit()
    if game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O" :
        print("PLAYER 2 is winner !")
        quit()
    if game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X" :
        print("PLAYER 1 is winner !")
        quit()
    if game_board[0][1] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O" :
        print("PLAYER 2 is winner !")
        quit()
    if game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X" :
        print("PLAYER 1 is winner !")
        quit()
    if game_board[0][2] == "O" and game_board[1][2] == "O" and game_board[2][2] == "O" :
        print("PLAYER 2 is winner !")
        quit()
    #columns are checked.
    if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X" :
        print("PLAYER 1 is winner !")
        quit()
    if game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O" :
        print("PLAYER 2 is winner !")
        quit()
    if game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X" :
        print("PLAYER 1 is winner !")
        quit()
    if game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O" :
        print("PLAYER 2 is winner !")
        quit()
    if draw == 9:
        print("DRAW !!")
        quit()
while True:  
    print("player1")
    while True:
        row = int(input())
        col = int(input())
        if 0 <= row <=2 and 0<= col <=2:
            if game_board[row][col] == "-":
                game_board[row][col] = "X"
                draw += 1    
            show()
            break
        else:
            print("wrong location ! ")
    win()
    print("player2")
    while True:    
        row = int(input())
        col = int(input())
        if 0 <= row <=2 and 0<= col <=2:
            if game_board[row][col] == "-":
                game_board[row][col] = "O"
                draw += 1
            show()
            break
        else:
            print("wrong location ! ")

