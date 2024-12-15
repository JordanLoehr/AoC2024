# https://adventofcode.com/2024/day/4
# ------ Advent Of Code 2024 ------
# --- Day 4: Ceres Search ---

# possible directions in [y,x], there is 8 of them, (1,1) is down and right, (-1,-1) is up and left
DIRECTIONS = [
    (0,1),   # E
    (1,1),   # SE
    (1,0),   # S
    (1,-1),  # SW
    (0,-1),  # W
    (-1,-1), # NW
    (-1,0),  # N
    (-1,1),  # NE
]

SEARCH_WORD = "XMAS"

def is_valid_coord(search_grid: list, coords: tuple[int,int]) -> bool:
    y, x = coords
    if x >= 0 and x < len(search_grid[0]) and y >= 0 and y < len(search_grid):
        return True
    else:
        return False

def parse_search_grid(lines: list[str]) -> list:
    search_grid = [list(line) for line in lines]
    return search_grid

def load(filename) -> list[str]:
    with open(filename, "r") as file:
        lines = file.readlines()

    return lines

def sub_search(search_grid: list, x_coords: tuple[int,int]) -> int:
    sub_search_count = 0
    for direction in DIRECTIONS:
        y, x = x_coords
        buffer = SEARCH_WORD[0]
        for char in SEARCH_WORD[1:]:
            dir_y, dir_x = direction
            y += dir_y
            x += dir_x
            if is_valid_coord(search_grid, (y,x)):
                if search_grid[y][x] == char:
                    buffer += char
                else:
                    break
            else:
                break
        if buffer == SEARCH_WORD:
            sub_search_count += 1
    return sub_search_count

def search(search_grid) -> int:
    # loop through every character in each row
    # if the character is an X, iterate through the 
    # cardinal directions, check if that coordinate it makes it valid
    # then check if that letter is M, if it is continue in that direction
    # if it finds all 3 leters increment the found count
    # iterate through all directions, then continue looking for the next X

    search_count = 0

    for y, row in enumerate(search_grid):
        for x, col in enumerate(row):
            if col == SEARCH_WORD[0]:
                found = sub_search(search_grid, (y,x))
                search_count += found

    return search_count

def part_one(filename):
    lines = load(filename)
    search_grid = parse_search_grid(lines)
    result = search(search_grid)
    return result

if __name__ == "__main__":
    print('Day 4: Part One'.center(40,'-'))
    answer = part_one('inputs/d4.txt') # newlines removed before hand
    print(answer)
    # print('Day 4: Part Two'.center(40,'-'))
    # answer = part_two('inputs/d3.txt')
    # print(answer)