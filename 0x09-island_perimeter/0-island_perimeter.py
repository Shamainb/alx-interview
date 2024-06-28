#!/usr/bin/python3
def island_perimeter(grid):
    # Initialize the perimeter
    perimeter = 0
    
    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Check if the cell is land
            if grid[r][c] == 1:
                # Check the four neighbors
                # Check the top neighbor
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                # Check the bottom neighbor
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                # Check the left neighbor
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                # Check the right neighbor
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1
    
    return perimeter
