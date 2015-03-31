"""
Merge function for 2048 game.
"""

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

print merge([4])