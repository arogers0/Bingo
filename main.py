from tkinter import *
from board import Board
from util import Utility

def updateBoards():
    pass

root = Tk()
root.geometry("1000x1000")
root.title("BINGO Game")

bingoTitle = Label(root, text="BINGO", borderwidth=1)
bingoTitle.config(font=("Helvetica", 32))
bingoTitle.pack()

board3 = Board(root, 3)
board2 = Board(root, 2)
board1 = Board(root, 1)

boardFrame = Frame(root)

boardsList = [board1, board2, board3]

board1.render()
board2.render()
board3.render()
board1.boardFrame.pack(side=LEFT, expand=YES)
board2.boardFrame.pack(side=LEFT, expand=YES)
board3.boardFrame.pack(side=LEFT, expand=YES)

gameButtonFrame = Frame(root)
singleIterButton = Button(gameButtonFrame, text="Call A Value", command=lambda: Utility.singleIteration(boardsList)).pack(side=LEFT)
finishGameButton = Button(gameButtonFrame, text="Call Until End", command=lambda: Utility.completeGame(boardsList)).pack(side=LEFT)
gameButtonFrame.place(relx=0.5, rely=0.9, anchor=S)

root.mainloop()

