def part1():
    with open('input/day02.input') as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            dim = [int(x) for x in line.split('x')]
            areas = [dim[0] * dim[1], dim[0] * dim[2], dim[1] * dim[2]]
            total += areas[0] * 2 + areas[1] * 2 + areas[2] * 2 + min(areas)
        print(f'Total: {total}')


def part2():
    with open('input/day02.input') as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            dim = [int(x) for x in line.split('x')]
            perimeters = [(dim[0] + dim[1]) * 2, (dim[0] + dim[2]) * 2, (dim[1] + dim[2]) * 2]
            total += min(perimeters) + dim[0]*dim[1]*dim[2]
        print(f'Total: {total}')


if __name__ == '__main__':
    part1()
    part2()
