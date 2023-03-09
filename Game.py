class Game:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name, 1)
        self.player2 = Player(player2_name, 2)
        self.player1_color = Color(self.player1)
        self.player2_color = Color(self.player2)


class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number


class Color:
    def __init(self, player):
        if player.number == 1:
            self.color == "white"
        else:
            self.color == "black"


class Position:
    def __init__(self, column, row):
        if column in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            self.column = column
        if row in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            self.row = row

        self.pos = self.column + self.row

    def __init__(self, pos_notation: str):
        if pos_notation[0] in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            self.column = pos_notation[0]

        if pos_notation[1] in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            self.row = pos_notation[1]

        self.pos = self.column + self.row


class PieceType:

    @staticmethod
    def getTypeList():
        return ["BISHOP", "KING", "KNIGHT", "PAWN", "QUEEN", "ROOK"]

    def __init__(self, piecetype: str):
        typelist = self.getTypeList()
        self.typelist = typelist
        if piecetype in typelist:
            self.type = piecetype


class Piece:
    def __init__(self, position: Position, piecetype: PieceType, color: Color):
        self.position = position
        self.piecetype = piecetype
        self.color = color


def getPointValue(piecetype):
    val = {'BISHOP': 3, 'KING': 0, 'KNIGHT': 3, 'PAWN': 1, 'QUEEN': 9, 'ROOK': 5}

    isPieceType = isinstance(piecetype, PieceType)
    isString = isinstance(piecetype, str)

    if isPieceType:
        return val[piecetype.type]

    if isString:
        return val[piecetype]


class Board:
    def __init__(self):

        self.whiteBishop1 = Piece(Position("c1"), "Bishop", "white")
        self.whiteBishop2 = Piece(Position("f1"), "Bishop", "white")
        self.whiteKing = Piece(Position("e1"), "King", "white")
        self.whiteKnight1 = Piece(Position("b1"), "Knight", "white")
        self.whiteKnight2 = Piece(Position("g1"), "Knight", "white")
        self.whiteQueen = Piece(Position("d1"), "Queen", "white")
        self.whiteRook1 = Piece(Position("a1"), "Rook", "white")
        self.whiteRook2 = Piece(Position("h1"), "Rook", "white")

        self.whitePawn1 = Piece(Position("a2"), "Pawn", "white")
        self.whitePawn2 = Piece(Position("b2"), "Pawn", "white")
        self.whitePawn3 = Piece(Position("c2"), "Pawn", "white")
        self.whitePawn4 = Piece(Position("d2"), "Pawn", "white")
        self.whitePawn5 = Piece(Position("e2"), "Pawn", "white")
        self.whitePawn6 = Piece(Position("f2"), "Pawn", "white")
        self.whitePawn7 = Piece(Position("g2"), "Pawn", "white")
        self.whitePawn8 = Piece(Position("h2"), "Pawn", "white")

        self.blackBishop1 = Piece(Position("c8"), "Bishop", "black")
        self.blackBishop2 = Piece(Position("f8"), "Bishop", "black")
        self.blackKing = Piece(Position("e8"), "King", "black")
        self.blackKnight1 = Piece(Position("b8"), "Knight", "black")
        self.blackKnight2 = Piece(Position("g8"), "Knight", "black")
        self.blackQueen = Piece(Position("d8"), "Queen", "black")
        self.blackRook1 = Piece(Position("a8"), "Rook", "black")
        self.blackRook2 = Piece(Position("h8"), "Rook", "black")

        self.blackPawn1 = Piece(Position("a7"), "Pawn", "black")
        self.blackPawn2 = Piece(Position("b7"), "Pawn", "black")
        self.blackPawn3 = Piece(Position("c7"), "Pawn", "black")
        self.blackPawn4 = Piece(Position("d7"), "Pawn", "black")
        self.blackPawn5 = Piece(Position("e7"), "Pawn", "black")
        self.blackPawn6 = Piece(Position("f7"), "Pawn", "black")
        self.blackPawn7 = Piece(Position("g7"), "Pawn", "black")
        self.blackPawn8 = Piece(Position("h7"), "Pawn", "black")

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
                posString = char + num
                position = Position(posString)

                thisPosition = position.pos
                thisPieceName = "None"

                for piece in startPieces:
                    if piece.position.pos == thisPosition:
                        thisPieceName = piece.color + piece.piecetype

                thisDefinition = {thisPosition: thisPieceName}

                allPositions.update(thisDefinition)

        self.posDict = allPositions


"""[print(piecetype, ": ", getPointValue(piecetype)) for piecetype in PieceType.getTypeList()]
rook = Piece(Position("a1"), "Rook", "white")
print("col: ", rook.position.column)
print("row: ", rook.position.row)
print("name: ", rook.piecetype)
print("color: ", rook.color)"""

board = Board()
print(board.posDict)
