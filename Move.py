from util import *


def didMoveOccur(oldSquare, newSquare, pieceType):
    if oldSquare == newSquare:
        return False

    if isMoveLegal(oldSquare,newSquare, pieceType):
        return True


def isMoveLegal(oldSquare,newSquare): #PSEUDOCODE
    piece = getPieceFromSquare(oldSquare)
    piececolor = piece.color

    piecetype = piece.getPieceType()

    if getTurnFromColor(piececolor):#needs rework
        return False

    #define moves explicitly? difficult part. if i can do queens, pawns, and knights, we're good. INCLUDE EN PASSANT



