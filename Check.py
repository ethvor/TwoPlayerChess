import Board
import Piece
import numpy as np
import util

def isKingChecked(KingPiece: Piece.Piece, board: Board.Board):
    if KingPiece.piecetype != "KING":
        print("\n\nError: checking check on non King Piece\n\n")
        return None

    pieceTypeList = Piece.Piece.PieceType.getTypeListNoNone()
    pieceTypeList.remove("BISHOP") #covered by Queen
    pieceTypeList.remove("ROOK") #covered by Queen
    #print(pieceTypeList)

    if KingPiece.color == "black":
        oppositeColorStr = "white"

    if KingPiece.color == "white":
        oppositeColorStr = "black"

    KingSquare = KingPiece.squareName
    print(KingSquare)

    checkableSquares = getAllCheckableSquares(KingSquare)

    listCheckPieceSquares = []

    for pieceType in pieceTypeList:
        for square in checkableSquares:
            if util.getPieceFromSquare(square,board) is not None: #only checks squares where theres something there:

                imaginaryPiece = Piece.Piece(square, pieceType, oppositeColorStr)  # make imaginary piece at king loc

                imaginaryCharacteristics = getMoveCharacteristics(square,KingSquare) #find char from imaginary piece to King

                imaginarySlope,imaginaryDistance,imaginaryRowDiff,imaginaryColDiff = imaginaryCharacteristics

                goodShape = isLegalShape(imaginarySlope,imaginaryDistance,imaginaryRowDiff,imaginaryColDiff,imaginaryPiece)

                if (imaginaryPiece.piecetype, imaginaryPiece.color) == (util.getPieceFromSquare(square,board).piecetype,util.getPieceFromSquare(square,board).color): #if imaginary piece type = real piece type At location


                    if pieceType == "PAWN": #manual pawn override (have not written canAttack() at this time.)
                        if imaginaryDistance == np.sqrt(2):
                            print("PAWN dist SQRT2")
                            if KingPiece.color == "white" and imaginaryPiece.color == "black":
                                print("WHITE KING BLACK PAWN")
                                if int(square[1]) - int(KingSquare[1]) == 1:
                                    if (square,imaginaryPiece.piecetype, imaginaryPiece.color) not in listCheckPieceSquares: #disallow duplicates
                                        listCheckPieceSquares.append((square, imaginaryPiece.piecetype, imaginaryPiece.color))

                            if KingPiece.color == "black" and imaginaryPiece.color == "white":
                                print("BLACK KING WHITE PAWN")
                                if int(square[1]) - int(KingSquare[1]) == -1:
                                    if (square,imaginaryPiece.piecetype, imaginaryPiece.color) not in listCheckPieceSquares: #disallow duplicates
                                        listCheckPieceSquares.append((square, imaginaryPiece.piecetype, imaginaryPiece.color))






                    if pieceType != "PAWN" and goodShape:
                        pathSquares = getPathSquares(square,KingSquare)
                        pathSquares.remove(KingSquare)
                        pathSquares.remove(square)

                        if len(pathSquares) == 0: #if theres nothing in between this imaginary piece and the king, it is checking the king
                            if (square,imaginaryPiece.piecetype, imaginaryPiece.color) not in listCheckPieceSquares: #disallow duplicates
                                    listCheckPieceSquares.append((square, imaginaryPiece.piecetype, imaginaryPiece.color))
                                    #print("pathsquares len for ", pieceType,"on", square,": ",len(pathSquares))
                                    #print(pathSquares)
                        #else:
                           # print(square, "failed len(pathSquares)")
                    else:
                        print(pieceType,"on",square, "failed goodshape")

    print(listCheckPieceSquares)













def getAllCheckableSquares(kingSquare):
    allSquares = util.getListOfBoardSquares()

    checkableSquares = []
    for square in allSquares:
        squareCharacteristics = getMoveCharacteristics(kingSquare, square)
        slope, distance, rowDiff, colDiff = squareCharacteristics
        if abs(slope) == 1 or slope == 0 or slope == np.inf or distance <= np.sqrt(8):
            checkableSquares.append(square)

    checkableSquares.remove(kingSquare)
    return checkableSquares

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

def getMoveCharacteristics(oldSquare, newSquare):
    allPositions = []
    col = ["a", "b", "c", "d", "e", "f", "g", "h"]
    row = ["1", "2", "3", "4", "5", "6", "7", "8"]
    for num in row:
        for char in col:
            squareName = char + num
            allPositions.append(squareName)

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

def getPathSquares(oldSquare,newSquare):
    moveCharacteristics = getMoveCharacteristics(oldSquare,newSquare)
    slope,distance,rowDiff,colDiff = moveCharacteristics

    xlist = ["a", "b", "c", "d", "e", "f", "g", "h"] #col
    ylist = ["1", "2", "3", "4", "5", "6", "7", "8"] #row

    pathSquares = []


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

def getIntersectPieces(pathSquares: list, board: Board):

    if len(pathSquares) == 0:
        return []

    piecesFound = []
    for square in pathSquares:
        piece = util.getPieceFromSquare(square,board)
        if piece is not None:
            piecesFound.append(piece)

    if len(piecesFound) != 0:
        piecesFound.remove(piecesFound[0]) #removes first value because i dont want it to always have 1 element (the piece you move)

    return piecesFound



