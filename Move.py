from util import getTurnColor
import Piece
import numpy as np
import Player
import Check



class Move:
    def __init__(self, oldSquare, newSquare, player: Player.Player):
        self.oldsquare = oldSquare
        self.newsquare = newSquare
        self.player = player

    def getMoveTouple(self):
        return (self.oldsquare,self.newsquare)

def isMoveLegal(move: Move, currentPosDict: dict):
    #print("checking legality")

    #print(move)
    movePlayer = move.player
    moveNumber = movePlayer.gameMoveNumber
    movePlayerColor = movePlayer.color

    #("legal: gamemovenumber",moveNumber)

    oldSquare = move.oldsquare
    newSquare = move.newsquare

    moveCharacteristics = getMoveCharacteristics(move)
    slope,distance,rowDiff,colDiff = moveCharacteristics

    movePiece = currentPosDict.get(oldSquare)
    if isinstance(movePiece, Piece.Piece):
        movePieceType = movePiece.piecetype
        #print(movePieceType)
    else:
        print("failed isinstance Piece")
        print("Something has gone HORRIBLY wrong. Probably pieces somehow getting into the same square")
        print("This happens when the visual board is desynced with the backend position dictionary.")
        print("object that failed:")
        print(movePiece)
        return [False, currentPosDict, "normal"]  # returns a currentposDict to correct for any errors



    #0. did the piece move at all
    if oldSquare == newSquare:
        print("piece did not move")
        return [False,currentPosDict] #returns a currentposDict to correct for any errors

    #print("thru 0")

    #1. is it your turn: if not return False
    if getTurnColor(moveNumber) != movePlayerColor:
        print("wrong color for turn")
        return [False,currentPosDict, "normal"] #returns a currentposDict to correct for any errors

    #print("thru 1")

    # 1.5: is piecetype Pawn or King

    pathSquares = getPathSquares(move)
    intersectPieces = getIntersectPieces(pathSquares, currentPosDict)
    if movePieceType == "PAWN" or movePieceType == "KING":
        # 1.9: does move shape form a special move?

        isAllowedSpecial = getMoveSpecial(move, movePiece, currentPosDict) #func not good yet

        if isAllowedSpecial[0]: #if special move WAS good
            #print("special allowed")


            if (movePiece.piecetype == "PAWN" and distance == 2.0 and slope==np.inf and len(intersectPieces)>0):
                print("stopped grasshopper case")
                return [False,currentPosDict, "normal"]

            else:
                #print("allowed special")
                return isAllowedSpecial

        #print("after doMoveSpecial")
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


        #print(slope)
        #print(distance)
        #print(rowDiff)
        #print(colDiff)
        #print(movePiece.piecetype)

        if not(movePiece.piecetype == "PAWN" and distance == np.sqrt(2) and abs(slope) == 1.0):
            print("illegal move shape")
            return [False,currentPosDict, "normal"] #returns a currentposDict to correct for any errors

    #print("thru 2")

    # 3. are there multiple pieces in the path (auto fail)
    pathSquares = getPathSquares(move)
    intersectPieces = getIntersectPieces(pathSquares,currentPosDict)
    if len(intersectPieces) >= 2:
        print("multiple intersected pieces")
        return [False,currentPosDict, "normal"] #returns a currentposDict to correct for any errors

    #print("thru 3")

    # 4. Does the intersect path contain any of the same color pieces
    for square in pathSquares:
        piece = currentPosDict.get(square)
        if piece is not None:
            if piece.color == movePiece.color:
                if piece != movePiece:
                    print("path contained same color piece")
                    return [False,currentPosDict, "normal"] #returns a currentposDict to correct for any errors

    #print("thru 4")

    # 5. is it a take move? if take king, VICTORY
    if len(intersectPieces) == 1:
        isAllowedTake = getTakeMove(move, movePiece, currentPosDict)
        if isAllowedTake is None:
            return [False,currentPosDict, "normal"] #returns a currentposDict to correct for any errors
        if isAllowedTake[0]:
            #print("allowed take")
            #print(isAllowedTake)
            return isAllowedTake


        else:
            #print("disallowed take")
            return [False,currentPosDict, "normal"] #returns a currentposDict to correct for any errors


    #6 catch diagonal pawns

    if movePieceType=="PAWN" and len(intersectPieces) == 0 and distance == np.sqrt(2) and abs(slope) == 1.0:
        print("caught diagonal pawn move")
        return [False, currentPosDict, "normal"]

    print("got through ALL checks")
    return [True,currentPosDict,"normal"]

