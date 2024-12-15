import re

def purge_disabled(memory: str) -> str:
    # remove sections of corrupted memory between don't() and do()
    purged_memory = re.sub(r"don't\(\).+?do\(\)", "", memory)
    return purged_memory

def parse_memory(memory: str) -> list[str]:
    # takes corrupted memory and returns list of valid instructions
    instructions = re.findall(r"mul\(\d+,\d+\)", memory)
    return instructions

def execute(instructions: list[str]):
    results = []
    for instruction in instructions:
        #mul(<int>,<int>) can drop mul( and )
        operands = instruction[4:-1].split(',')
        result = int(operands[0]) * int(operands[1])
        results.append(result)

    return sum(results)

def part_one(filename):
    with open(filename, 'r') as file:
        memory = file.readline()
        instructions = parse_memory(memory)
        result = execute(instructions)
    return result

def part_two(filename):
    with open(filename, 'r') as file:
        memory = file.readline()
        purged_memory = purge_disabled(memory)
        instructions = parse_memory(purged_memory)
        result = execute(instructions)
    return result
        
if __name__ == "__main__":
    print('Day 3: Part One'.center(40,'-'))
    answer = part_one('inputs/d3.txt') # newlines removed before hand
    print(answer)
    print('Day 3: Part Two'.center(40,'-'))
    answer = part_two('inputs/d3.txt')
    print(answer)