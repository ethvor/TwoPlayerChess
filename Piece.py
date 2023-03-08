from Game import Position
from Game import Color


class PieceType:

    @staticmethod
    def getTypeList():
        return ["BISHOP", "KING", "KNIGHT", "PAWN", "QUEEN", "ROOK", "NONE"]

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
    val = {'BISHOP': 3, 'KING': 0, 'KNIGHT': 3, 'PAWN': 1, 'QUEEN': 9, 'ROOK': 5, 'NONE': 0}

    isPieceType = isinstance(piecetype, PieceType)
    isString = isinstance(piecetype, str)

    if isPieceType:
        return val[piecetype.type]

    if isString:
        return val[piecetype]


[print(piecetype, ": ", getPointValue(piecetype)) for piecetype in PieceType.getTypeList()]

rook = Piece(Position("a1"), "Rook", "White")


print("col: ", rook.position.column)
print("row: ", rook.position.row)
print("name: ", rook.piecetype)
print("color: ", rook.color)
