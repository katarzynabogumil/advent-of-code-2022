def main():
    with open('input_data.txt', 'r') as input_data:
        instructions = [line.strip().split(' ') for line in input_data.readlines()]

    part_1(instructions)
    part_2(instructions)


def part_1(instructions):
    previous_positions = set()
    pos_H = (0, 0)
    pos_T = (0, 0)

    for instruction in instructions:
        direction, steps = instruction
        for n in range(int(steps)):
            last_pos_H = pos_H 
            pos_H = move_H(pos_H, direction)

            if not are_touching(pos_H, pos_T):
                previous_positions.add(pos_T)
                pos_T = last_pos_H
            
    previous_positions.add(pos_T)

    print('part 1:', len(previous_positions))


def part_2(instructions):
    previous_positions = set()
    rope = [(0, 0) for i in range(10)]
    pos_H = (0, 0)

    for instruction in instructions:
        direction, steps = instruction
        for i in range(int(steps)):

            rope[0] = move_H(rope[0], direction)

            for n in range(9):
                if not are_touching(rope[n], rope[n+1]):
                    rope[n+1] = move_rope(rope[n], rope[n+1])

            previous_positions.add(rope[-1])

    print('part 2:', len(previous_positions))


def move_rope(a, b):
    x_a, y_a = a
    x_b, y_b = b
    dif_x = x_a - x_b
    dif_y = y_a - y_b

    if abs(dif_x) == 2:
        dif_x = dif_x / 2
    if abs(dif_y) == 2:
        dif_y = dif_y / 2

    return (x_b + dif_x, y_b + dif_y)

    
def move_H(position, direction):
    x, y = position

    if direction == 'R':
        position = (x + 1, y)
    elif direction == 'L':
        position = (x - 1, y)
    elif direction == 'U':
        position = (x, y + 1)
    else: 
        position = (x, y - 1)

    return position


def are_touching(pos_H, pos_T):
    x_H, y_H = pos_H
    x_T, y_T = pos_T
    if x_T in [x_H - 1, x_H, x_H + 1] and y_T in [y_H - 1, y_H, y_H + 1]:
        return True
    return False


if __name__ == "__main__":
    main()