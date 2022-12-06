"""
No Moudles
"""
class AocSolverDay1:
    """
    A class for solving the Advent of Code 2022 Day 1 puzzle
    """
    def __init__(self, inputfile):
        self.input = inputfile

    def read_input(self, file):
        """
        Read the input file and return a list of lines
        """
        with open(self.input, 'r', encoding='utf-8') as file:
            return file.readlines()

    def solve_p1(self):
        """
        Solve for part 1:
        Find the elf holding the most calories and return that total
        """
        lines = self.read_input(self.input)

        # keep running total of lines
        total_elf = 0
        highest_elf = 0

        # find the elf with the highest amout of calories
        # each line is a string, so we need to convert to int
        # we also need to remove the newline character
        # we can do this with the strip() method
        for line in lines:
            if line.strip() == '':
                if total_elf > highest_elf:
                    highest_elf = total_elf
                total_elf = 0
            else:
                total_elf += int(line.strip())

        return highest_elf

    def solve_p2(self):
        """
        Solve for part 2:
        Find the 3 elves holding the most calories and return that total
        """
        lines = self.read_input(self.input)

        # keep running total of lines
        total_elf = 0
        elf_count = 0
        total_group = {}

        # the 3 elfs with the most calories
        for line in lines:
            if line.strip() == '':
                total_group[elf_count] = total_elf
                total_elf = 0
            else:
                total_elf += int(line.strip())
                elf_count += 1

        # sort the total group, descending, and return the total of the first 3
        sorted_group = sorted(total_group.items(), key=lambda x: x[1], reverse=True)
        return sum(x[1] for x in sorted_group[:3])

if __name__ == '__main__':
    solver = AocSolverDay1('01-calorie_counting/input.txt')
    print(f"Solution Part 1: {solver.solve_p1()}")
    print(f"Solution Part 2: {solver.solve_p2()}")
