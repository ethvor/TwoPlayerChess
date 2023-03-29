import Graphics
import Move
import Piece
import Board
import Player
import Check








#Graphics.initialGui()



whitePlayer = Player.Player("white")
blackPlayer = Player.Player("black")



oldSquare = "e1"
newSquare = "d1"


move = Move.Move(oldSquare, newSquare, whitePlayer)

board = Board.Board()

pathSquares = Move.getPathSquares(move)
intersectPieces = Move.getIntersectPieces(pathSquares,board)
intersectPieceNames = [pieceObj.piecename for pieceObj in intersectPieces]
#print(intersectPieceNames)

legal = Move.isMoveLegal(move,board)
print(legal)


pieceObject = Piece.Piece("d3", "KING", "black")
print("\n\ncheck test\n\n")
Check.isKingChecked(pieceObject,board)