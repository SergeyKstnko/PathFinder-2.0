'''
@TODO:
- Add choice of algorithms:
-- A*
-- Maze creation algorithnm
'''

import pygame
from pathfinder.constants import BLACK, BLUE, BOTTOM_INDENT, DARK_BLUE, DARK_PURPLE, HEADER, HEIGHT, INDENT, PURPLE, SKYBLUE, COLS, ROWS, TILE_SIZE, CANVAS_XY, WHITE, WIDTH, PROMPT_CORAL, YELLOW
from .tile import Tile


class Canvas:
    def __init__(self):
        self.start_tile = None
        self.target_tile = None
        self.canvas = self.initialize_canvas()
        self.alg = None
        self.alg_prompt = "Press 1 or 2 to pick an algorithm and then"    #TOP LEFT PROMPT
        self.alg_prompt_col = PROMPT_CORAL
        self.status_prompt = "Press SPACE to run it."    #TOP RIGHT PROMPT
        self.status_col = PROMPT_CORAL

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

    def update_neighbours(self):
        canvas = self.canvas
        for row in canvas:
            for tile in row:
                nrows = len(canvas)
                ncols = len(canvas[0])
                row, col = tile.get_row_col()

                if row-1 >= 0 and not canvas[row-1][col].is_wall(): #UPPER
                    tile.append_neighbours(canvas[row-1][col])
                if row+1 < nrows and not canvas[row+1][col].is_wall(): #LOWER
                    tile.append_neighbours(canvas[row+1][col])
                if col-1 >= 0 and not canvas[row][col-1].is_wall(): #LEFT
                    tile.append_neighbours(canvas[row][col-1])
                if col+1 < ncols and not canvas[row][col+1].is_wall(): #RIGHT
                    tile.append_neighbours(canvas[row][col+1])


    def set_alg(self, alg):
        self.alg = alg
        self.alg_prompt = alg.get_alg_prompt()
        self.alg_prompt_col = HEADER


    def run_alg(self, game_window, canvas_object):
        if self.alg:
            self.update_neighbours()
            self.alg.run(game_window, canvas_object)

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
            if not self.get_target():
                self.status_prompt = " Pick target node."

        elif not self.get_target():
            self.target_tile = tile
            tile.make_target()
            self.status_prompt = "Press SPACE to run it."
        elif not tile.is_target() and not tile.is_start():
            tile.make_wall()
    
    def reset_tile(self, row, col):
        tile = self.canvas[row][col]
        if tile.is_start():
            self.start_tile = None
            self.status_prompt = "Pick start node."
        elif tile.is_target():
            self.target_tile = None
            if not self.get_start():
                self.status_prompt = "Pick start node."
            else:
                self.status_prompt = " Pick target node."
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
        game_window.blit(txt_surface, (WIDTH//2-len(txt)//2*16, 22))

        
        font_prompt = pygame.font.Font("fonts/NotoSans-ExtraBold.ttf", 15)
        
        tot_len = len(self.alg_prompt+""+ self.status_prompt)
        txt = self.alg_prompt.upper()
        #txt = self.alg_prompt+" "+ self.status_prompt.upper()
        txt_surface = font_prompt.render(txt, True, self.alg_prompt_col) 
        game_window.blit(txt_surface, (WIDTH//2-tot_len//2*9, 92))

        
        txt = self.status_prompt.upper()
        pos = tot_len//2 - len(txt) #position where this sign should be
        txt_surface = font_prompt.render(txt, True, self.status_col) 
        game_window.blit(txt_surface, (WIDTH//2+pos*9, 92))

    def draw_legend(self, game_window):
        legend_x = INDENT
        legend_y = HEIGHT-BOTTOM_INDENT+20

        #START NODE
        rect = pygame.Rect(legend_x+7, legend_y, TILE_SIZE-4, TILE_SIZE-4)
        pygame.draw.rect(game_window, PURPLE, rect, 0)
        rect = pygame.Rect(legend_x+7, legend_y, TILE_SIZE-4, TILE_SIZE-4)
        pygame.draw.rect(game_window, SKYBLUE, rect, 1)

        font_legend = pygame.font.Font("fonts/NotoSans-ExtraBold.ttf", 16)
        txt = "- Start Node"
        txt_surface = font_legend.render(txt, True, HEADER) 
        game_window.blit(txt_surface, (legend_x+34, legend_y-2))

        #TARGET NODE
        rect = pygame.Rect(legend_x+150, legend_y, TILE_SIZE-4, TILE_SIZE-4)
        pygame.draw.rect(game_window, DARK_PURPLE, rect, 0)
        rect = pygame.Rect(legend_x+150, legend_y, TILE_SIZE-4, TILE_SIZE-4)
        pygame.draw.rect(game_window, SKYBLUE, rect, 1)

        txt = "- Target Node"
        txt_surface = font_legend.render(txt, True, HEADER) 
        game_window.blit(txt_surface, (legend_x+177, legend_y-2))

        #PATH NODE
        rect = pygame.Rect(legend_x+312, legend_y, TILE_SIZE-4, TILE_SIZE-4)
        pygame.draw.rect(game_window, YELLOW, rect, 0)
        rect = pygame.Rect(legend_x+312, legend_y, TILE_SIZE-4, TILE_SIZE-4)
        pygame.draw.rect(game_window, SKYBLUE, rect, 1)

        txt = "- Shortest-path Node"
        txt_surface = font_legend.render(txt, True, HEADER) 
        game_window.blit(txt_surface, (legend_x+342, legend_y-2))

        #WALL NODE
        rect = pygame.Rect(legend_x+533, legend_y, TILE_SIZE-4, TILE_SIZE-4)
        pygame.draw.rect(game_window, BLACK, rect, 0)
        rect = pygame.Rect(legend_x+533, legend_y, TILE_SIZE-4, TILE_SIZE-4)
        pygame.draw.rect(game_window, SKYBLUE, rect, 1)

        txt = "- Wall Node"
        txt_surface = font_legend.render(txt, True, HEADER) 
        game_window.blit(txt_surface, (legend_x+563, legend_y-2))

        #DISCOVERED/PROCESSED NODE NODE
        rect = pygame.Rect(legend_x+673, legend_y, TILE_SIZE-4, TILE_SIZE-4)
        pygame.draw.rect(game_window, DARK_BLUE, rect, 0)
        rect = pygame.Rect(legend_x+673, legend_y, TILE_SIZE-4, TILE_SIZE-4)
        pygame.draw.rect(game_window, SKYBLUE, rect, 1)

        rect = pygame.Rect(legend_x+695, legend_y, TILE_SIZE-4, TILE_SIZE-4)
        pygame.draw.rect(game_window, BLUE, rect, 0)
        rect = pygame.Rect(legend_x+695, legend_y, TILE_SIZE-4, TILE_SIZE-4)
        pygame.draw.rect(game_window, SKYBLUE, rect, 1)

        txt = "- Discovered and Processed Nodes"
        txt_surface = font_legend.render(txt, True, HEADER) 
        game_window.blit(txt_surface, (legend_x+725, legend_y-2))

        font_legend = pygame.font.Font("fonts/NotoSans-ExtraBold.ttf", 14)
        txt = "You can press numbers on your keyboard to choose algorithms: 1.Dijkstra 2.Depth-first Search or 3.Breadth-first Search Algorithms."
        txt_surface = font_legend.render(txt, True, HEADER) 
        game_window.blit(txt_surface, (legend_x+7, legend_y+30))

        txt = "You can select and deselct squares and build walls with right/left mouse click."
        txt_surface = font_legend.render(txt, True, HEADER) 
        game_window.blit(txt_surface, (legend_x+7, legend_y+50))

        txt = "Press \"R\" to reset the canvas."
        txt_surface = font_legend.render(txt, True, HEADER) 
        game_window.blit(txt_surface, (legend_x+7, legend_y+70))


    def draw_canvas(self, game_window):
        self.draw_tiles(game_window)
        self.draw_grid(game_window)
        self.draw_header(game_window)
        self.draw_legend(game_window)
        
        pygame.display.update()
        
        