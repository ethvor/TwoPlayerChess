from Game import Board


def getPieceFromSquare(squareName,boardObject: Board):
    currentPosDict = boardObject.currentPosDict
    pieceTouple = currentPosDict.get(squareName)
    pieceName = pieceTouple[0]
    piece = pieceTouple[1]
    return pieceTouple

def getTurnColor(moveNumber):
    remainder = moveNumber%2
    if remainder == 1:
        return "white"
    elif remainder == 0:
        return "black"
    else:
        return "error"