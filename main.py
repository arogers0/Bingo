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

#board3a = Board(boardFrame, 3, board3.tiles)
#board2a = Board(boardFrame, 2, board2.tiles)
#board1a = Board(boardFrame, 1, board1.tiles)

#board3a.boardFrame.pack(side=RIGHT)
#board2a.boardFrame.pack(side=RIGHT)
#board1a.boardFrame.pack(side=RIGHT)
#boardFrame.place(relx=0.5, rely=0.2, anchor=N)
#boardFrame.lift()
#print(board3a.tiles[0][0].value)

#boardsList = [board1, board2, board3]

#buttonFrame = Frame(root)
#boardButton1 = Button(buttonFrame, text="Board 1", command=board1.focus).pack(side=LEFT)
#boardButton2 = Button(buttonFrame, text="Board 2", command=board2.focus).pack(side=LEFT)
#boardButton3 = Button(buttonFrame, text="Board 3", command=board3.focus).pack(side=LEFT)
#buttonFrame.pack()

board1.render()
board2.render()
board3.render()
board1.boardFrame.pack(side=LEFT)
board2.boardFrame.pack(side=LEFT)
board3.boardFrame.pack(side=LEFT)

gameButtonFrame = Frame(root)
singleIterButton = Button(gameButtonFrame, text="Call A Value", command=lambda: Utility.singleIteration(boardsList)).pack(side=LEFT)
finishGameButton = Button(gameButtonFrame, text="Call Until End", command=lambda: Utility.completeGame(boardsList)).pack(side=LEFT)
gameButtonFrame.place(relx=0.5, rely=0.9, anchor=S)

root.mainloop()
