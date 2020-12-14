from utils import get_lines_from_file


def build_index(lines):
    index = {}
    i = 0
    for line in lines:
        index[i] = parse_line(line)
        i += 1
    return index


def parse_line(line):
    [op, val] = line.split(' ')
    return {'op': op, 'val': int(val), 'run': False}


def execute(index):
    current_index = 0
    acc = 0
    current = index[current_index]

    while current['run'] is False:
        current['run'] = True
        op = current['op']
        if op == 'nop':
            current_index += 1
        elif op == 'acc':
            acc += current['val']
            current_index += 1
        elif op == 'jmp':
            current_index += current['val']

        try:
            current = index[current_index]
        except KeyError:
            return True, acc

    return False, acc


if __name__ == '__main__':
    lines = get_lines_from_file('inputs/day8.txt')

    # Index is a map of line ID to objects
    # Each object is
    # {
    #   'op': 'nop',
    #   'val': -42,
    #   'run': False,
    # }
    index = build_index(lines)

    _, result = execute(index)
    print(f"Went through the program and the acc was {result} when we hit the loop")

    i = -1
    for line in lines:
        i += 1
        if parse_line(line)['op'] == 'acc':
            continue

        # Rebuild the index, since we modified it in previous loop iter
        index = build_index(lines)
        if parse_line(line)['op'] == 'nop':
            index[i]['op'] = 'jmp'
            finished, result_acc = execute(index)
            if finished is True:
                print(f"Found it, replace nop with jmp on line {i}, acc is {result_acc}")

        elif parse_line(line)['op'] == 'jmp':
            index[i]['op'] = 'nop'
            finished, result_acc = execute(index)
            if finished is True:
                print(f"Found it, replace jmp with nop on line {i}, acc is {result_acc}")
