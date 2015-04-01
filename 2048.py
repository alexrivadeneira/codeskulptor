"""
Clone of 2048 game.
"""

import poc_2048_gui

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

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        pass

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        pass

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return ""

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return 0

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return 0

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        pass

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return 0


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

