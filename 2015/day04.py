import hashlib


def part1():
    with open('input/day04.input') as file:
        line = file.readline()
        i = 0
        while not hashlib.md5((line + str(i)).encode('utf-8')).hexdigest().startswith('00000'):
            i += 1
        print(f'Key: {i}')


def part2():
    with open('input/day04.input') as file:
        line = file.readline()
        i = 0
        while not hashlib.md5((line + str(i)).encode('utf-8')).hexdigest().startswith('000000'):
            i += 1
        print(f'Key: {i}')


if __name__ == '__main__':
    part1()
    part2()
