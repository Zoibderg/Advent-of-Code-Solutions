"""
No Moudles
"""

class AocSolverDay4:
    """
    A class for solving the Advent of Code 2022 Day 4 puzzle
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
        """
        Solve for part 1:
        Space needs to be cleared and so several Elves
        have been assigned the job of cleaning up sections of the camp
        Every section has a unique ID number, and each Elf is assigned a range of section IDs

        To try to quickly find overlaps and reduce duplicated effort
        the Elves pair up and make a big list of
        the section assignments for each pair (your puzzle input).

        Each line in the list gives the range of section IDs
        that the two Elves assigned to that line are responsible for
        Each line contains section IDs separated by a comma

        In how many assignment pairs does one range fully contain the other?
        """

        # Initialize variables
        fully_contained = 0

        # Loop through each line in the input file
        for line in self.lines:
            # split the line into its ranges remove the newline character
            ranges = line.strip().split(',')
            # pull ranges from the list, remove dashes, and convert to int
            first = [int(x) for x in ranges[0].split('-')]
            second = [int(x) for x in ranges[1].split('-')]
            # check if either range is fully contained in the other
            # if so, increment the fully_contained counter
            if (all(x in range(second[0], second[1] + 1) for x in range(first[0], first[1] + 1)) or
                all(x in range(first[0], first[1] + 1) for x in range(second[0], second[1] + 1))):
                fully_contained += 1

        return fully_contained

    def solve_p2(self):
        """
        Solve for part 2:

        It seems like there is still quite a bit of duplicate work planned
        Instead, the Elves would like to know the number of pairs that overlap at all.

        In how many assignment pairs does at least one section ID overlap?
        """

        # Initialize variables
        overlap = 0

        # Loop through each line in the input file
        for line in self.lines:
            # split the line into its ranges remove the newline character
            ranges = line.strip().split(',')
            # pull ranges from the list, remove dashes, and convert to int
            first = [int(x) for x in ranges[0].split('-')]
            second = [int(x) for x in ranges[1].split('-')]
            # check if either range contains any of the other range
            # if so, increment the overlap counter
            if (any(x in range(second[0], second[1] + 1) for x in range(first[0], first[1] + 1)) or
                any(x in range(first[0], first[1] + 1) for x in range(second[0], second[1] + 1))):
                overlap += 1

        return overlap

if __name__ == '__main__':
    solver = AocSolverDay4('04-camp_cleanup/input.txt')
    print(f"Solution Part 1: {solver.solve_p1()}")
    print(f"Solution Part 2: {solver.solve_p2()}")