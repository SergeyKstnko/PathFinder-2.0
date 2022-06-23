'''
This class implements Dijkstra algorithm

'''
import math
from .FormalAlgorithmInterface import FormalAlgorithmInterface

class Dijkstra(FormalAlgorithmInterface):
    def __init__(self):
        self.object = None
        self.canvas = None
        self.start = None
        self.target = None
        self.alg_prompt = "Dijkstra Weighted Algorithm, guarantees shortest path" + " "

    def find_smallest_distance(self):
        dist = math.inf
        shortest = self.canvas[0][0]
        for row in self.canvas:
            for tile in row:
                if dist > tile.get_distance() and not tile.is_intree():
                    dist = tile.get_distance()
                    shortest = tile
        
        return shortest

    def get_alg_prompt(self):
        return self.alg_prompt

    def run(self, game_window, canvas):
        self.object = canvas
        self.canvas = canvas.get_canvas()
        self.start = canvas.get_start()
        self.target = canvas.get_target()

        #set start distance to 0
        self.start.set_distance(0)
        #set v-node to start
        v = self.start

        
        while v != self.target:
            v.set_intree()

            neighbours = v.get_neighbours()
            
            for n in neighbours:

                weight = n.get_weight()
                if n.get_distance() > (v.get_distance() + weight):
                    n.set_distance(v.get_distance() + weight)
                    n.set_parent(v)
                    n.set_discovered()
            
            v.set_processed()
            v = self.find_smallest_distance()
            
            self.object.draw_canvas(game_window)
