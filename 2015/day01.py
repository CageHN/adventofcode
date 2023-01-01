def part1():
    with open('input/day01.input') as file:
        floor = 0
        for char in file.read():
            floor += 1 if char == '(' else -1
        print(f'Floor: {floor}')


def part2():
    with open('input/day01.input') as file:
        floor = 0
        position = 1
        for char in file.read():
            floor += 1 if char == '(' else -1
            if floor == -1:
                break
            position += 1
        print(f'Position: {position}')


if __name__ == '__main__':
    part1()
    part2()
