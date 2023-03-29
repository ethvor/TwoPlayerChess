import Graphics
import Move
import Piece
import Board
import Player









#Graphics.initialGui()



whitePlayer = Player.Player("white")
blackPlayer = Player.Player("black")



oldSquare = "d1"
newSquare = "d1"

#pieceObject = Piece.Piece(oldSquare, "QUEEN", "white")

move = Move.Move(oldSquare, newSquare, whitePlayer)

board = Board.Board()

pathSquares = Move.getPathSquares(move)
intersectPieces = Move.getIntersectPieces(pathSquares,board)
intersectPieceNames = [pieceObj.piecename for pieceObj in intersectPieces]
#print(intersectPieceNames)

legal = Move.isMoveLegal(move,board)
print(legal)