from utils import get_lines_from_file


TARGET = 2020


def solution1():
    values = get_lines_from_file('inputs/day1.txt')
    values = [int(val) for val in values]
    sorted_values = sorted(values)
    total = 0
    saved_val1 = 0
    saved_val2 = 0
    for val1 in sorted_values:
        if total == 2020:
            break
        for val2 in reversed(sorted_values):
            total = val1 + val2
            if total <= 2020:
                saved_val1 = val1
                saved_val2 = val2
                break

    return (saved_val1, saved_val2, saved_val1 + saved_val2, saved_val1 * saved_val2)


def solution2():
    values = get_lines_from_file('inputs/day1.txt')
    values = [int(val) for val in values]
    sorted_values = sorted(values)
    sorted_values_trimmed = sorted([val for val in values if (val + sorted_values[0] + sorted_values[1] < 2020)])

    saved1 = 0
    saved2 = 0
    saved3 = 0
    exit = False
    for val1 in sorted_values_trimmed:
        if exit is True:
            break
        for val2 in sorted_values_trimmed:
            if exit is True:
                break
            if val1 + val2 > 2020:
                break
            for val3 in sorted_values_trimmed:
                if val1 + val2 + val3 == 2020:
                    saved1 = val1
                    saved2 = val2
                    saved3 = val3
                    exit = True
                    break
                if val1 + val2 + val3 > 2020:
                    break
    return (saved1, saved2, saved3, saved1 + saved2 + saved3, saved1 * saved2 * saved3)


if __name__ == '__main__':
    print("Solution 1:", solution1())
    print("Solution 2:", solution2())
