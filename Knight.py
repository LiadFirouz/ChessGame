import Piece
import math

class Knight(Piece):

    def __init__(self, piece: Piece):
        self.killed = False
        self.white = piece.white
        self.row = piece.row
        self.col = piece.col