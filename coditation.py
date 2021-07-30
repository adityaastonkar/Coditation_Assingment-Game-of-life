# importing packages required
import numpy as np
def Game_of_life(grid):
    # checking the neighbours creating Array
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    # accessing every index of the matrix
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # counter to check number of neighbouors alive
            count=0
            for k in direction:
                # checking the values index error
                if i+k[0]>=0 and j+k[1]>=0 and i+k[0]<len(grid) and j+k[1]<len(grid[0]):
                    # checking the neighbour cells
                    if grid[i+k[0]][j+k[1]]==1:
                        # increasing counter
                        count+=1
            # checking given 4 conditions
            if grid[i][j] == 1:
                if count < 2 or count > 3:
                    grid[i][j] = 0
            elif count == 3:
                grid[i][j]=1
    # returning new grid to the result
    return grid

grid=np.zeros((25,25))
Game_of_life(grid)