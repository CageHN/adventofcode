from util import Point
from util.Point import Point


def part1():
    with open('input/day03.input') as file:
        line = file.readline()
        current = Point(0, 0)
        visited = {current}
        directions = {'v': Point.S, '^': Point.N, '<': Point.W, '>': Point.E}
        for c in line:
            current += directions[c]
            visited.add(current)
        print(f'Visited {len(visited)} houses.')


def part2():
    with open('input/day03.input') as file:
        line = file.readline()
        santa = Point(0, 0)
        robot = santa
        visited = {santa}
        directions = {'v': Point.S, '^': Point.N, '<': Point.W, '>': Point.E}
        i = 0
        for c in line:
            if i % 2 == 0:
                santa += directions[c]
                visited.add(santa)
            else:
                robot += directions[c]
                visited.add(robot)
            i += 1
        print(f'Visited {len(visited)} houses.')


if __name__ == '__main__':
    part1()
    part2()
