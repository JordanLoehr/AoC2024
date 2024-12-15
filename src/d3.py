import re

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
        
if __name__ == "__main__":
    print('Day 3: Part One'.center(40,'-'))
    answer = part_one('inputs/d3.txt') # newlines removed before hand
    print(answer)
    # print('Day 2: Part Two'.center(40,'-'))
    # answer = part_two('inputs/d2.txt')
    # print(answer)