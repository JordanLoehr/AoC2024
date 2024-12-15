# https://adventofcode.com/2024/day/5
# ------ Advent Of Code 2024 -------
# ------- Day 5: Print Queue -------

from common.loaders import load_lines
from collections import defaultdict

def build_rule_index(rules: list[str]) -> dict:
    rule_index = defaultdict(list)
    for rule in rules:
        a,b = rule.split('|')
        rule_index[int(a)].append(int(b))

    return rule_index



def parse_input(lines: list) -> tuple:
    # parse input lines into a list of rules and a list of records, there is a '' that splits them
    split_index = lines.index('')

    rules = lines[:split_index]
    updates = lines[split_index+1:]

    int_updates = [[int(x) for x in update.split(',')] for update in updates]
    dict_rules = build_rule_index(rules)

    return (dict_rules, int_updates)

def is_update_valid(update: list[int], rules: dict) -> bool:
    # for each page in the record, check if its allowed to be before the remaining pages
    # this includes checking that the remaining pages are in the rule for the current page
    # as well as the current mage is not in the rules for any of the remaining pages
    for i, page in enumerate(update):
        rule_list = rules[page]
        remaining = update[i+1:]
        r_status = []
        for r in remaining:
            if r in rule_list:
                r_status.append(True) # rule explicitly allows this so can short circuit out any additonal checks
                continue 
            if page in rules[r]:
                # if current page is in a rule for a remaining page then its an obvious fail
                r_status.append(False)

        if all(r_status):
            # if this page passed all the rules then continue to check the next one
            continue
        else:
            # otherwise fail
            return False
    
    # if none of the rules failed then the update is valid
    return True
        

def filter_valid_updates(rules: dict, updates: list[list[int]]) -> list:
    valid_updates = [update for update in updates if is_update_valid(update, rules)]
    return valid_updates

def filter_invalid_updates(rules: dict, updates: list[list[int]]) -> list:
    invalid_updates = [update for update in updates if not is_update_valid(update, rules)]
    return invalid_updates

def reorder_invalid_updates(rules: dict, updates: list[list[int]]) -> list:
    return updates

def middle_sum(updates: list[list[int]]) -> int:
    middles = [update[len(update)//2] for update in updates]
    return sum(middles)

def part_one(filename):
    lines = load_lines(filename)
    rules, updates = parse_input(lines)
    valid_updates = filter_valid_updates(rules, updates)
    result = middle_sum(valid_updates)
    return result

def part_two(filename):
    lines = load_lines(filename)
    rules, updates = parse_input(lines)
    invalid_updates = filter_invalid_updates(rules, updates)
    reordered_updates = reorder_invalid_updates(rules, invalid_updates)
    result = middle_sum(reordered_updates)
    return result

if __name__ == "__main__":
    print("Day 5: Part One".center(40, "-"))
    answer = part_one("inputs/d5.txt")  # newlines removed before hand
    print(answer)
    print("Day 5: Part Two".center(40, "-"))
    answer = part_two("inputs/d5.txt")  # newlines removed before hand
    print(answer)
