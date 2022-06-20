'''GUI for Pathfinding Algorithm visualizer

@TODO:
- algorithm may run only if start and target tiles are selected
'''

import pygame
from pathfinder.constants import BOTTOM_INDENT, CANVAS_HEIGHT, CANVAS_WIDTH, COLS, DARK_BLUE, HEADER_HEIGHT, INDENT, PURPLE, ROWS, TILE_SIZE, WIDTH, HEIGHT, WHITE, YELLOW
from pathfinder.canvas import Canvas


FPS = 60
pygame.init()

game_window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("The Best Visualizer for PathFinding Algorithms")

def get_tile_coords(pos):
    col = (pos[0] - INDENT) // TILE_SIZE
    row = (pos[1] - HEADER_HEIGHT) // TILE_SIZE
    return row, col

def main():
    clock = pygame.time.Clock()
    run = True
    canvas = Canvas()
    
    while run:

        clock.tick(FPS)
        game_window.fill(WHITE)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                #these two if statements check if mouse click is within canvas boundaries
                if event.pos[0] > INDENT and event.pos[0] < WIDTH - INDENT:
                    if event.pos[1] > HEADER_HEIGHT and event.pos[1] < HEADER_HEIGHT+ROWS*TILE_SIZE:
                        row, col = get_tile_coords(event.pos)
                        if pygame.mouse.get_pressed()[0]: #left
                            canvas.make_tile(row, col)
                        elif pygame.mouse.get_pressed()[2]: #right
                            canvas.reset_tile(row, col)

                        #if right mouse buttong is clicked on the start or end node
                            #remove it
                            #place it where user will press left mouse        
            

        canvas.draw_canvas(game_window)
        pygame.display.update()
         
    pygame.quit()

main()
