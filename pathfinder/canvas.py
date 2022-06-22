'''
@TODO:
- Make colors of the game better
- Add choice of algorithms:
-- Dijkstra
-- A*
-- Maze creation algorithnm
'''

import pygame
from pathfinder.constants import BLACK, DARK_PURPLE, HEADER, INDENT, PURPLE, SKYBLUE, COLS, ROWS, TILE_SIZE, CANVAS_XY, WHITE, WIDTH
from .tile import Tile


class Canvas:
    def __init__(self):
        self.start_tile = None
        self.target_tile = None
        self.canvas = self.initialize_canvas()
        self.alg = None

    def initialize_canvas(self) -> list:
        canvas = []
        for row in range(ROWS):
            canvas.append([])
            for col in range(COLS):
                canvas[row].append(Tile(row,col))

        self.start_tile = canvas[ROWS//2-1][COLS//2-COLS//4]
        self.target_tile = canvas[ROWS//2-1][COLS//2+COLS//4]
        self.start_tile.make_start()
        self.target_tile.make_target()
        self.update_neighbours(canvas)
        
        return canvas

    def update_neighbours(self, canvas):
        for row in canvas:
            for tile in row:
                nrows = len(canvas)
                ncols = len(canvas[0])
                row, col = tile.get_row_col()

                if row-1 >= 0: #UPPER
                    tile.append_neighbours(canvas[row-1][col])
                if row+1 < nrows: #LOWER
                    tile.append_neighbours(canvas[row+1][col])
                if col-1 >= 0: #LEFT
                    tile.append_neighbours(canvas[row][col-1])
                if col+1 < ncols: #RIGHT
                    tile.append_neighbours(canvas[row][col+1])

    def set_alg(self, alg):
        self.alg = alg

    def run_alg(self, game_window, canvas):
        self.alg.run(game_window, canvas)

    def reset_canvas(self):
        self.canvas = self.initialize_canvas()

    def get_start(self):
        return self.start_tile

    def get_target(self):
        return self.target_tile

    def get_canvas(self):
        return self.canvas

    def make_tile(self, row, col):
        tile = self.canvas[row][col]
        #if there is no start
        if not self.get_start():
            self.start_tile = tile
            tile.make_start()
        elif not self.get_target():
            self.target_tile = tile
            tile.make_target()
        elif not tile.is_target() and not tile.is_start():
            tile.make_wall()
    
    def reset_tile(self, row, col):
        tile = self.canvas[row][col]
        if tile.is_start():
            self.start_tile = None
        elif tile.is_target():
            self.target_tile = None
        tile.set_unvisited()


    def set_target(self):
        tile = self.canvas[1][22]
        tile.make_start()

    def make_start_tile(self, row, col):
        tile = self.canvas[row][col]
        tile.make_start()


    def draw_shortest_path(self, game_window):
        curr = self.target_tile.get_parent()

        while curr and not curr.is_start():
            curr.set_shortest()
            curr = curr.get_parent()
            self.draw_canvas(game_window)


    def draw_tiles(self, game_window):
        for row in range(ROWS):
            for col in range(COLS):
                #rect = pygame.Rect(980, 100 ,25, 25)
                #pygame.draw.rect(game_window, (0,0,0), rect, 0)
                next_tile_x = CANVAS_XY[0]+col*TILE_SIZE
                next_tile_y = CANVAS_XY[1]+row*TILE_SIZE

                rect = pygame.Rect(next_tile_x, next_tile_y, TILE_SIZE, TILE_SIZE)
                tile = self.canvas[row][col]
                pygame.draw.rect(game_window, tile.color, rect, 0)

    def draw_grid(self, game_window):
        for row in range(ROWS):
            for col in range(COLS):
                next_tile_x = CANVAS_XY[0]+col*TILE_SIZE
                next_tile_y = CANVAS_XY[1]+row*TILE_SIZE
                
                rect = pygame.Rect(next_tile_x, next_tile_y ,TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(game_window, SKYBLUE, rect, 1)
    
    def draw_header(self, game_window):
        rect = pygame.Rect(INDENT, INDENT, WIDTH-INDENT*2, 75)
        pygame.draw.rect(game_window, HEADER, rect, 0)
        
        font_header = pygame.font.Font("fonts/NotoSans-ExtraBold.ttf", 30)
        txt = "Pathfinding Algorithms Visualizer"
        txt_surface = font_header.render(txt, True, WHITE) 
        game_window.blit(txt_surface, (WIDTH/2-len(txt)//2*16, 22))


    def draw_canvas(self, game_window):
        self.draw_tiles(game_window)
        self.draw_grid(game_window)
        self.draw_header(game_window)

        pygame.display.update()
        