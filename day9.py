from utils import get_lines_from_file


def is_number_a_sum(target, candidates):
    sorted_candidates = sorted(candidates)

    # Remember day 1? ;)
    total = -1
    for val1 in sorted_candidates:
        if total == target:
            return True
        for val2 in reversed(sorted_candidates):
            total = val1 + val2
            if total == target:
                return True
            elif total < target:
                break
    return False


if __name__ == '__main__':
    lines = get_lines_from_file('inputs/day9.txt')
    lines = [int(n) for n in lines]
    length = len(lines)

    candidates = lines[0:25]
    number = lines[25]
    target = -1
    for i in range(length - 25):
        candidates = lines[i:i + 25]
        target = lines[i + 25]

        if is_number_a_sum(target, candidates) is False:
            print(f"Line {i}'s value {target} is not a sum of previous 25")
            break

    # Now that we have our target, we search for a continuous set
    # of at least 2 numbers  that sum to it.
    finished = False
    for lower_cursor in range(length):
        if finished is True:
            break
        for higher_cursor in range(length - lower_cursor):
            total = sum(lines[lower_cursor:higher_cursor])
            if total > target:
                break
            if total == target:
                # We are good!
                final_range = lines[lower_cursor:higher_cursor]
                print(f"The desired sum is {min(final_range) + max(final_range)}")
                finished = True