def getTakeMove(move, movePiece, currentPosDict):

    oldSquare = move.oldsquare
    newSquare = move.newsquare
    moveChar = getMoveCharacteristics(move)
    slope,distance, rowDiff, colDiff = moveChar

    takenPiece = currentPosDict.get(newSquare)

    movePieceType = movePiece.piecetype

    if movePieceType == "PAWN":
        #print("takemove pawn")

        #print(slope)
        #print(distance)
        #print(rowDiff)
        #print(colDiff)

        if slope == np.inf:
            if takenPiece is not None:
                #print("takemove pawn inf slope")
                return [False,currentPosDict, "normal"] #returns a currentposDict to correct for any errors

        elif distance == np.sqrt(2) and abs(slope) == 1.0:
            #print("takemove pawn npsqrt2 slope")
            if takenPiece is not None:
                return [True, currentPosDict, "take"]



    elif takenPiece.piecetype == "KING":
        return [True,currentPosDict,"win",move.player.color]

    else:
        #print("last in takemove")
        return [True,currentPosDict,"take"]

def doDoublePawn(Move, movePiece, currentPosDict):
    #print("double pawn check")
    if movePiece.hasMoved:
        return [False, currentPosDict, "normal"]  # returns a currentposDict to correct for any errors
    elif not movePiece.hasMoved:
        return [True,currentPosDict, "normal"] #returns a currentposDict to correct for any errors

def getMoveSpecial(move: Move, movePiece: Piece.Piece,currentPosDict: dict):
    #print("GET MOVE SPECIAL CHECK")
    moveCharacteristics = getMoveCharacteristics(move)
    slope, distance, rowDiff, colDiff = moveCharacteristics
    movePieceType = movePiece.piecetype



    if not movePiece.hasMoved and distance==2 and slope==0 and movePieceType == "KING":
        #print("going to doCastle")
        specialMove = getCastle(move, movePiece, currentPosDict)
        return specialMove

    if distance == 2 and slope == np.inf and movePieceType == "PAWN":
        specialMove = doDoublePawn(Move, movePiece, currentPosDict)
        return specialMove


    return [False,currentPosDict, "normal"]


