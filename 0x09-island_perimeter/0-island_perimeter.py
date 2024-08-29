#!/usr/bin/python3
def island_perimeter(grid):
    # Initialize the perimeter counter
    perimeter = 0

    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Traverse each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Check if the current cell is land (1)
            if grid[r][c] == 1:
                # Initially add 4 to the perimeter for each land cell
                perimeter += 4

                # Check for adjacent land cells and subtract the shared edges

                # If there is a land cell above the current cell
                if r > 0 and grid[r-1][c] == 1:
                    # Subtract 2 from the perimeter (one shared edge)
                    perimeter -= 2

                # If there is a land cell to the left of the current cell
                if c > 0 and grid[r][c-1] == 1:
                    # Subtract 2 from the perimeter (one shared edge)
                    perimeter -= 2

    # Return the total perimeter of the island
    return perimeter
