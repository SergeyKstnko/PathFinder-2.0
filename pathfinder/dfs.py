'''
dfs.py implements Depth Search Algorithm

@TODO:

'''

from .constants import COLS, ROWS

class Dfs:
    def __init__(self):
        self.object = None
        self.canvas = None
        self.start = None
        self.target = None
        self.found = False

    def dfs(self, row, col, parent, game_window):
        #if node is outside bounaries or if node is a wall
        if row < 0 or row >= ROWS or col < 0 or col >= COLS or self.found:
            return
        curr = self.canvas[row][col]
        if curr.is_discovered() or curr.is_wall():
            return

        curr.set_parent(parent)
        if curr.is_target():
            self.found = True
            return

        if not curr.is_start():
            curr.set_discovered()

        self.object.draw_canvas(game_window)
        #recurse into every neighbour of the node

        self.dfs(row-1, col, curr, game_window) #UPPER
        self.dfs(row, col-1, curr, game_window) #LEFT
        self.dfs(row, col+1, curr, game_window) #RIGHT
        self.dfs(row+1, col, curr, game_window) #DOWN
        
        #mark current node as processed
        if not curr.is_start():
            curr.set_processed()
        self.object.draw_canvas(game_window)

    def run(self, game_window, canvas):
        self.object = canvas
        self.canvas = canvas.get_canvas()
        self.start = canvas.get_start()
        self.target = canvas.get_target()
        self.found = False

        row, col = self.start.get_row_col()
        self.dfs(row, col, None, game_window)