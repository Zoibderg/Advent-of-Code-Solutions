"""
No modules
"""

import itertools

class AocSolverDay14:
    """A class for solving the Advent of Code 2022 Day 14 puzzle"""
    def __init__(self, inputfile):
        self.input = inputfile
        self.lines = self.read_input(self.input)

    def read_input(self, file):
        """Read the input file"""
        with open(self.input, 'r', encoding='utf-8') as file:
            return file.readlines()

    def solve_p1(self):
        """ Solver for Part 1 """
        blocked = set()
        abyss = 0

        abyss = self.parse_input(blocked, abyss)

        return self.drop_sand(blocked, abyss, 1)

    def solve_p2(self):
        """ Solver for Part 2 """
        blocked = set()
        abyss = 0

        abyss = self.parse_input(blocked, abyss)

        return self.drop_sand(blocked, abyss, 2)

    def drop_sand(self, blocked, abyss, part):
        """
        Drop sand and count how many sand particles are at rest before sand
        falls into the abyss
        """
        sand_at_rest = 0

        if part == 1:
            # Part 1
            while True:
                sand = 500
                while True:
                    if sand.imag >= abyss:
                        return sand_at_rest
                    if sand + 1j not in blocked:
                        sand += 1j
                        continue
                    if sand + 1j - 1 not in blocked:
                        sand += 1j - 1
                        continue
                    if sand + 1j + 1 not in blocked:
                        sand += 1j + 1
                        continue
                    blocked.add(sand)
                    sand_at_rest += 1
                    break

        if part == 2:
            # Part 2
            while 500 not in blocked:
                sand = 500
                while not sand.imag >= abyss:
                    if sand + 1j not in blocked:
                        sand += 1j
                        continue
                    if sand + 1j - 1 not in blocked:
                        sand += 1j - 1
                        continue
                    if sand + 1j + 1 not in blocked:
                        sand += 1j + 1
                        continue
                    break
                blocked.add(sand)
                sand_at_rest += 1

        return sand_at_rest

    def parse_input(self, blocked, abyss):
        """Parse the input"""
        # will parse the normal way as regex does not seem necessary
        for line in self.lines:
            line = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
            for (x_1, y_1), (x_2, y_2) in zip(line, line[1:]):
                x_1, x_2 = sorted([x_1, x_2])
                y_1, y_2 = sorted([y_1, y_2])
                for x, y in itertools.product(range(x_1, x_2 + 1), range(y_1, y_2 + 1)):
                    # keep x as real part
                    # convert y to imaginary part
                    blocked.add(x + y * 1j)
                    abyss = max(abyss, y + 1)
        return abyss


if __name__ == '__main__':
    solver = AocSolverDay14('2022/14/input.txt')
    print(f"Solution Part 1: {solver.solve_p1()}")
    print(f"Solution Part 2: {solver.solve_p2()}")
