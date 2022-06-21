'''
@TODO:
- make grid color more faint. Probably by drawing lines instead of squares
'''

import pygame
from pathfinder.constants import BLACK, DARK_PURPLE, PURPLE, SKYBLUE, COLS, ROWS, TILE_SIZE, CANVAS_XY
from .tile import Tile


class Canvas:
    def __init__(self):
        self.start_tile = None
        self.target_tile = None
        self.canvas = self.initialize_canvas()

        
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
        
        return canvas
    
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
        print(self.start_tile.get_row_col())
    
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
    
    def draw_canvas(self, game_window):
        self.draw_tiles(game_window)
        self.draw_grid(game_window)

        pygame.display.update()
        