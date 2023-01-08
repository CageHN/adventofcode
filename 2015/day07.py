from typing import Optional

from util.Point import Point


def part1():
    with open('input/day07.input') as file:
        lines = file.readlines()
        wires = dict()

        for line in lines:
            s = line.strip()
            wire = parse_wire(s)
            wires[wire.name] = wire

        result = evaluate('a', wires)
        print(f'Signal for wire a is {result & 65535}.')


def part2():
    with open('input/day07.input') as file:
        lines = file.readlines()
        wires = dict()

        for line in lines:
            s = line.strip()
            wire = parse_wire(s)
            wires[wire.name] = wire

        result = evaluate('a', wires)
        for wire in wires.values():
            wire.reset()

        wires['b'] = Wire('b', None, str(result & 65535), None)
        result = evaluate('a', wires)
        print(f'Signal for wire a is {result & 65535}.')


def evaluate(value, wires: dict) -> int:
    if value is None:
        return None
    elif value in wires.keys():
        return wires[value].eval(wires)
    else:
        return int(value)


class Wire:

    def __init__(self, name, operator, input1, input2):
        self.name = name
        self.operator = operator
        self.input1 = input1
        self.input2 = input2
        self.value = None

    def __str__(self) -> str:
        if self.operator is None:
            return self.input1
        elif self.input2 is None:
            return self.operator + ' ' + self.input1
        else:
            return self.input1 + ' ' + self.operator + ' ' + self.input2

    def reset(self):
        self.value = None

    def eval(self, wires: dict) -> int:
        if self.value is None:
            w1 = evaluate(self.input1, wires)
            w2 = evaluate(self.input2, wires)
            match self.operator:
                case 'AND':
                    self.value = w1 & w2
                case 'OR':
                    self.value = w1 | w2
                case 'LSHIFT':
                    self.value = w1 << w2
                case 'RSHIFT':
                    self.value = w1 >> w2
                case 'NOT':
                    self.value = ~ w1
                case _:
                    self.value = w1

        return self.value


def parse_wire(s: str) -> Wire:
    split = s.split(' -> ')
    name = split[-1]
    match split[0].split():
        case [x]:
            return Wire(name, None, x, None)
        case [op, x]:
            return Wire(name, op, x, None)
        case [x, op, y]:
            return Wire(name, op, x, y)
        case _:
            raise Exception('Not supposed to happen!')


if __name__ == '__main__':
    part1()
    part2()