def getCastle(move: Move, movePiece: Piece.Piece, currentPosDict: dict):
    oldSquare = move.oldsquare
    newSquare = move.newsquare

    xlist = ["a", "b", "c", "d", "e", "f", "g", "h"]
    ylist = ["1", "2", "3", "4", "5", "6", "7", "8"]

    oldSquareX = xlist.index(oldSquare[0])
    oldSquareY = ylist.index(oldSquare[1])

    newSquareX = xlist.index(newSquare[0])
    newSquareY = ylist.index(newSquare[1])


    xDiff = newSquareX - oldSquareX
    yDiff = newSquareY - oldSquareY


    side = ""
    if xDiff == 2 and yDiff == 0:
        side = "kingside"

    if xDiff == -2 and yDiff == 0:
        side = "queenside"


    if side == "kingside":
        oldSquareRook = "h" + str(oldSquareY + 1)
        newSquareRook = "f" + str(oldSquareY + 1)

    elif side == "queenside":
        oldSquareRook = "a" + str(oldSquareY + 1)
        newSquareRook = "d" + str(oldSquareY + 1)

    else:
        print("failed kingside / queenside checks: side is not either")
        return [False,currentPosDict, "normal"] #returns a currentposDict to correct for any errors

    castle_color = "None"

    if oldSquareY + 1 == 1:
        castle_color = "white"

    if oldSquareY + 1 == 8:
        castle_color = "black"

   # print(movePiece.piecetype)
   # print(movePiece.color)


    print(f"side: {side}, rook square, {oldSquareRook}")

    rook = currentPosDict.get(oldSquareRook)
   # print(rook.color)
    if rook is None:
        #print("rook fail none")
        return [False,currentPosDict, "normal"] #returns a currentposDict to correct for any errors

    if rook.piecetype != "ROOK":
        #print("rook fail none: piece on rookSquare not rook")
        return [False,currentPosDict, "normal"] #returns a currentposDict to correct for any errors

    if rook.color != movePiece.color:
        #print("rook fail color mismatch")
        return [False,currentPosDict, "normal"] #returns a currentposDict to correct for any errors

    if rook.hasMoved or movePiece.hasMoved:
        #print("hasmoved fail")
        return [False,currentPosDict, "normal"] #returns a currentposDict to correct for any errors


    oldSquareKing = oldSquare
    newSquareKing = newSquare

    if oldSquareKing != "e1" and oldSquareKing != "e8":
        #print("oldSquareKing not e1 or e8")
        return [False,currentPosDict, "normal"] #returns a currentposDict to correct for any errors

    firstMoveTest = Move(oldSquareKing,oldSquareRook,move.player)
    firstPathTrace = getPathSquares(firstMoveTest)
    firstIntersectPieces = getIntersectPieces(firstPathTrace,currentPosDict)
    # print(f"doCastleIntersectPieces from {oldSquare} to {rookSquare}")

    if not len(firstIntersectPieces)==1 or not firstIntersectPieces[0] == rook: #is the area clear between king and rook
        print("failed: area was not clear between king and rook")
        for item in firstIntersectPieces:
            print("intersection: ", item.piecetype, "on", item.squareName)
        return [False,currentPosDict, "normal"] #returns a currentposDict to correct for any errors



    checkMoveTest = Move(oldSquareKing,newSquareKing,move.player)
    checkTestPathTrace = getPathSquares(checkMoveTest)
    #print("checking for any checks if king was in ",checkTestPathTrace)
    for square in checkTestPathTrace:
        index = checkTestPathTrace.index(square)
        if castle_color == "white":
            oldSquareKingTest = "e1"

        #print(square, index)
        imaginaryPosDict = currentPosDict
        imaginaryKing = Piece.Piece(square, "KING" ,castle_color)

        if square in imaginaryPosDict.keys():
            imaginaryPosDict.pop(square)

        else:
            kingLocations = []
            print("square somehow not in keys")
            print("square:", square)
            testforking = [(x, y.piecetype) for (x, y) in imaginaryPosDict.items()]
            for item in testforking:
                x, y = item
                if y == "KING":
                    print(x, "King")

        imaginaryPosDict.update({square: imaginaryKing})

        checkableSquares = Check.getAllCheckableSquares(square, imaginaryPosDict)




        isChecked = Check.isKingInCheck(imaginaryKing,imaginaryPosDict)


        #print("for square = ",square,"checkable = ",checkableSquares)
        checkSquares = Check.getKingCheckList(imaginaryKing,imaginaryPosDict)
        #print("King on", imaginaryKing.squareName, ": ", checkSquares)


        if isChecked:
            print("move went through check if king was on ", square)
            return [False,currentPosDict, "normal"] #returns a currentposDict to correct for any errors


    newPosDict = currentPosDict
    KingPiece = newPosDict.get(oldSquareKing)
    newPosDict.pop(oldSquareKing)
    newPosDict.update({newSquareKing:KingPiece}) #UPDATE KING POSITION ON SUCCESS

    rookPiece = newPosDict.get(oldSquareRook)
    newPosDict.pop(oldSquareRook)
    newPosDict.update({newSquareRook:rookPiece}) #UPDATE ROOK POSITION ON SUCCESS


    infoList = [True, newPosDict, "castle", (oldSquareKing,newSquareKing),(oldSquareRook,newSquareRook),(castle_color,side)]
    return infoList







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


