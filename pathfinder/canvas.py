'''
@TODO:
- make grid color more faint. Probably by drawing lines instead of squares
'''

import pygame
from pathfinder.constants import BLACK, DARK_PURPLE, PURPLE, SKYBLUE, COLS, ROWS, TILE_SIZE, CANVAS_XY
from .tile import Tile


class Canvas:
    def __init__(self):
        self.canvas = self.initialize_canvas()
        self.start_tile = self.canvas[ROWS//2-1][COLS//2-COLS//4]
        self.target_tile = self.canvas[ROWS//2-1][COLS//2+COLS//4]
        #self.set_start_target()

    def initialize_canvas(self) -> list:
        canvas = []
        for row in range(ROWS):
            canvas.append([])
            for col in range(COLS):
                canvas[row].append(Tile(row,col))
        
        return canvas

    def set_start_target(self) -> None:
        #set as start tile
        self.start_tile.make_start()
        #set as target tile
        self.target_tile.make_target()
    
    def set_target(self):
        tile = self.canvas[1][22]
        tile.make_start()

    def make_start_tile(self, row, col):
        tile = self.canvas[row][col]
        tile.make_start()

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
    
    def draw_canvas(self, game_window):
        self.draw_tiles(game_window)
        self.draw_grid(game_window)
        