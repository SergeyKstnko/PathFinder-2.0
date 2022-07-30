'''
bfs.py implements Breadth-First Search Algorithm
'''

from re import L
from .FormalAlgorithmInterface import FormalAlgorithmInterface
from collections import deque
from .constants import COLS, ROWS
import pygame

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


    def add_neighbours(self, curr):
        coord = [[1,0], [-1.0],[0,1],[0,-1]]

        for row_c, col_c in coord:
            row, col = curr.get_row_col()
            new_row, new_col = row+row_c, col+col_c
            if new_row in range(ROWS) and new_col in range(COLS) and not curr.is_wall():
                neigh = self.grid[new_row][new_col]
                neigh.set_parent=curr

                if not curr.is_target():
                    curr.set_discovered()
                q.append(neigh)


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