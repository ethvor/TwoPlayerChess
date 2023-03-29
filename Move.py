from util import *
import numpy as np
import Player
import Check



class Move:
    def __init__(self, oldSquare, newSquare, player: Player.Player):
        self.oldsquare = oldSquare
        self.newsquare = newSquare
        self.player = player


def isMoveLegal(move: Move, currentPosDict: dict):

    movePlayer = move.player
    moveNumber = movePlayer.gameMoveNumber
    movePlayerColor = movePlayer.color

    oldSquare = move.oldsquare
    newSquare = move.newsquare

    moveCharacteristics = getMoveCharacteristics(move)
    slope,distance,rowDiff,colDiff = moveCharacteristics

    movePiece = currentPosDict.get(oldSquare)
    if isinstance(movePiece, Piece.Piece):
        movePieceType = movePiece.piecetype
        print(movePieceType)
    else:
        print("failed isinstance")
        print("object that failed:")
        print(movePiece)
        return False

    legal = True #legal by default

    #0. did the piece move at all
    if oldSquare == newSquare:
        print("did not move")
        return False

    #1. is it your turn: if not return False
    if getTurnColor(moveNumber) != movePlayerColor:
        print("wrong color for turn")
        return False


    # 1.5: is piecetype Pawn or King

    if movePieceType == "PAWN" or movePieceType == "KING":
        # 1.9: does move shape form a special move?

        if isMoveSpecial(move): #func not made yet
            1 == 1
                #if not continue to #2

                #if so continue to 1.99




                    #1.99: if piecetype King: (castling)

                        #is distance 2? if no return false
                        ##is slope 0? if no return false

                        #has this King moved before? if yes return false
                        #has the rook on this side moved before? if yes return false

                        #if no: continue to 1.999



                            #1.999 get path Squares from King to endSquare
                                    #check all squares:
                                            #for each square:
                                                # is square occupied? if so return False (illegal)
                                                #is square attacked? if so return False (illegal)


    #2. does the endpoint form a legal shape: if not return continue to 2.5
    if not isLegalShape(slope,distance,rowDiff,colDiff,movePiece):
        print("illegal move shape")
        return False

    # 3. are there multiple pieces in the path (auto fail)
    pathSquares = getPathSquares(move)
    intersectPieces = getIntersectPieces(pathSquares,currentPosDict)
    if len(intersectPieces) >= 2:
        print("multiple intersected pieces")
        return False

    # 4. Does the intersect path contain any of the same color pieces
    for square in pathSquares:
        piece = currentPosDict.get(square)
        if piece is not None:
            if piece.color == movePiece.color:
                if piece != movePiece:
                    print("path contained same color piece")
                    return False



    #5. does move put king into check


    return legal


def isMoveSpecial(move: Move):
    return False

def getMoveCharacteristics(move: Move):
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


def isLegalShape(slope,distance,rowDiff,colDiff,piece):

    #print("INSIDE ISPATHLEGALSHAPE")

    pieceType = piece.piecetype
   # print("pieceType:",pieceType)


    slope = abs(slope)
    #print("abs Slope:",slope)

    if pieceType == "KNIGHT":
        if ((slope==2 or slope==0.5)and(distance==2.23606797749979)):
            #print("Legal Shape")
            return True

    if pieceType == "BISHOP":
        if ((slope == 1.0 or slope == -1.0)):
            #print("Legal Shape")
            return True

    if pieceType == "ROOK":
        if ((slope == 0 or slope == np.inf)):
            #print("Legal Shape")
            return True

    if pieceType == "QUEEN":
        if ((slope == 1.0 or slope == -1.0) or (slope == 0 or slope == np.inf)):
            #print("Legal Shape")
            return True

    if pieceType == "KING":
        if ((distance == 1.0 and (slope==0 or slope==np.inf))or(distance==np.sqrt(2) and slope==1)):
            #print("Legal Shape")
            return True

    if pieceType == "PAWN":
        if ((slope == np.inf) and (distance == 1)):
            if piece.color == "white":
                if rowDiff == 1:
                    #print("Legal Shape")
                    return True
            elif piece.color == "black":
                if rowDiff == -1:
                    #print("Legal Shape")
                    return True

    #print("Illegal move shape WITHIN isLegalShape function")
    return False



def getPathSquares(move):
    moveCharacteristics = getMoveCharacteristics(move)
    slope,distance,rowDiff,colDiff = moveCharacteristics

    xlist = ["a", "b", "c", "d", "e", "f", "g", "h"] #col
    ylist = ["1", "2", "3", "4", "5", "6", "7", "8"] #row

    pathSquares = []

    oldSquare = move.oldsquare
    newSquare = move.newsquare

    oldSquareX = oldSquare[0]
    oldSquareY = oldSquare[1]

    newSquareX = newSquare[0]
    newSquareY = newSquare[1]





    indexCurrentX = xlist.index(oldSquareX)
    indexCurrentY = ylist.index(oldSquareY)


    slopeXincrement = colDiff
    slopeYincrement = rowDiff

    #print(f"slopeXinc = {slopeXincrement}")
    #print(f"slopeYinc = {slopeYincrement}")
    pathSquares.append(oldSquare)
    squareToAppend = oldSquare
    #print(slope)
    while squareToAppend != newSquare:

        if slope ==np.inf or slope == -np.inf:
            incrementorY = (slopeYincrement/abs(slopeYincrement))
            indexCurrentY += incrementorY

        elif slope == 0.0 or slope == 0 or slope == -0.0 or slope == -0:

            incrementorX = (slopeXincrement/abs(slopeXincrement))
            indexCurrentX += incrementorX #this is either 1 or -1. preserves direction so that this can iterate down or left too.

        elif slope == 1 or slope == 1.0 or slope == -1 or slope == -1.0:

            incrementorX = (slopeXincrement/abs(slopeXincrement))
            incrementorY = (slopeYincrement/abs(slopeYincrement))

            indexCurrentX += incrementorX
            indexCurrentY += incrementorY

        else:
            return [oldSquare,newSquare]

        indexCurrentX = int(indexCurrentX)
        indexCurrentY = int(indexCurrentY)

        squareToAppend = str(xlist[indexCurrentX] + ylist[indexCurrentY])
        #print(squareToAppend)

        pathSquares.append(squareToAppend)

    return pathSquares

def getIntersectPieces(pathSquares: list, currentPosDict: dict):

    piecesFound = []
    for square in pathSquares:
        piece = currentPosDict.get(square)
        if piece is not None:
            piecesFound.append(piece)

    piecesFound.remove(piecesFound[0]) #removes first value because i dont want it to always have 1 element (the piece you move)

    return piecesFound




def executeTakeMove(move):
    1
    piece = getPieceFromSquare()

def executeNormalMove(move):
    1

def executeCastle(move, color):
    1

def executeEnPassant(move, color):
    1
