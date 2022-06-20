'''GUI for Pathfinding Algorithm visualizer

'''

import pygame
from pathfinder.constants import BOTTOM_INDENT, COLS, HEADER_HEIGHT, INDENT, ROWS, TILE_SIZE, WIDTH, HEIGHT, WHITE
from pathfinder.canvas import Canvas


FPS = 60
pygame.init()

game_window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("The Best Visualizer for PathFinding Algorithms")

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        canvas = Canvas()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] > INDENT and event.pos[0] < WIDTH - INDENT:
                    if event.pos[1] > HEADER_HEIGHT and event.pos[1] < HEADER_HEIGHT+ROWS*TILE_SIZE:
                        x, y = pygame.mouse.get_pos()
                        gap_x = (WIDTH - INDENT*2) // COLS
                        gap_y = (HEIGHT-HEADER_HEIGHT-BOTTOM_INDENT) // ROWS

                        row = x // gap_x
                        col = y // gap_y

                        print(ROWS, COLS)
                        print(row, col)
                        #print((event.pos[0] - INDENT) // TILE_SIZE, (event.pos[1] - HEADER_HEIGHT) // TILE_SIZE)
                        #xpos = event.pos[0]-INDENT) // TILE_SIZE
                        #ypos = (event.pos[1] - )
            #if right mouse buttong is clicked on the start or end node
                #remove it
                #place it where user will press left mouse

        game_window.fill(WHITE)

        canvas.draw_canvas(game_window)

        pygame.display.update()
    pygame.quit()

main()
