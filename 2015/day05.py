def part1():
    with open('input/day05.input') as file:
        lines = file.readlines()

        nice = 0
        for line in lines:
            if is_nice(line.strip()):
                nice += 1

        print(f'Total Nice: {nice}')


def part2():
    with open('input/day05.input') as file:
        lines = file.readlines()

        nice = 0
        for line in lines:
            if is_nice2(line.strip()):
                nice += 1

        print(f'Total Nice: {nice}')


vowels = set('aeiou')
forbidden = {'ab', 'cd', 'pq', 'xy'}


def is_nice(s):
    consecutive = False
    vcount = 0
    if s[0] in vowels:
        vcount += 1

    for i in range(1, len(s)):
        if not consecutive and s[i] == s[i - 1]:
            consecutive = True
        if s[i] in vowels:
            vcount += 1
        if s[i - 1: i + 1] in forbidden:
            return False

    return consecutive and vcount >= 3


def is_nice2(s):
    pairs = dict()
    twice = False
    repeats = False
    for i in range(1, len(s)):
        if twice and repeats:
            break
        if not twice:
            pair = s[i - 1: i + 1]
            if pair in pairs.keys():
                if pairs[pair] != i - 1:
                    twice = True
            else:
                pairs[pair] = i
        if i > 1 and not repeats and s[i - 2] == s[i]:
            repeats = True

    return twice and repeats


if __name__ == '__main__':
    part1()
    part2()
