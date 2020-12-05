def is_valid1(line):
    part1, part2, password = line.split(' ')
    min_, max_ = [int(n) for n in part1.split('-')]
    char = part2[0]
    letter_count = 0
    for elt in password:
        if elt == char:
            letter_count += 1

    return letter_count >= min_ and letter_count <= max_


def is_valid2(line):
    part1, part2, password = line.split(' ')
    pos1, pos2 = [int(n) for n in part1.split('-')]
    char = part2[0]
    count = 0
    if password[pos1 - 1] == char:
        count += 1
    if password[pos2 - 1] == char:
        count += 1
    return count == 1


def solution(lines, is_valid_fn):
    valid_count = 0
    for line in lines:
        if is_valid_fn(line):
            valid_count += 1
    return valid_count


if __name__ == '__main__':
    with open('day2_input.txt', 'r') as f:
        data = f.read()
        lines = [x for x in data.split('\n') if x]

    print(f"Found {solution(lines, is_valid1)} valid passwords (solution1)")
    print(f"Found {solution(lines, is_valid2)} valid passwords (solution2)")
