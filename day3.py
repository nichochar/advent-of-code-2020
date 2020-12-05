from utils import get_lines_from_file


def solution(lines, params):
    line_length = len(lines[0])
    count = 0
    for i in range(len(lines)):
        # iterate on each row
        try:
            if lines[i * params[1]][(i * params[0]) % line_length] == '#':
                # we hit a tree!
                count += 1
        except IndexError:
            break
    return count


if __name__ == '__main__':
    lines = get_lines_from_file('inputs/day3.txt')

    params = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    solutions = [solution(lines, param) for param in params]
    print(solutions)
    total = 1
    for element in solutions:
        total *= element

    print(f"total: {total}")
