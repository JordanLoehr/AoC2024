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