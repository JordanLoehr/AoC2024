# https://adventofcode.com/2024/day/6
# ------ Advent Of Code 2024 -------
# ----- Day 6: Guard Gallivant -----

def load_grid(filename: str) -> list:
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        grid = [list(line) for line in lines]

    return grid

def find_start(grid: list) -> tuple:
    start_coords = (0,0)
    for i, row in enumerate(grid):
        if '^' in row:
            start_coords = (row.index('^'), i)
    return start_coords
  

def walk_path(grid: list):
    curr_loc = find_start(grid)
    direction = (0,-1)
    in_grid = True
    while in_grid:
        grid[curr_loc[1]][curr_loc[0]] = "X"
        next_x, next_y= tuple(sum(x) for x in zip(curr_loc, direction))

        # is outside bounds?
        if next_y < 0 or next_y > (len(grid)-1) or next_x < 0 or next_x > (len(grid[0])-1):
            in_grid = False
            break
        
        # is it an obstacle?
        if grid[next_y][next_x] == "#":
            # turn
            direction = (-direction[1], direction[0])
            continue

        curr_loc = (next_x, next_y)


def count_coords(grid: list) -> int:
    count = 0
    for row in grid:
        for col in row:
            if col == "X":
                count +=1

    return count

def part_one(filename):
    grid = load_grid(filename)
    walk_path(grid)
    coord_count = count_coords(grid)
    return coord_count

if __name__ == "__main__":
    print("Day 6: Part One".center(40, "-"))
    answer = part_one("inputs/d6.txt")  # newlines removed before hand
    print(answer)