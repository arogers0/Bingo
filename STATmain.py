from tkinter import *
from STATboard import Board
from STATutil import Utility

def updateBoards():
    pass

counter = 0
tests = 200         # Number of games to be played
numBoards = 3       # Number of boards playing per game
boardsWinList = [0] * numBoards

numCalls = 0

while counter < tests:

    root = Tk()
    boardsList = []
    for i in range(0, numBoards):
        boardsList.append(Board(root, i))

    numCalls += Utility.completeGame(boardsList)

    counter += 1
    for i in range(numBoards):
        if i in Utility.checkWinner(boardsList):
            boardsWinList[i] += 1

headerString = "Boards: "
for i in range(numBoards):
    headerString += "B%d   " % i
print(headerString)

winPercentages = []
for i in range(numBoards):
    winPercentages.append(boardsWinList[i] / tests * 100)

winString = "Wins:   "
for i in range(numBoards):
    winString += "%d%%  " % winPercentages[i]
print(winString)

print("average num calls: " + str(numCalls / tests))
