
from .constants import BLACK, DARK_PURPLE, PURPLE, WHITE

class Tile:
    
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.color = WHITE

    def is_start(self) -> bool:
        return self.color == PURPLE

    def is_target(self) -> bool:
        return self.color == DARK_PURPLE

    def is_wall(self):
        return self.color == BLACK

    def make_start(self):
        self.color = PURPLE
    
    def make_target(self):
        self.color = DARK_PURPLE

    def make_wall(self):
        self.color = BLACK

    def make_unvisited(self):
        print("HERE")
        self.color = WHITE
    
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
    