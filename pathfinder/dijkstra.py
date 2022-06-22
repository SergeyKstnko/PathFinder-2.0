'''
This class implements Dijkstra algorithm

'''

class Dijkstra:
    def __init__(self, canvas):
        self.object = None
        self.canvas = None
        self.start = None
        self.target = None

    def find_smallest_distance(self):
        shortest = self.start
        for row in self.canvas:
            for tile in row:
                if shortest.get_distance() > tile.get_distance() and not tile.is_intree():
                    shortest = tile
        
        return shortest

    def run(self, game_window, canvas):
        self.object = canvas
        self.canvas = canvas.get_canvas()
        self.start = canvas.get_start()
        self.target = canvas.get_target()

        #set start distance to 0
        self.start.set_distance(0)
        #set v-node to start
        v = self.start

        while(v != self.target):
            v.set_intree()

            neighbours = v.get_neighbours()
            for n in neighbours:
                if n.is_start() or n.is_wall():
                    continue

                weight = n.get_weight()
                if n.get_distance() > (n.get_distance() + weight):
                    n.set_distance(n.get_distance() + weight)
                    n.set_parent(v)
            
            v.set_processed()
            v = self.find_smallest_distance()
            
            self.object.draw_canvas(game_window)

        #check if neighbour is a wall or a start but probably do not check if it is a target?
        pass