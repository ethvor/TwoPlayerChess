from Board import *


def getPieceFromSquare(squareName,boardObject: Board):
    currentPosDict = boardObject.currentPosDict
    piece = currentPosDict.get(squareName)
    return piece

def getTurnColor(moveNumber):
    remainder = moveNumber%2
    if remainder == 1:
        return "white"
    elif remainder == 0:
        return "black"
    else:
        return "error"

def getListOfBoardSquares():
    allPositions = []
    col = ["a", "b", "c", "d", "e", "f", "g", "h"]
    row = ["1", "2", "3", "4", "5", "6", "7", "8"]
    for num in row:
        for char in col:
            squareName = char + num
            allPositions.append(squareName)

    return allPositions