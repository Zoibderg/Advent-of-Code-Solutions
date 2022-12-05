"""
No Moudles
"""

class AocSolverDay5:
    """
    A class for solving the Advent of Code 2022 Day 5 puzzle
    """
    def __init__(self, inputfile):
        self.input = inputfile
        self.lines = self.read_input(self.input)

    def read_input(self, file):
        """
        Read the input file and return a list of lines
        """
        with open(self.input, 'r', encoding='utf-8') as file:
            return file.readlines()

    def solve_p1(self):

if __name__ == '__main__':
    solver = AocSolverDay5('4-camp_cleanup/input.txt')
    print(f"Solution Part 1: {solver.solve_p1()}")
    # print(f"Solution Part 2: {solver.solve_p2()}")