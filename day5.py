from utils import get_lines_from_file


def binary_search(row_id, max_):
    """
    We assume that the row_id is composed of characters 'B' or 'F'
    for 'back' and 'front' respectively.

    'B' means you pick [4-8] from [0, 8]
    'F' neans you pick [0-4] from [0.8]
    """
    min_ = 0
    for char in row_id:
        if char == 'B':
            min_ = (max_ + min_) / 2
        elif char == 'F':
            max_ = max_ - (max_ - min_) / 2
        else:
            raise Exception("Expect values to be either 'B' of 'F'")
    if min_ == max_ - 1:
        return int(min_)
    else:
        raise Exception("Binary search failed")


def get_one_result(seat):
    # Normalize them both to use 'B' and 'F'
    row_id = seat[:7]
    col_id = seat[7:]
    col_id = col_id.replace('R', 'B').replace('L', 'F')

    row = binary_search(row_id, 128)
    col = binary_search(col_id, 8)
    return row * 8 + col


if __name__ == '__main__':
    lines = get_lines_from_file('day5_input.txt')
    results = []
    for seat in lines:
        results.append(get_one_result(seat))
    print(f"Max: {max(results)}")
    print(f"Min: {min(results)}")
    ordered = sorted(results)

    counter = 80
    for i in range(len(results)):
        if counter == ordered[i]:
            counter += 1
            continue
        else:
            print(f"Missing {counter}")
            break
