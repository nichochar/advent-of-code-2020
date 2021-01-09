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


def get_36_padded_bit_val(int_val):
    return format(int_val, '036b')  # This pads with 0s to length 36


def apply_mask(bit_val, mask):
    new_val = list(bit_val)
    for i in range(len(mask)):
        if mask[i] == 'X':
            continue
        else:
            new_val[i] = mask[i]

    return int(''.join(new_val), 2)


def get_new_addrs(bit_addr, mask):
    """
    Applies the mask for part 2.
    Returns a list of strings for each memory addr
    """
    size = mask.count('X')
    perms = get_all_permutations(size)
    bit_addr_list = list(bit_addr)
    for i in range(len(mask)):
        if mask[i] == 'X':
            bit_addr_list[i] = '%s'  # We will use these for substitution
        if mask[i] == '1':
            bit_addr_list[i] = '1'

    formattable_str = ''.join(bit_addr_list)
    return [formattable_str % variant for variant in perms]


def add_to_mem_v1(op, mem):
    mask = op[0]
    for (addr, val) in op[1]:
        bit_val = get_36_padded_bit_val(val)
        new_val = apply_mask(bit_val, mask)
        mem[addr] = new_val


def add_to_mem_v2(op, mem):
    mask = op[0]
    for (addr, val) in op[1]:
        bit_addr = get_36_padded_bit_val(addr)
        new_addrs = get_new_addrs(bit_addr, mask)
        for new_addr in new_addrs:
            mem[new_addr] = val


def get_all_permutations(size):
    """
    Returns all possible permutations (as a list of tuples)
    of 0s and 1s for a string of a given size
    Example:
        If size == 2, returns [
            ('0', '0'),
            ('0', '1'),
            ('1', '0'),
            ('1', '1'),
        ]
    """
    assert size >= 0
    if size == 0:
        return []
    result = ['0', '1']
    while len(result[0]) != size:
        current = []
        for elt in result:
            current.append('1' + elt)
            current.append('0' + elt)
        result = current
    return [tuple(elt) for elt in result]


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
        add_to_mem_v1(op, mem)

    # This is now the sum of values of the memory which
    # is the solution to the first part of the problem
    total = 0
    for val in mem.values():
        total += val
    print("Part 1 solution: ", total)

    # Part 2 is actually pretty different so let's write separate code
    # Let's reinitialize
    mem = {}
    for op in operations:
        add_to_mem_v2(op, mem)
    total = 0
    for val in mem.values():
        total += val
    print("Part 2 solution: ", total)
