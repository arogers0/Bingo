from random import randint
from string import ascii_lowercase
import tkinter
# using 64 possible tile values across the 75 tiles (25 tiles in each 5x5 board)
tileValues = []
for i in range(1, 4):
    for char in ascii_lowercase:
            if not (i == 3 and char > 'l'):
                val = "%s%d" % (char, i)
                tileValues.append(val)

testTiles = []
for i in range(5):
    for j in range(5):
        testTiles.append("%s%s"%(i,j))

class Utility:

    @staticmethod
    def completeGame(boards):
        # TODO irrelevant checking for bingo here
        while not any(board.hasBingo() for board in boards):
            Utility.singleIteration(boards)
            # boards[0].getMaster().after(20, None)


    @staticmethod
    def singleIteration(boards):
        tileVal = Utility.genRandomTile()
        Utility.updateBoards(boards, tileVal)
        Utility.checkWinner(boards)

    @staticmethod
    def genRandomTile():
        num = randint(0, 63)
        return tileValues[num]


    @staticmethod
    def updateBoards(boards, tileVal):
        for board in boards:
            board.updateTiles(tileVal)


    @staticmethod
    def checkWinner(boards):
        winners = []
        for board in boards:
            if board.hasBingo():
                winners.append(board)

        if len(winners) > 0:
            for winner in winners:
                print("Board #%d is a winner!" % winner.getId())

