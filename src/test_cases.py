from d1 import compute_list_distance, compute_similarity_score


def test_day_01_part_01():
    # arrange
    left_list = [3,4,2,1,3,3]
    right_list = [4,3,5,3,9,3]

    # act
    result = compute_list_distance(left_list, right_list)

    # assert
    assert result == 11

def test_day_01_part_02():
    # arrange
    left_list = [3,4,2,1,3,3]
    right_list = [4,3,5,3,9,3]

    # act
    result = compute_similarity_score(left_list, right_list)

    # assert
    assert result == 31