from utils import get_lines_from_file
import re


def parse_input(lines):
    operations = []
    current_mask = lines[0].split('= ')[1]
    ops = []

    for line in lines[1:]:
        if line.startswith('mask'):
            # Flush
            operations.append((current_mask, ops))
            ops = []
            current_mask = line.split('= ')[1]
            continue
        else:
            match = re.match(r"mem\[(\d+)] = (\d+)", line)
            key = int(match.group(1))
            val = int(match.group(2))
            ops.append((key, val))

    operations.append((current_mask, ops))

    return operations


def apply_mask(bit_val, mask):
    new_val = list(bit_val)
    for i in range(len(mask)):
        if mask[i] == 'X':
            continue
        else:
            new_val[i] = mask[i]

    return int(''.join(new_val), 2)


def add_to_mem(op, mem):
    mask = op[0]
    for (addr, val) in op[1]:
        bit_val = format(val, '036b')  # This pads with 0s to length 36
        new_val = apply_mask(bit_val, mask)
        mem[addr] = new_val


if __name__ == '__main__':
    lines = get_lines_from_file('inputs/day14.txt')
    # This dict will hold the map of memory offsets to the values
    # Need to figure out the representation of each
    mem = {}

    # operations is a list of (mask, list_of_tuples)
    # where a mask is `100X100X101011111X100000100X11010011`
    # and a list of tuples would be something like:
    # [(address, value), ..., (33323, 349380),...]
    operations = parse_input(lines)
    for op in operations:
        add_to_mem(op, mem)

    total = 0
    for val in mem.values():
        total += val
    print("Total: ", total)
