import Piece


#piece1 = Piece.Piece(squareName, pieceType, pieceColor)

class Board:
    def __init__(self):

        self.whiteBishop1 = Piece.Piece("c1", "Bishop", "white")
        self.whiteBishop2 = Piece.Piece("f1", "Bishop", "white")
        self.whiteKing = Piece.Piece("e1", "King", "white")
        self.whiteKnight1 = Piece.Piece("b1", "Knight", "white")
        self.whiteKnight2 = Piece.Piece("g1", "Knight", "white")
        self.whiteQueen = Piece.Piece("d1", "Queen", "white")
        self.whiteRook1 = Piece.Piece("a1", "Rook", "white")
        self.whiteRook2 = Piece.Piece("h1", "Rook", "white")

        self.whitePawn1 = Piece.Piece("a2", "Pawn", "white")
        self.whitePawn2 = Piece.Piece("b2", "Pawn", "white")
        self.whitePawn3 = Piece.Piece("c2", "Pawn", "white")
        self.whitePawn4 = Piece.Piece("d2", "Pawn", "white")
        self.whitePawn5 = Piece.Piece("e2", "Pawn", "white")
        self.whitePawn6 = Piece.Piece("f2", "Pawn", "white")
        self.whitePawn7 = Piece.Piece("g2", "Pawn", "white")
        self.whitePawn8 = Piece.Piece("h2", "Pawn", "white")

        self.blackBishop1 = Piece.Piece("c8", "Bishop", "black")
        self.blackBishop2 = Piece.Piece("f8", "Bishop", "black")
        self.blackKing = Piece.Piece("e8", "King", "black")
        self.blackKnight1 = Piece.Piece("b8", "Knight", "black")
        self.blackKnight2 = Piece.Piece("g8", "Knight", "black")
        self.blackQueen = Piece.Piece("d8", "Queen", "black")
        self.blackRook1 = Piece.Piece("a8", "Rook", "black")
        self.blackRook2 = Piece.Piece("h8", "Rook", "black")

        self.blackPawn1 = Piece.Piece("a7", "Pawn", "black")
        self.blackPawn2 = Piece.Piece("b7", "Pawn", "black")
        self.blackPawn3 = Piece.Piece("c7", "Pawn", "black")
        self.blackPawn4 = Piece.Piece("d7", "Pawn", "black")
        self.blackPawn5 = Piece.Piece("e7", "Pawn", "black")
        self.blackPawn6 = Piece.Piece("f7", "Pawn", "black")
        self.blackPawn7 = Piece.Piece("g7", "Pawn", "black")
        self.blackPawn8 = Piece.Piece("h7", "Pawn", "black")

        startPieces = [self.whiteBishop1, self.whiteBishop2, self.whiteKing, self.whiteKnight1, self.whiteKnight2,
                       self.whiteQueen, self.whiteRook1,
                       self.whiteRook2, self.whitePawn1, self.whitePawn2, self.whitePawn3, self.whitePawn4,
                       self.whitePawn5, self.whitePawn6, self.whitePawn7,
                       self.whitePawn8, self.blackBishop1, self.blackBishop2, self.blackKing, self.blackKnight1,
                       self.blackKnight2, self.blackQueen,
                       self.blackRook1, self.blackRook2, self.blackPawn1, self.blackPawn2, self.blackPawn3,
                       self.blackPawn4, self.blackPawn5, self.blackPawn6, self.blackPawn7, self.blackPawn8]

        col = ["a", "b", "c", "d", "e", "f", "g", "h"]
        row = ["1", "2", "3", "4", "5", "6", "7", "8"]

        allPositions = {}

        # CHANGE THIS SECTION TO INCLUDE A TUPLE THAT INCLUDES WHETHER A PIECE IS AT A GIVEN INDEX.
        # IE: allPositions = [(a1,whiteRook1), (a2,whiteKnight1), ... , (c4, None), ... , (h8,blackRook2)]
        # this change will happen in the loop down there

        for num in row:
            for char in col:
                squareName = char + num


                for piece in startPieces:
                    if piece.squareName == squareName:
                        thisDefinition = {piece.squareName: piece}
                        allPositions.update(thisDefinition)


        self.initialPosDict = allPositions
        self.currentPosDict = allPositions #constructed to initialPosDict because no moves have occurred


board = Board()
dict = board.initialPosDict
print(dict)