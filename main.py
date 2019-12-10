from tkinter import *
from board import Board
from util import Utility

root = Tk()
root.geometry("1000x500")
root.title("BINGO Game")

bingoTitle = Label(root, text="BINGO", borderwidth=1)
bingoTitle.config(font=("Helvetica", 32))
bingoTitle.pack()

boardFrame = Frame(root)
board3 = Board(boardFrame, 3)
board2 = Board(boardFrame, 2)
board1 = Board(boardFrame, 1)

boardsList = [board1, board2, board3]

board1.boardFrame.pack(side=LEFT, expand=YES, padx=10)
board2.boardFrame.pack(side=LEFT, expand=YES, padx=10)
board3.boardFrame.pack(side=LEFT, expand=YES, padx=10)
boardFrame.pack()

gameButtonFrame = Frame(root)
singleIterButton = Button(gameButtonFrame, text="Call A Value", command=lambda: Utility.singleIteration(boardsList)).pack(side=LEFT)
finishGameButton = Button(gameButtonFrame, text="Call Until End", command=lambda: Utility.completeGame(boardsList)).pack(side=LEFT)
gameButtonFrame.pack()

root.mainloop()
