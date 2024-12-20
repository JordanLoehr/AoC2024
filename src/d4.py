# https://adventofcode.com/2024/day/4
# ------ Advent Of Code 2024 ------
# --- Day 4: Ceres Search ---

from common.loaders import load_lines

# possible directions in [y,x], there is 8 of them, (1,1) is down and right, (-1,-1) is up and left
DIRECTIONS = [
    (0, 1),  # E
    (1, 1),  # SE
    (1, 0),  # S
    (1, -1),  # SW
    (0, -1),  # W
    (-1, -1),  # NW
    (-1, 0),  # N
    (-1, 1),  # NE
]

SEARCH_WORD = "XMAS"


def is_valid_coord(search_grid: list, coords: tuple[int, int]) -> bool:
    y, x = coords
    if x >= 0 and x < len(search_grid[0]) and y >= 0 and y < len(search_grid):
        return True
    else:
        return False


def parse_search_grid(lines: list[str]) -> list:
    search_grid = [list(line) for line in lines]
    return search_grid


def sub_search(search_grid: list, x_coords: tuple[int, int]) -> int:
    sub_search_count = 0
    for direction in DIRECTIONS:
        y, x = x_coords
        buffer = SEARCH_WORD[0]
        for char in SEARCH_WORD[1:]:
            dir_y, dir_x = direction
            y += dir_y
            x += dir_x
            if is_valid_coord(search_grid, (y, x)):
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
                found = sub_search(search_grid, (y, x))
                search_count += found

    return search_count


def sub_search_p2(search_grid: list, a_coords: tuple[int, int]) -> bool:
    cross_coords = [(-1, -1), (1, 1), (1, -1), (-1, 1)]

    cross_chars = []

    for coord in cross_coords:
        y, x = a_coords
        dir_y, dir_x = coord
        y += dir_y
        x += dir_x

        if is_valid_coord(search_grid, (y, x)):
            cross_chars += search_grid[y][x]
        else:
            # if any directions are not valid there is no way there is a valid cross
            return False

    if (
        (cross_chars[0] == "M" and cross_chars[1] == "S")
        or (cross_chars[0] == "S" and cross_chars[1] == "M")
    ) and (
        (cross_chars[2] == "M" and cross_chars[3] == "S")
        or (cross_chars[2] == "S" and cross_chars[3] == "M")
    ):
        return True

    return False


def search_p2(search_grid: list) -> int:
    # similar to search, loop through every character in each row
    # if the character is an X, iterate through the NE/NW/SW/SE directions
    # look for a cross of MAS, if two MAS exist then it can be considered an X-MAS
    search_count = 0

    for y, row in enumerate(search_grid):
        for x, col in enumerate(row):
            if col == "A":
                if sub_search_p2(search_grid, (y, x)):
                    search_count += 1

    return search_count


def part_one(filename):
    lines = load_lines(filename)
    search_grid = parse_search_grid(lines)
    result = search(search_grid)
    return result


def part_two(filename):
    lines = load_lines(filename)
    search_grid = parse_search_grid(lines)
    result = search_p2(search_grid)
    return result


if __name__ == "__main__":
    print("Day 4: Part One".center(40, "-"))
    answer = part_one("inputs/d4.txt")  # newlines removed before hand
    print(answer)
    print("Day 4: Part Two".center(40, "-"))
    answer = part_two("inputs/d4.txt")
    print(answer)
