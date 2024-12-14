from common.loaders import list_per_line

def is_safe(report: list) -> bool:
    # The levels are either all increasing or all decreasing.
    safe_direction = len(set(['asc' if f < s else 'desc' for f,s in zip(report, report[1:])])) == 1

    # Any two adjacent levels differ by at least one and at most three.
    safe_values = all([(abs(f-s) >= 1 and abs(f-s) <=3) for f,s in zip(report, report[1:])])

    return all((safe_direction, safe_values))

def dampen(report: list) -> bool:
    if not is_safe(report):
        # try dampening
        for i in range(len(report)):
            dampened_report = report[:i] + report[(i+1):]
            if is_safe(dampened_report):
                return True
        return False
    else:
        return True


def part_one(input: str) -> int:
    reports = list_per_line(input)

    results = [is_safe(report) for report in reports]

    return results.count(True)

def part_two(input: str) -> int:
    reports = list_per_line(input)

    results = [dampen(report) for report in reports]

    return results.count(True)

if __name__ == "__main__":
    print('Day 2: Part One'.center(40,'-'))
    answer = part_one('inputs/d2.txt')
    print(answer)
    print('Day 2: Part Two'.center(40,'-'))
    answer = part_two('inputs/d2.txt')
    print(answer)