from utils import get_lines_from_file


if __name__ == '__main__':
    lines = get_lines_from_file('inputs/day10.txt')
    lines = [int(n) for n in lines]
    # I checked the input and the biggest delta between
    # two consecutive values is 3. This is expected tbh
    # given the rules
    lines.sort()
    print(lines)
    current = 0  # Start with the charging outlet, with 0 volts
    jolt_count_1 = 0
    jolt_count_2 = 0
    jolt_count_3 = 1  # We add one for our adapter
    for i in range(len(lines)):
        delta = lines[i] - current
        if delta == 3:
            jolt_count_3 += 1
        if delta == 1:
            jolt_count_1 += 1
        if delta == 2:
            jolt_count_2 += 1
        current = lines[i]
    print(f"Jolt count 1 diff: {jolt_count_1}")
    print(f"Jolt count 2 diff: {jolt_count_2}")
    print(f"Jolt count 3 diff: {jolt_count_3}")
    print(f"{jolt_count_1} * {jolt_count_3} = {jolt_count_1 * jolt_count_3}")

    # For the solution to problem 2, we need to use the permutation math
    # First we subdivide the problem by breaking into sub-slices
    # around the 3-deltas. Those are basically immutable and give us a
    # set of subproblems.
    # Then each sub-slice has a length of 1, 2 or 3:
    # For length 1: either have it or don't: 2 options
    # For length 2: example is [1, 2, 3],
    # Our permutation options (given the ordering constraint):
    # []
    # [1]
    # [1, 2]
    # [2]
    # For length 3: example [1, 2, 3], we count 7 permutatinos

    # Let's add the 0 and the adapter in our array, to manage
    # boundary conditions better
    new_lines = [0]
    new_lines.extend(lines)
    new_lines.extend([lines[len(lines) - 1] + 3])
    print("New lines, with the plug (0) and the adapter (max+3):", new_lines)

    sub_slices = []
    current = 0
    previous_cursor = 0
    for i in range(len(new_lines)):
        delta = new_lines[i] - current
        if delta == 3:
            sub_slices.append(new_lines[previous_cursor + 1:i - 1])
            previous_cursor = i
        current = new_lines[i]

    combination_count = 1
    # We notice that subslices are only of size 0, 1, 2, 3, 4.
    # We can easily manually count the permutations of such sub-problems
    for s in sub_slices:
        length = len(s)  # noqa
        print(s, "length:", length)
        if length == 3:
            combination_count *= 7
        elif length == 2:
            combination_count *= 4
        elif length == 1:
            combination_count *= 2
        elif length == 4:
            print("we have a length 4")
    print(f"Potential combinations: {combination_count}")
