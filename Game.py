import Board
import Piece
import Move

class Game:
    def __init__(self):
        self.player1 = Player(player1_name, 1)
        self.player2 = Player(player2_name, 2)
        self.player1_color = Color(self.player1)
        self.player2_color = Color(self.player2)
        self.board = Board.Board()
        self.moveNumber = 1

    def nextMove(self):
        self.moveNumber += 1

    def getTurnColor(self):
        remainder = self.moveNumber % 2
        if remainder == 1:
            return "white"
        elif remainder == 0:
            return "black"
        else:
            return "error"

    def updatePosDict(self, oldSquare, newSquare):
        if Move.isMoveLegal(oldSquare, newSquare):

            oldKey = oldSquare
            oldVal = self.board.currentPosDict.get(oldKey)

            newKey = newSquare
            newVal = self.board.currentPosDict.get(newKey)


class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number

















"""[print(piecetype, ": ", getPointValue(piecetype)) for piecetype in PieceType.getTypeList()]
rook = Piece(Position("a1"), "Rook", "white")
print("col: ", rook.position.column)
print("row: ", rook.position.row)
print("name: ", rook.piecetype)
print("color: ", rook.color)"""


