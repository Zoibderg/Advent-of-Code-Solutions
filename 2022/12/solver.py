"""
No modules
"""

class AocSolverDay11:
    """A class for solving the Advent of Code 2022 Day 11 puzzle"""
    def __init__(self, inputfile):
        self.input = inputfile
        self.data = self.read_input(self.input)
        self.lines = self.data.split('\n')

    def read_input(self, file):
        """Read the input file"""
        with open(self.input, 'r', encoding='utf-8') as file:
            return file.read()

    def solve_p1(self):
        """Solver for Part 1"""
        pass

    def solve_p2(self):
        """Solver for Part 2"""
        pass

if __name__ == '__main__':
    solver = AocSolverDay11('2022/11/input.txt')
    # print(f"Solution Part 1: {solver.solve_p1()}")
    print(f"Solution Part 2: {solver.solve_p2()}")