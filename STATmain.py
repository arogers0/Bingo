from tkinter import *
from STATboard import Board
from STATutil import Utility

def updateBoards():
    pass

counter = 0
tests = 10
b1wins = 0
b2wins = 0
b3wins = 0

while counter < tests:

    root = Tk()
    board3 = Board(root, 3)
    board2 = Board(root, 2)
    board1 = Board(root, 1)
    boardsList = [board1, board2, board3]

    def testClick1():
        Utility.completeGame(boardsList)

    testClick1()
    counter += 1
    if Utility.checkWinner(boardsList) == 1:
        b1wins += 1
    elif Utility.checkWinner(boardsList) == 2:
        b2wins +=1
    elif Utility.checkWinner(boardsList) == 3:
        b3wins += 1

print(tests,'Tests  ','B1', ' B2', ' B3')
print('Wins:','    ', b1wins,' ', b2wins,' ', b3wins)
p1 = str(round(100*b1wins/tests))
p2 = str(round(100*b2wins/tests))
p3 = str(round(100*b3wins/tests))
print('Win Rate:', p1+'%', p2+'%', p3+'%')