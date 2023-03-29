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