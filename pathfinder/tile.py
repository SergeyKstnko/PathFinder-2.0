
from .constants import BLACK, BLUE, DARK_BLUE, DARK_PURPLE, PURPLE, WHITE, YELLOW
import math

class Tile:
    
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.color = WHITE
        self.parent = None

        #fields for Dijkstra
        self.neighbours = []
        self.intree = False
        self.weight = 1
        self.distance = math.inf #SHORTEST DISTANCE
        
    def append_neighbours(self, neighbour):
        self.neighbours.append(neighbour)

    def make_start(self):
        self.color = PURPLE
    
    def make_target(self):
        self.color = DARK_PURPLE

    def make_wall(self):
        self.color = BLACK

    def get_row_col(self):
        return self.row, self.col

    def get_neighbours(self):
        return self.neighbours
    
    def get_weight(self):
        return self.weight

    def get_distance(self):
        return self.distance

    def get_parent(self):
        return self.parent
    
    def set_intree(self):
        self.intree = True

    def set_distance(self, dist):
        self.distance = dist

    def set_unvisited(self):
        self.color = WHITE

    def set_discovered(self):
        self.color = DARK_BLUE

    def set_parent(self, parent):
        self.parent = parent

    def set_processed(self):
        self.color = BLUE

    def set_shortest(self):
        self.color = YELLOW

    def is_intree(self):
        return self.intree == True

    def is_start(self) -> bool:
        return self.color == PURPLE

    def is_target(self) -> bool:
        return self.color == DARK_PURPLE

    def is_wall(self) -> bool:
        return self.color == BLACK

    def is_discovered(self) -> bool:
        return self.color == DARK_BLUE or self.color == BLUE



    
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
    