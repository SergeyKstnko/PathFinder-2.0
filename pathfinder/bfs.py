'''
bfs.py implements Breadth-First Search Algorithm
'''

from .FormalAlgorithmInterface import FormalAlgorithmInterface
from collections import deque

class Bfs(FormalAlgorithmInterface):
    def __init__(self):
        self.graph = None
        self.grid = None
        self.start = None
        self.target = None
        self.found = False
        self.alg_prompt = "Breadth-First Search Algorithm, unweighted and guarantees the shortest path" + "  "
        

    def get_alg_prompt(self):
        return self.alg_prompt

    def bfs(self, row, col, game_window):
        q = deque()
        q.append(self.grid[row][col])

        while q and not self.found:

            curr = q.popleft()
            if curr.is_target():
                self.found = True
                return

            for neighbour in curr.get_neighbours():
                if neighbour.is_wall() or neighbour.is_discovered():
                    continue
                neighbour.set_parent(curr)
                q.append(neighbour)
                if not neighbour.is_start():
                    neighbour.set_discovered()

            if not curr.is_start():
                curr.set_processed()

            self.object.draw_canvas(game_window)
            


    def run(self, game_window, graph):
        self.object = graph
        self.grid = graph.get_canvas()
        self.start = graph.get_start()
        self.target = graph.get_target()
        self.found = False

        row, col = self.start.get_row_col()
        self.bfs(row, col, game_window)