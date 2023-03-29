import Graphics
import Move
import Piece
import Board
import Player
import Check

whitePlayer = Player.Player("white")
blackPlayer = Player.Player("black")







#Graphics.initialGui()



"""NEXT:

make canTakePiece and killPiece in Move.py.

hopefully implementing these in move and legal and graphics wont be too bad

make sure it fixes the instanceof glitch that occurs when pieces overlap

"""





oldSquare = "e1"
newSquare = "d1"


move = Move.Move(oldSquare, newSquare, whitePlayer)

board = Board.Board()




pieceObject = Piece.Piece("d4", "KING", "white")
#print("\n\ncheck test\n\n")

#print(Check.isKingInCheck(pieceObject,board))

Graphics.initialGui()
