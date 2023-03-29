
class Piece:
    class PieceType:

        @staticmethod
        def getTypeList():
            return ["BISHOP", "KING", "KNIGHT", "PAWN", "QUEEN", "ROOK", "NONE"]

        def __init__(self, piecetype: str):

            piecetype = piecetype.upper()


            typelist = self.getTypeList()
            self.typelist = typelist
            if piecetype in typelist:
                self.type = piecetype
            else:
                print("\n\n\nERROR: piece type entered not in list")
                list = self.getTypeList()
                print("List: ", list)
                print("You entered: ", piecetype,"\n\n\n")



        def getPointValue(self, piecetype):
            val = {'BISHOP': 3, 'KING': 0, 'KNIGHT': 3, 'PAWN': 1, 'QUEEN': 9, 'ROOK': 5}
            return val[piecetype.type]


    class PieceColor:
        def __init__(self, color_str):
            self.color = color_str




    class PiecePosition:
        def __init__(self, squareName: str):

            column = squareName[0], row = squareName[1]
            if column in ["a", "b", "c", "d", "e", "f", "g", "h"]:
                self.column = column
            if row in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                self.row = row

            self.squareName = self.column + self.row

        def __init__(self, pos_notation: str):
            if pos_notation[0] in ["a", "b", "c", "d", "e", "f", "g", "h"]:
                self.column = pos_notation[0]

            if pos_notation[1] in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                self.row = pos_notation[1]

            self.squareName = self.column + self.row

    def __init__(self, squareName: str, piecetype: str, color: str): #Piece Class Init
        self.squareName = self.PiecePosition(squareName).squareName
        self.piecetype = self.PieceType(piecetype).type
        self.color = self.PieceColor(color).color
        self.piecename = self.color + self.piecetype
        self.hasMoved = False





