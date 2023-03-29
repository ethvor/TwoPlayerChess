import Graphics
from util import *
import numpy as np



class Move:
    def __init__(self,oldSquare,newSquare,moveNumber):
        self.oldsquare=oldSquare
        self.newsquare=newSquare
        self.moveNumber=moveNumber


def didMoveOccur(move: Move):

    oldSquare = move.oldsquare
    newSquare = move.newsquare
    moveNumber = move.moveNumber

    if oldSquare == newSquare:
        return False

    if isMoveLegal(oldSquare, newSquare, moveNumber):
        return True


def isMoveLegal(move: Move):
    oldSquare = move.oldsquare
    newSquare = move.newsquare
    moveNumber = move.moveNumber

    piece = getPieceFromSquare(oldSquare)


    #1. is it your turn: if not return False

    #2. does the endpoint form a legal shape: if not return continue to 2.5

        #2.5. does the endpoint form a special shape: if so continue to 2.9


            #2.9. is piecetype Pawn or King
                #if not return false

                #if so continue to 2.99


                    #2.99 if King: (castling)

                        #is distance 2? if no return false
                        ##is slope 0? if no return false

                        #has this King moved before? if yes return false
                        #has the rook on this side moved before? if yes return false

                        #if no: continue to 2.999

"""MAKE SQUARE CLASS. Square.isAttacked(returns bool)"""

                            #2.999 get path Squares from King to endSquare
                                    #check all squares:
                                            #for each square:
                                                # is square occupied? if so return False (illegal)
                                                #is square attacked? if so return False (illegal)


    #3. is endpoint occupied
        #if yes:
            #is occupant same color
                #if so return False

                #if not continue to #4

        #if no continue to #4

    #4. for:

def getMoveCharacteristics(move: Move):
    print("getMoveCharacteristics called")
    allPositions = []
    col = ["a", "b", "c", "d", "e", "f", "g", "h"]
    row = ["1", "2", "3", "4", "5", "6", "7", "8"]
    for num in row:
        for char in col:
            squareName = char + num
            allPositions.append(squareName)

    oldSquare = move.oldsquare
    newSquare = move.newsquare

    oldCol = oldSquare[0] #letter
    oldRow = oldSquare[1] #number

    newCol = newSquare[0] #letter
    newRow = newSquare[1] #number


    colDiff = col.index(newCol) - col.index(oldCol)
    rowDiff = row.index(newRow) - row.index(oldRow)

    if colDiff != 0: #division by zero check
        slope = rowDiff/colDiff
    else:
        slope = np.inf

    distance = np.sqrt((colDiff)**2+(rowDiff)**2)

    moveInfo = (slope,distance,rowDiff,colDiff)
    return moveInfo


def isPathLegalShape(slope,distance,rowDiff,colDiff,piece):

    print("INSIDE ISPATHLEGALSHAPE")

    pieceType = piece.piecetype
    print("pieceType:",pieceType)


    slope = abs(slope)
    print("abs Slope:",slope)

    if pieceType == "KNIGHT":
        if ((slope==2 or slope==0.5)and(distance==2.23606797749979)):
            print("Legal Shape")
            return True

    if pieceType == "BISHOP":
        if ((slope == 1.0 or slope == -1.0)):
            print("Legal Shape")
            return True

    if pieceType == "ROOK":
        if ((slope == 0 or slope == np.inf)):
            print("Legal Shape")
            return True

    if pieceType == "QUEEN":
        if ((slope == 1.0 or slope == -1.0) or (slope == 0 or slope == np.inf)):
            print("Legal Shape")
            return True

    if pieceType == "KING":
        if ((distance == 1.0 and (slope==0 or slope==np.inf))or(distance==np.sqrt(2) and slope==1)):
            print("Legal Shape")
            return True

    if pieceType == "PAWN":
        if ((slope == np.inf) and (distance == 1)):
            if piece.color == "white":
                if rowDiff == 1:
                    print("Legal Shape")
                    return True
            elif piece.color == "black":
                if rowDiff == -1:
                    print("Legal Shape")
                    return True

    print("Illegal")
    return False

    doesPathHitPieces

    def getPathSquares(move):
        return True

    def executeTakeMove(move):
        1
        piece = getPieceFromSquare()

    def executeNormalMove(move):
        1

    def executeCastle(move,color):
        1

    def executeEnPassant(move,color):
        1
