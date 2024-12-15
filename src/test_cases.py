import pytest

from d1 import compute_list_distance, compute_similarity_score
from d2 import is_safe, dampen
from d3 import parse_memory, execute, purge_disabled
from d4 import search


def test_day_01_part_01():
    # arrange
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9, 3]

    # act
    result = compute_list_distance(left_list, right_list)

    # assert
    assert result == 11


def test_day_01_part_02():
    # arrange
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9, 3]

    # act
    result = compute_similarity_score(left_list, right_list)

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
    assert is_safe(report) == expected

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
    assert dampen(report) == expected

def test_day_03_part_01():
    # arrange
    memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    # act
    instructions = parse_memory(memory)
    result = execute(instructions)

    # assert
    assert result == 161

def test_day_03_part_02():
    # arrange
    memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    # act
    purged_memory = purge_disabled(memory)
    instructions = parse_memory(purged_memory)
    result = execute(instructions)
    
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
    result = search(search_grid)

    # assert
    assert result == 18

