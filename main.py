import pygame

import Piece
import Spot

pygame.init()

SHIFT_FOR_PHOTO = 20
CELL_SIZE = 80


class InitGame:

    def __init__(self, width, height):
        self.surface_width = width
        self.surface_height = height

        self.display_surface = pygame.display.set_mode((self.surface_width, self.surface_height))
        pygame.display.set_caption('Chess Game')
        image = pygame.image.load(r'C:\Users\LiadF\PycharmProjects\chessgame\img\chess_board.png')
        self.display_surface.blit(pygame.transform.scale(image, (self.surface_width, self.surface_height)), (0, 0))

        self.board = self.init_board()
        self.draw_pieces(board=self.board)

    def init_board(self):

        kind = None
        board = [[Spot.Spot(kind, row, col, True, True) for col in range(8)] for row in range(8)]

        for row in range(8):
            x = (20 + 80 * row)
            for col in range(8):
                y = (20 + 80 * col)

                kind = None
                if row == 1 or row == 6:
                    kind = "pawn"
                    if row == 1:
                        isWhite = False

                if row == 0 or row == 7:
                    if row == 0:
                        isWhite = False
                    if col == 0 or col == 7:
                        kind = "rook"
                    if col == 1 or col == 6:
                        kind = "knight"
                    if col == 2 or col == 5:
                        kind = "bishop"

                if row == 0 and col == 3:
                    kind = "queen"
                if row == 0 and col == 4:
                    kind = "king"

                if row == 7 and col == 3:
                    kind = "king"
                if row == 7 and col == 4:
                    kind = "queen"

                board[row][col] = Spot.Spot(kind, y, x, isWhite, True)
                isWhite = True

        # self.print_board(board)
        return board

    def draw_pieces(self, board):

        start_x, start_y = 20, 10

        b_pawn_img = pygame.image.load(r'C:\Users\LiadF\PycharmProjects\chessgame\img\128h\b_pawn.png')
        b_king_img = pygame.image.load(r'C:\Users\LiadF\PycharmProjects\chessgame\img\128h\b_king.png')
        b_bishop_img = pygame.image.load(r'C:\Users\LiadF\PycharmProjects\chessgame\img\128h\b_bishop.png')
        b_knight_img = pygame.image.load(r'C:\Users\LiadF\PycharmProjects\chessgame\img\128h\b_knight.png')
        b_queen_img = pygame.image.load(r'C:\Users\LiadF\PycharmProjects\chessgame\img\128h\b_queen.png')
        b_rook_img = pygame.image.load(r'C:\Users\LiadF\PycharmProjects\chessgame\img\128h\b_rook.png')

        w_pawn_img = pygame.image.load(r'C:\Users\LiadF\PycharmProjects\chessgame\img\128h\w_pawn.png')
        w_king_img = pygame.image.load(r'C:\Users\LiadF\PycharmProjects\chessgame\img\128h\w_king.png')
        w_bishop_img = pygame.image.load(r'C:\Users\LiadF\PycharmProjects\chessgame\img\128h\w_bishop.png')
        w_knight_img = pygame.image.load(r'C:\Users\LiadF\PycharmProjects\chessgame\img\128h\w_knight.png')
        w_queen_img = pygame.image.load(r'C:\Users\LiadF\PycharmProjects\chessgame\img\128h\w_queen.png')
        w_rook_img = pygame.image.load(r'C:\Users\LiadF\PycharmProjects\chessgame\img\128h\w_rook.png')

        for row in range(board.__len__()):
            for col in range(board.__len__()):
                if board[row][col].kind is not None:
                    if board[row][col].isWhite:
                        image = b_pawn_img

                        if board[row][col].kind == "king":
                            image = b_king_img
                        if board[row][col].kind == "bishop":
                            image = b_bishop_img
                        if board[row][col].kind == "knight":
                            image = b_knight_img
                        if board[row][col].kind == "queen":
                            image = b_queen_img
                        if board[row][col].kind == "rook":
                            image = b_rook_img


                    else:
                        image = w_pawn_img

                        if board[row][col].kind == "king":
                            image = w_king_img
                        if board[row][col].kind == "bishop":
                            image = w_bishop_img
                        if board[row][col].kind == "knight":
                            image = w_knight_img
                        if board[row][col].kind == "queen":
                            image = w_queen_img
                        if board[row][col].kind == "rook":
                            image = w_rook_img

                    self.display_surface.blit(pygame.transform.scale(image, (40, 50)),
                                              (board[row][col].x, board[row][col].y))

    def print_board(self, board):
        print("------------------------------------")
        print("new BOARD:")
        for row in board:
            for obj in row:
                print(obj.__str__())


def main():
    WIDTH, HEIGHT = 640, 640
    init_game_obj = InitGame(WIDTH, HEIGHT)
    run = True

    while run:

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():
            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for row in range(init_game_obj.board.__len__()):
                    for col in range(init_game_obj.board.__len__()):
                        if init_game_obj.board[row][col].get_Kind() is not None:
                            # print(init_game_obj.board[row][col].kind)
                            green_frame = pygame.image.load(
                                r'C:\Users\LiadF\PycharmProjects\chessgame\img\green_frame.png')
                            init_game_obj.display_surface.blit(pygame.transform.scale(green_frame, (80, 80)),
                                                               (init_game_obj.board[row][col].x - 20,
                                                                init_game_obj.board[row][col].y - 20))
                # if ballrect.collidepoint(event.pos):

            # Draws the surface object to the screen.

        pygame.display.update()


if __name__ == '__main__':
    main()
