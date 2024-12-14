import pytest

from d1 import compute_list_distance, compute_similarity_score
from d2 import is_safe, dampen


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
def test_day_02_part_02(report, expected):
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
def test_day_02_part_01(report, expected):
    # arrange
    # act
    # assert
    assert dampen(report) == expected