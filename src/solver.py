#---------------------------- TASK 1 ----------------------------
def count_neighbors(grid, row, col):
    """
    Counts the number of alive neighbors for a specific cell in the grid.
    A cell can have up to 8 neighbors (horizontal, vertical, and diagonal).
    
    Args:
        grid (list of lists): The current 2D state of the game.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        
    Returns:
        int: The total number of alive neighbors (0 to 8).
    """
    
    alive_count = 0
    rows = len(grid)
    cols = len(grid[0])
    
    # TODO: Implement your neighbor-counting logic here!
    for dr in range (-1,2):           #Helps in iterating through the row number of each neighbour.
        for dc in range (-1,2):       #Helps in iterating through the column number of each neighbour.
            neighbouring_row = row + dr
            neighbouring_col = col + dc
            if rows>neighbouring_row>=0 and cols>neighbouring_col>=0:     #Checks if the row actually exists / is not off the grid
                if dr==0 and dc==0:       #Excludes the specific cell
                    continue
                else:
                    alive_count += grid[neighbouring_row][neighbouring_col]
    return alive_count

#---------------------------- TASK 2 ----------------------------
def compute_next_generation(grid):
    """
    Generates the next state of the grid based on Conway's rules.
    
    Args:
        grid (list of lists): The current 2D state of the game.
        
    Returns:
        list of lists: A BRAND NEW 2D grid representing the next generation.
        
    Note:
        - Do NOT modify the original `grid` directly while iterating through it. 
          You must create a new grid to store the updated states, otherwise 
          your changes will mess up the neighbor counts for subsequent cells!
    """
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)]                # Creates a new blank grid of the same size, filled with 0s
    
    # TODO: Iterate through every cell in the `grid`.
    for row in range(0,rows):
            for col in range(0,cols):


                # TODO: Use your `count_neighbors` function to find out how many neighbors it has.
                num_neighbours = count_neighbors(grid,row,col)


                # TODO: Apply the 4 Rules of Life to determine if it should be 1 (alive) or 0 (dead) in `next_grid`.
                if grid[row][col] == 1:                                  # 2. Survival: Any live cell with two or three live neighbors lives on to the next generation.
                    if num_neighbours == 2 or num_neighbours == 3:       
                           next_grid[row][col] = 1
                    elif num_neighbours >= 3:                            # 3. Overpopulation: Any live cell with more than three live neighbors dies.
                         next_grid[row][col] = 0
                    elif num_neighbours <= 2:                            # 1. Underpopulation: Any live cell with fewer than two live neighbors dies.
                         next_grid[row][col] = 0                         
                elif grid[row][col] == 0:                                # 4. Reproduction: Any dead cell with exactly three live neighbors becomes a live cell.
                         if num_neighbours == 3:
                              next_grid[row][col] = 1
    return next_grid