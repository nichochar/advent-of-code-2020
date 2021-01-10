from collections import defaultdict


INPUT_DATA = (1, 12, 0, 20, 8, 16)
MAX_TURN = 30000000


def solution():
    # mem is a map that tracks, for each number (key)
    # the indexes of turns they were used
    # We clean it to only keep the last 2 as an optimization
    # for part 2
    mem = defaultdict(list)

    current = -1

    # First, we initialize
    turn = 0
    for val in INPUT_DATA:
        turn += 1
        mem[val].append(turn)
        current = val

    # Now, we play!
    while turn < MAX_TURN:
        turn += 1
        current_mem = mem[current]
        if len(current_mem) == 1:
            # The number has never been said before
            # (or rather, only once at the current turn)
            new = 0
            mem[new].append(turn)
        else:
            # The number has been said multiple times before
            last, before_last = mem[current][-1], mem[current][-2]
            new = last - before_last
            mem[new].append(turn)

            # Critical data structure cleaning for performance
            if len(mem[new]) > 2:
                mem[new] = mem[new][-2:]
        current = new
    print("Turn:", turn, "val:", current)


if __name__ == '__main__':
    solution()
