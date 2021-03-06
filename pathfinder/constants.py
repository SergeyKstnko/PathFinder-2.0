

WIDTH, HEIGHT = 1020, 763 #963
HEADER_HEIGHT = 120
TILE_SIZE = 25
INDENT = 10
BOTTOM_INDENT = 118

CANVAS_XY = (INDENT, HEADER_HEIGHT)
CANVAS_WIDTH = WIDTH - INDENT*2
CANVAS_HEIGHT = HEIGHT - HEADER_HEIGHT - BOTTOM_INDENT
ROWS = CANVAS_HEIGHT // TILE_SIZE
COLS = CANVAS_WIDTH // TILE_SIZE


WHITE = (255,255,255)
BLACK = (0,0,0)
SKYBLUE = (135,206,235)     #GRID COLOR

DARK_BLUE = (0, 217, 159)   #DISCOVERED TILES
BLUE = (0, 190, 218)           #PROCESSED TILES


#DARK_BLUE = (0, 190, 218)   #DISCOVERED TILES
#BLUE = (75,0,135)           #PROCESSED TILES

YELLOW = (255, 254, 106)    #PATH
PURPLE = (148,0,211)        #START TILE
DARK_PURPLE = (75,0,130)    #END TILE

HEADER = (53, 74, 95)       #HEADER COLOR
PROMPT_CORAL = (255,127,80)        #HEADER PROMPT
