from util.Point import Point


def part1():
    with open('input/day06.input') as file:
        lines = file.readlines()

        lights = set()
        for line in lines:
            s = line.strip()
            p1, p2 = parse_points(s)
            for x in range(p1.x, p2.x + 1):
                for y in range(p1.y, p2.y + 1):
                    p = Point(x, y)
                    if s.startswith('turn on'):
                        lights.add(p)
                    elif s.startswith('turn off'):
                        lights.discard(p)
                    else:
                        if p in lights:
                            lights.discard(p)
                        else:
                            lights.add(p)

        print(f'Lights to turn on: {len(lights)}')


def part2():
    with open('input/day06.input') as file:
        lines = file.readlines()

        lights = dict()
        for line in lines:
            s = line.strip()
            p1, p2 = parse_points(s)
            for x in range(p1.x, p2.x + 1):
                for y in range(p1.y, p2.y + 1):
                    p = Point(x, y)
                    b = lights.get(p, 0)
                    if s.startswith('turn on'):
                        lights[p] = b + 1
                    elif s.startswith('turn off'):
                        lights[p] = max(b - 1, 0)
                    else:
                        lights[p] = b + 2

        print(f'Total brightness: {sum(lights.values())}')


def parse_points(s: str):
    split = s.replace(' through ', ',').split(' ')[-1].split(',')
    numbers = [int(x) for x in split]
    return Point(numbers[0], numbers[1]), Point(numbers[2], numbers[3])


if __name__ == '__main__':
    #part1()
    part2()
