"""
Clone of 2048 game.
"""

# import user39_Q304aD4fSn_6  as testsuite


import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    
    numbers_slid_not_merged = [0 for dummy_index in line]
    
    dummy_index = 0
  
    for number in line:
        if number != 0:
            numbers_slid_not_merged[dummy_index] = number
            dummy_index += 1
    
      
    return_list = []
    
    last_merge = False
    
    for dummy_index in range(len(numbers_slid_not_merged)):
        if last_merge == False:
            if dummy_index == len(numbers_slid_not_merged)-1:
                return_list.append(numbers_slid_not_merged[dummy_index])
                #print "FALSE not merging, but appending", i  
                
            elif numbers_slid_not_merged[dummy_index] == numbers_slid_not_merged[dummy_index+1]:
                return_list.append(numbers_slid_not_merged[dummy_index] * 2)
                #print "FALSE merging", i
                return_list.append(0)
                last_merge = True
            else:
                return_list.append(numbers_slid_not_merged[dummy_index])
                #print "FALSE not merging, but appending", i
                
        else:
            last_merge = False
            #print "TRUE not merging", i
    
    # consolidate into a separate function later (repeats above)
    final_list = [0 for dummy_index in return_list]
    
    dummy_index2 = 0
    for number in return_list:
        if number != 0:
            final_list[dummy_index2] = number
            dummy_index2 += 1
    
    
    return final_list

def traverse_grid(start_cell, direction, num_steps):
    
    tiles = []
    
    for step in range(num_steps):
        row = start_cell[0] + step * direction[0]
        col = start_cell[1] + step * direction[1]
        tiles.append((row, col))
  
    return tiles
        
class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.width = grid_width
        self.height = grid_height
        self.grid = [[0 for col in range(self.width)] for row in range(self.height)]
        self.reset()
             
        left_col = traverse_grid((0,0), OFFSETS[UP], self.height)
        right_col = traverse_grid((0,self.width - 1), OFFSETS[UP], self.height)
        
        top_row = traverse_grid((0,0), OFFSETS[LEFT], self.width)
        bottom_row = traverse_grid((self.height - 1,0), OFFSETS[LEFT], self.width)

        self.initial_tiles = {UP: top_row,
                   DOWN: bottom_row,
                   LEFT: left_col,
                   RIGHT: right_col}
        
        print self.initial_tiles
        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for col in range(self.width)] for row in range(self.height)]
        self.new_tile()
        self.new_tile()
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        for tile in self.initial_tiles[1]:
            print "initial_tiles[1]", tile
            
        for tile in self.initial_tiles[2]:
            print "initial_tiles[2]", tile
            
        return "THE GRID: " + str(self.grid) + "\n " + str(self.initial_tiles)

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
   
        initial_tiles = self.initial_tiles[direction]
        
        
        merge_lists = []
        
        print "==="
        print direction

        tiles_changed = False       
        
        for initial_tile in initial_tiles:
            
            if direction == 1 or direction == 2:
                squares_to_merge = traverse_grid(initial_tile, OFFSETS[direction], self.height)
                merge_list = []
                for square in squares_to_merge:
                    merge_list.append(self.grid[square[0]][square[1]])
                    print "merge_list", merge_list
                merged_list = merge(merge_list)
                
                i = 0
                for value in merged_list:
                   
                    self.set_tile(squares_to_merge[i][0], squares_to_merge[i][1], value)
                    i += 1
                    
                    
                if merged_list != merge_list:
                    tiles_changed = True
                    
                    
                print "merged list: ", merged_list

            #  def set_tile(self, row, col, value):
                    
            else:
                squares_to_merge = traverse_grid(initial_tile, OFFSETS[direction], self.width) 
                merge_list = []
                for square in squares_to_merge:
                    merge_list.append(self.grid[square[0]][square[1]])
                    print "merge_list", merge_list
                merged_list = merge(merge_list)
                print "merged list: ", merged_list
        
                i = 0
                for value in merged_list:
                   
                    self.set_tile(squares_to_merge[i][0], squares_to_merge[i][1], value)
                    i += 1        
        
                    
                if merged_list != merge_list:
                    tiles_changed = True

            print "initial_tile", initial_tile

        if tiles_changed == True:
            self.new_tile()          

        
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        spawn_tile = [2,2,2,2,2,2,2,2,2,4]
        new_tile = random.choice(spawn_tile)
        
        random_row = random.randrange(0, self.height)
        random_col = random.randrange(0, self.width)
        
        while self.grid[random_row][random_col] != 0:
            random_row = random.randrange(0, self.height)
            random_col = random.randrange(0, self.width)
        
        self.grid[random_row][random_col] = new_tile
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        
        return self.grid[row][col]


test = TwentyFortyEight(4,4)
poc_2048_gui.run_gui(test)


print test

# testsuite.run_suite(TwentyFortyEight)


