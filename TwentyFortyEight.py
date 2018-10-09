"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    line_len_counter = 0
    result_list = []
    pos = 0
    changed = False
    
    while line_len_counter < len(line):
        result_list.append(0)
        line_len_counter += 1
                
    for tile in line:
        if tile != 0:
            result_list[pos] = tile
            if pos >= 1 and result_list[pos] == result_list[pos - 1] and not changed:
                result_list[pos - 1] = result_list[pos] * 2
                result_list[pos] = 0
                changed = True
                
            else:
                pos += 1
                changed = False
            
    return result_list

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.height = grid_height
        self.width = grid_width
        self.initial_board = []
        self.reset()
        
        initial_up = []
        initial_down = []
        initial_right = []
        initial_left = []
        
        for row in range(self.height):
            initial_up.append((0, row))
            initial_down.append(((self.height - 1), row))
        
        for col in range(self.width):
            initial_left.append((col, 0))
            initial_right.append((col, self.width - 1))
        
        self.indicies_dict = {UP: initial_up, 
                              DOWN: initial_down,
                              LEFT: initial_left,
                              RIGHT: initial_right}
        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.initial_board = [[0 for col in range(self.width)]
                           for row in range(self.height)]
        
        self.new_tile()
        self.new_tile()

        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """

        for row in range(self.height):
            print str(self.initial_board[row])
          
        return "Board is above"

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        temp_list = []
        changed = False
        initial_tiles = self.indicies_dict[direction]
        move = OFFSETS[direction]
        num_steps = len(initial_tiles)
        
        if direction == UP or direction == DOWN:
            num_lines = self.width
            
        elif direction == LEFT or direction == RIGHT:
            num_lines = self.height
            
        
        for line in range(num_lines):
            
            for step in range(num_steps):
                row = initial_tiles[0][0] + line * move[1] + step * move[0]
                col = initial_tiles[0][1] + line * move[0] + step * move[1]
                temp_list.append(self.initial_board[row][col])
            
            temp_list = merge(temp_list)

            for step in range(num_steps):
                row = initial_tiles[0][0] + line * move[1] + step * move[0]
                col = initial_tiles[0][1] + line * move[0] + step * move[1]
                if self.initial_board[row][col] != temp_list[step]:
                    changed = True
                    
                self.initial_board[row][col] = temp_list[step]

            temp_list = []
            
        if changed == True:
            self.new_tile()
            changed = False
            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        tile_randomizer = random.randrange(0, 10)
        if tile_randomizer == 1:
            new_tile = 4
        else:
            new_tile = 2
            
        new_tile_row = random.randrange(0, self.height)
        new_tile_column = random.randrange(0, self.width)
        
        if self.initial_board[new_tile_row][new_tile_column] == 0:
            self.initial_board[new_tile_row][new_tile_column] = new_tile
            
        else:
            self.new_tile()
        

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.initial_board[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.initial_board[row][col]

board = TwentyFortyEight(4, 4)
poc_2048_gui.run_gui(board)

print board

print board.indicies_dict


initial_tiles = board.indicies_dict[3]
print len(initial_tiles)
print board.indicies_dict[1][1][0]
