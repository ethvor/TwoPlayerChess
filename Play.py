import Graphics
import Move
import Piece





piece = Piece.Piece("d4","PAWN","black")

oldSquare = piece.squareName
newSquare = "d3"
move = Move.Move(oldSquare,newSquare,1)

slope,distance,x,y = Move.getMoveCharacteristics(move)

print("slope:",slope)
print("distance:",distance)
print("rowDif:", x)
print("colDif:", y)
print("piece:",piece)


x = Move.isPathLegalShape(slope,distance,x,y,piece)
print(x)

#Graphics.initialGui()
