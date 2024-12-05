# https://adventofcode.com/2024/day/1
# ------ Advent Of Code 2024 ------
# --- Day 1: Historian Hysteria ---

from common.loaders import columnar_lists_tab_delim

def compute_list_distance(left_list: list, right_list: list) -> int:
    left_list.sort()
    right_list.sort()

    distances = []

    for i in range(len(left_list)):
        distances.append(abs(int(left_list[i]) - int(right_list[i])))

    return sum(distances)

def compute_similarity_score(left_list: list, right_list: list) -> int:
    counts = []
    for i in left_list:
        counts.append(int(i) * right_list.count(i))
    
    return sum(counts)

def part_one(input_path: str) -> int:
    left_list, right_list = columnar_lists_tab_delim(input_path)
    distance = compute_list_distance(left_list, right_list)
    return distance

def part_two(input_path: str) -> int:
    left_list, right_list = columnar_lists_tab_delim(input_path)
    score = compute_similarity_score(left_list, right_list)
    return score

if __name__ == "__main__":
    print('Day 1: Part One'.center(40,'-'))
    answer = part_one('inputs/d1.txt')
    print(answer)
    print('Day 1: Part Two'.center(40,'-'))
    answer = part_two('inputs/d1.txt')
    print(answer)