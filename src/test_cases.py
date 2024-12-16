import pytest

import d1, d2, d3, d4, d5, d6


def test_day_01_part_01():
    # arrange
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9, 3]

    # act
    result = d1.compute_list_distance(left_list, right_list)

    # assert
    assert result == 11


def test_day_01_part_02():
    # arrange
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9, 3]

    # act
    result = d1.compute_similarity_score(left_list, right_list)

    # assert
    assert result == 31


@pytest.mark.parametrize(
    "report,expected",
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], False),
        ([8, 6, 4, 4, 1], False),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_day_02_part_01(report, expected):
    # arrange
    # act
    # assert
    assert d2.is_safe(report) == expected

@pytest.mark.parametrize(
    "report,expected",
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], True),
        ([8, 6, 4, 4, 1], True),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_day_02_part_02(report, expected):
    # arrange
    # act
    # assert
    assert d2.dampen(report) == expected

def test_day_03_part_01():
    # arrange
    memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    # act
    instructions = d3.parse_memory(memory)
    result = d3.execute(instructions)

    # assert
    assert result == 161

def test_day_03_part_02():
    # arrange
    memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    # act
    purged_memory = d3.purge_disabled(memory)
    instructions = d3.parse_memory(purged_memory)
    result = d3.execute(instructions)
    
    # assert
    assert result == 48

def test_day_04_part_01():
    # arrange
    a = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    search_grid = [list(row) for row in a.split()]

    # act
    result = d4.search(search_grid)

    # assert
    assert result == 18

def test_day_04_part_02():
    # arrange
    a = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    search_grid = [list(row) for row in a.split()]

    # act
    result = d4.search_p2(search_grid)

    # assert
    assert result == 9

def test_day_05_part_01():
    # arrange
    a = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

    lines = a.split('\n')
    rules, updates = d5.parse_input(lines)

    # act
    valid_updates = d5.filter_valid_updates(rules, updates)
    middle_sum = d5.middle_sum(valid_updates)

    # assert

    assert middle_sum == 143

def test_day_05_part_02():
    # arrange
    a = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

    lines = a.split('\n')
    rules, updates = d5.parse_input(lines)

    # act
    invalid_updates = d5.filter_invalid_updates(rules, updates)
    print(invalid_updates)
    d5.sort_invalid_updates(rules, invalid_updates)
    print(invalid_updates)
    middle_sum = d5.middle_sum(invalid_updates)

    # assert

    assert middle_sum == 123

def test_day_06_part_01():
    # arrange
    grid_raw = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

    grid = [list(col) for col in grid_raw.split("\n")]
    print(grid)

    # act
    d6.walk_path(grid)
    print(grid)
    coord_count = d6.count_coords(grid)


    # assert

    assert coord_count == 41

    