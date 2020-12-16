from utils import get_lines_from_file


FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'


def state_from_input(lines):
    """
    We build the state as an array of strings values
    """
    width = len(lines[0])
    height = len(lines)

    state = [[0 for n in range(width)] for h in range(height)]

    for i in range(height):
        for j in range(width):
            state[i][j] = lines[i][j]

    return state


def get_adjacent_values(i, j, state):
    height = len(state)
    width = len(state[0])
    # Values is an array of length 3 to 8, based on limit conditions
    values = []
    to_attempt = [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
        (i, j - 1),
    ]
    for (r, c) in to_attempt:
        if r < 0 or c < 0 or r >= height or c >= width:
            continue
        values.append(state[r][c])
    return values


def count_visible_occupied(i, j, state):  # noqa
    count = 0
    height = len(state)
    width = len(state[0])
    # Go up
    r, c = i - 1, j
    while r >= 0:
        if state[r][c] == OCCUPIED:
            count += 1
            break
        if state[r][c] == EMPTY:
            break
        r -= 1
    # Go down
    r, c = i + 1, j
    while r < height:
        if state[r][c] == OCCUPIED:
            count += 1
            break
        if state[r][c] == EMPTY:
            break
        r += 1
    # Go left
    r, c = i, j - 1
    while c >= 0:
        if state[r][c] == OCCUPIED:
            count += 1
            break
        if state[r][c] == EMPTY:
            break
        c -= 1
    # Go Right
    r, c = i, j + 1
    while c < width:
        if state[r][c] == OCCUPIED:
            count += 1
            break
        if state[r][c] == EMPTY:
            break
        c += 1
    # Go top left
    r, c = i - 1, j - 1
    while r >= 0 and c >= 0:
        if state[r][c] == OCCUPIED:
            count += 1
            break
        if state[r][c] == EMPTY:
            break
        r -= 1
        c -= 1
    # Go top right
    r, c = i - 1, j + 1
    while r >= 0 and c < width:
        if state[r][c] == OCCUPIED:
            count += 1
            break
        if state[r][c] == EMPTY:
            break
        r -= 1
        c += 1
    # Go bottom left
    r, c = i + 1, j - 1
    while r < height and c >= 0:
        if state[r][c] == OCCUPIED:
            count += 1
            break
        if state[r][c] == EMPTY:
            break
        r += 1
        c -= 1
    # Go bottom right
    r, c = i + 1, j + 1
    while r < height and c < width:
        if state[r][c] == OCCUPIED:
            count += 1
            break
        if state[r][c] == EMPTY:
            break
        r += 1
        c += 1

    return count


def get_next_state_v1(state):
    """
    This function returns a new state (we don't modify the passed in
    state) based on the rules:
        * If a seat is empty (L) and there are no occupied seats adjacent to it,
          the seat becomes occupied.
        * If a seat is occupied (#) and four or more seats adjacent to it are
          also occupied, the seat becomes empty.
        * Otherwise, the seat's state does not change.
    """
    width = len(state[0])
    height = len(state)
    new_state = [[0 for n in range(width)] for h in range(height)]

    for i in range(height):
        for j in range(width):
            current = state[i][j]
            adj_values = get_adjacent_values(i, j, state)
            if current == EMPTY:
                if OCCUPIED not in adj_values:
                    new_state[i][j] = OCCUPIED
                    continue
            if current == OCCUPIED:
                if adj_values.count(OCCUPIED) >= 4:
                    new_state[i][j] = EMPTY
                    continue
            new_state[i][j] = state[i][j]
    return new_state


def get_next_state_v2(state):
    """
    This function returns a new state (we don't modify the passed in
    state) based on the rules:
        * If a seat is empty (L) and there are no occupied visible to it
          in all directions, the seat becomes occupied.
        * If a seat is occupied (#) and FIVE or more seats visible to it are
          also occupied, the seat becomes empty.
        * Otherwise, the seat's state does not change.
    """
    width = len(state[0])
    height = len(state)
    new_state = [[0 for n in range(width)] for h in range(height)]

    for i in range(height):
        for j in range(width):
            current = state[i][j]
            if current == EMPTY:
                if count_visible_occupied(i, j, state) == 0:
                    new_state[i][j] = OCCUPIED
                    continue
            if current == OCCUPIED:
                if count_visible_occupied(i, j, state) >= 5:
                    new_state[i][j] = EMPTY
                    continue
            new_state[i][j] = state[i][j]
    return new_state


def print_state(state):
    print("\nPrinting state:")
    for line in state:
        print(''.join(line))


def solve_v1(current_state):
    while True:
        # print_state(current_state)  # use to debug
        next_state = get_next_state_v1(current_state)
        if next_state == current_state:
            break
        current_state = next_state

    print("The state has converged. Counting...")
    counter = 0
    for i in range(len(current_state)):
        for j in range(len(current_state[0])):
            if current_state[i][j] == OCCUPIED:
                counter += 1
    print(f"Counted {counter} occupied seats (V1)")


def solve_v2(current_state):
    while True:
        # print_state(current_state)  # use to debug
        next_state = get_next_state_v2(current_state)
        if next_state == current_state:
            break
        current_state = next_state

    print("The state has converged. Counting...")
    counter = 0
    for i in range(len(current_state)):
        for j in range(len(current_state[0])):
            if current_state[i][j] == OCCUPIED:
                counter += 1
    print(f"Counted {counter} occupied seats (V2)")


if __name__ == '__main__':
    lines = get_lines_from_file('inputs/day11.txt')
    current_state = state_from_input(lines)

    solve_v1(current_state)

    current_state = state_from_input(lines)
    solve_v2(current_state)
