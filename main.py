'''GUI for Pathfinding Algorithm visualizer

@TODO:
- design OOP interface
- make readme file
- 
- algorithm may runs only if start and target tiles are selected
- show message when algorithm found NO solution
- make algorithm go faster and slower
'''

import pygame
from pathfinder.constants import HEADER_HEIGHT, INDENT, ROWS, TILE_SIZE, WIDTH, HEIGHT, WHITE
from pathfinder.canvas import Canvas
from pathfinder.dfs import Dfs
from pathfinder.dijkstra import Dijkstra


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
    canvas.set_alg(Dfs())
    
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
                            

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    canvas.set_alg(Dfs())
                    canvas.set_alg_prompt("Depth-First Search Algorithm, unweighted and does not guearantee shortest path")
                elif event.key == pygame.K_2:
                    canvas.set_alg(Dijkstra(canvas))
                    canvas.set_alg_prompt("Dijkstra Weighted Algorithm, guarantees shortest path")
                elif event.key == pygame.K_SPACE and canvas.get_target() and canvas.get_start():
                    canvas.run_alg(game_window, canvas)
                    canvas.draw_shortest_path(game_window)
                elif event.key == pygame.K_r:
                    canvas = Canvas()


        canvas.draw_canvas(game_window)

        pygame.display.update()

    pygame.quit()

main()
