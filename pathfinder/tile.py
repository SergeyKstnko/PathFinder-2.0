from pathfinder.constants import WHITE

from .constants import DARK_PURPLE, PURPLE, WHITE

class Tile:
    
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.color = WHITE

    def is_start_tile(self) -> bool:
        return self.color == PURPLE

    def is_target_tile(self) -> bool:
        return self.color == DARK_PURPLE
    
    #when not is unvisited
        #its color = white
        #border is blue

    #when node is marked as discovered
        #color -> blue
        #border white

    #for the shortest path
        #color is yellow
        #border is also yellow


    ### HOW WILL IMPLEMENT BORDER AND COLOR
    #1) color inside first
    #2) color border
    