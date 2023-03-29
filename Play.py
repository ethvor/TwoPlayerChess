import Graphics
import Move
import Piece
import Board
import Player
import Check

whitePlayer = Player.Player("white")
blackPlayer = Player.Player("black")

class GuiMoveAttempt:
    def __init__(self):
        self.oldSquare = "z9"
        self.newSquare = "q0"
        self.player = whitePlayer #hardcoded needs to be dynamic based on turn

latestMoveAttempt = GuiMoveAttempt()






#Graphics.initialGui()







oldSquare = "e1"
newSquare = "d1"


move = Move.Move(oldSquare, newSquare, whitePlayer)

board = Board.Board()




pieceObject = Piece.Piece("d4", "KING", "white")
#print("\n\ncheck test\n\n")

#print(Check.isKingInCheck(pieceObject,board))

Graphics.initialGui()
