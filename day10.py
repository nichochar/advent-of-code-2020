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

    # For the solution to problem 2, we need to use the permutation formula
    # https://www.mathplanet.com/education/algebra-2/discrete-mathematics-and-probability/permutations-and-combinations
    # P(n, r) = n! / (n - r)!
    # In our example, the 3 jolt deltas separate the 1 jot delta areas. Since we have no 2 jolt deltas
    # (thank god) we can simply multiply each P with each other, and that should give us the total permutations
    new_lines = [0]
    new_lines.extend(lines)
    new_lines.extend([lines[len(lines) - 1] + 3])
    sub_slices = []
    current = 0
    previous_cursor = 0
    for i in range(len(new_lines)):
        delta = new_lines[i] - current
        if delta == 3:
            sub_slices.append(new_lines[previous_cursor + 1:i - 1])
            previous_cursor = i
        current = new_lines[i]

    print(new_lines)
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
