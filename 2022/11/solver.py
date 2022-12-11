"""
Advent of Code 2022 Day 11
math: https://docs.python.org/3/library/math.html
regex: https://regex101.com/r/4Q9Q2g/1
numexpr: https://numexpr.readthedocs.io/en/latest/user_guide.html
"""
from math import prod
import re
import numexpr as ne

class AocSolverDay11:
    """A class for solving the Advent of Code 2022 Day 11 puzzle"""
    def __init__(self, inputfile):
        self.input = inputfile
        self.data = self.read_input(self.input)
        self.lines = self.data.split('\n')

        self.monkies = self._attendance()

    def read_input(self, file):
        """Read the input file"""
        with open(self.input, 'r', encoding='utf-8') as file:
            return file.read()

    def solve_p1(self, rounds=20):
        """Solver for Part 1"""
        for i in range(rounds):
            print(f"Round {i + 1} of {rounds}...")
            for monkey in self.monkies:
                print(f"Monkey {monkey.key} is inspecting {len(monkey.items)} items...")
                self._process_items(monkey)

        return prod(sorted([monkey.inspections for monkey in self.monkies], reverse=True)[:2])


    def _attendance(self):
        """Take attendance of the monkeys"""
        monkies = []
        monkey_data = [""]

        for line in self.lines:
            if not line:
                monkey_data.append("")
            else:
                monkey_data[-1] += line + "\n"

        for monkey in monkey_data:
            curr_monkey = Monkey()
            rows = monkey.split('\n')

            curr_monkey.key = int(re.findall(r'(\d+)', rows[0])[0])
            curr_monkey.items = [int(x) for x in re.findall(r'(\d+)', rows[1])]
            curr_monkey.operation = rows[2].split(' = ')[1]
            curr_monkey.test = int(re.findall(r'(\d+)', rows[3])[0])
            curr_monkey.true = int(re.findall(r'(\d+)', rows[4])[0])
            curr_monkey.false = int(re.findall(r'(\d+)', rows[5])[0])

            monkies.append(curr_monkey)

        return monkies

    def _process_items(self, monkey):
        """Process the items for the monkey"""
        for item in monkey.items:
            item = self._get_worried(monkey, item)
            item = self._relif(item)

            if item % monkey.test == 0:
                self.monkies[monkey.true].items.append(item)
            else:
                self.monkies[monkey.false].items.append(item)

            monkey.inspections += 1

        monkey.items = []

    def _get_worried(self, monkey, item):
        item = monkey.opfunc(item)

        return item

    def _relif(self, item):
        item = int(item / 3)

        return item

    def solve_p2(self):
        """Solver for Part 2"""
        pass

class Monkey:
    """A class for defining our monkey and its items"""
    def __init__(self):
        self.key = int
        self.items = []
        self.operation = str
        self.opfunc = lambda old: ne.evaluate(self.operation)
        self.test = int
        self.true = int
        self.false = int
        self.inspections = 0


if __name__ == '__main__':
    solver = AocSolverDay11('2022/11/input.txt')
    print(f"Solution Part 1: {solver.solve_p1()}")
    # print(f"Solution Part 2: {solver.solve_p2()}")
