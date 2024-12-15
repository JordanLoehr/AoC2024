# Various file loaders for AoC inputs

def columnar_lists_tab_delim(filename: str) -> tuple[list, list]:
    list_a = []
    list_b = []
    with open(filename, "r") as file:
        for line in file:
            a,b = line.split()
            list_a.append(a)
            list_b.append(b)

    return (list_a, list_b)

def list_per_line(filename: str) -> list[list[int]]:
    results = []
    with open(filename, "r") as file:
        for line in file:
            a = line.split()
            a_int = [int(x) for x in a]
            results.append(a_int)
    return results

def load_lines(filename: str) -> list[str]:
    with open(filename, "r") as file:
        lines = file.read().splitlines() 

    return lines