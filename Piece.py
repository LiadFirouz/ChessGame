from main import SHIFT_FOR_PHOTO, CELL_SIZE


class Piece:

    def __init__(self, x, y, isWhite):
        self.killed = False
        self.isWhite = False
        self.row = (x - SHIFT_FOR_PHOTO) / CELL_SIZE
        self.col = (y - SHIFT_FOR_PHOTO) / CELL_SIZE

    def isWhite(self):
        return self.white

    def isKilled(self):
        return self.killed

    def setKilled(self, killed):
        self.killed = killed

