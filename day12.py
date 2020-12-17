import math
from utils import get_lines_from_file


ORDER = ['N', 'E', 'S', 'W']  # this allows for left/right


def parse_line_v1(line, direction):
    letter, num = line[0], int(line[1:])
    if letter == 'N':
        return 0, num, direction
    elif letter == 'E':
        return num, 0, direction
    elif letter == 'S':
        return 0, -num, direction
    elif letter == 'W':
        return -num, 0, direction
    elif letter == 'F':
        return parse_line_v1(direction + str(num), direction)
    elif letter == 'R':
        angle_count = num / 90
        new_direction = ORDER[int((ORDER.index(direction) + angle_count) % 4)]
        return parse_line_v1(new_direction + '0', new_direction)
    elif letter == 'L':
        angle_count = num / 90
        new_direction = ORDER[int((ORDER.index(direction) - angle_count) % 4)]
        return parse_line_v1(new_direction + '0', new_direction)


def parse_line_v2(line, ship_x, ship_y, way_x, way_y):
    letter, num = line[0], int(line[1:])
    if letter == 'N':
        return ship_x, ship_y, way_x, way_y + num
    elif letter == 'E':
        return ship_x, ship_y, way_x + num, way_y
    elif letter == 'S':
        return ship_x, ship_y, way_x, way_y - num
    elif letter == 'W':
        return ship_x, ship_y, way_x - num, way_y
    elif letter == 'F':
        return ship_x + (num * way_x), ship_y + (num * way_y), way_x, way_y
    elif letter == 'R':
        # We solve the trigonometric equations
        # If we call A the angle for the current position
        # and B the angle for the new position
        # new_y = sin(A + B) * r
        # new_y = cos(A + B) * r
        # Then we resolve with classic trigo formulas, and end up with
        # the famous rotation matrix
        angle = -num * math.pi / 180  # convert to radian
        new_way_x = round(way_x * math.cos(angle) - way_y * math.sin(angle))
        new_way_y = round(way_y * math.cos(angle) + way_x * math.sin(angle))
        return ship_x, ship_y, new_way_x, new_way_y
    elif letter == 'L':
        angle = num * math.pi / 180  # convert to radian
        new_way_x = round(way_x * math.cos(angle) - way_y * math.sin(angle))
        new_way_y = round(way_y * math.cos(angle) + way_x * math.sin(angle))
        return ship_x, ship_y, new_way_x, new_way_y


if __name__ == '__main__':
    lines = get_lines_from_file('inputs/day12.txt')
    direction = 'E'
    total_x = 0
    total_y = 0
    for line in lines:
        x, y, direction = parse_line_v1(line, direction)
        total_x += x
        total_y += y
    print(f"[Version 1] Moved {total_x} East and {total_y} North. Manhattan distance: {abs(total_x) + abs(total_y)}")

    direction = 'E'
    x = 0
    y = 0
    way_x = 10
    way_y = 1
    for line in lines:
        x, y, way_x, way_y = parse_line_v2(line, x, y, way_x, way_y)
    print(f"[Version 2] Moved {x} East and {y} North. Manhattan distance: {abs(x) + abs(y)}")
