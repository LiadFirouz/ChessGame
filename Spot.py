SHIFT_FOR_PHOTO = 20
CELL_SIZE = 80


class Spot:

    def __init__(self, kind, x, y, isWhite, isKilled):
        self.kind = kind
        self.x = x
        self.y = y
        self.isWhite = isWhite
        self.killed = isKilled
        self.row = (x - SHIFT_FOR_PHOTO) / CELL_SIZE
        self.col = (y - SHIFT_FOR_PHOTO) / CELL_SIZE

    def get_Kind(self):
        return self.kind

    def get_X(self):
        return self.x

    def get_Y(self):
        return self.y

    def isKilled(self):
        return self.killed

    def setKilled(self, killed):
        self.killed = killed

    def __str__(self):
        print(f"kind: {self.kind}, x:{self.row}, y: {self.col}, isWhite: {self.isWhite}, isKilled:{self.killed}")
