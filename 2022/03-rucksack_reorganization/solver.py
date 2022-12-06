"""
No Moudles
"""

class AocSolverDay3:
    """
    A class for solving the Advent of Code 2022 Day 3 puzzle
    """
    def __init__(self, inputfile):
        self.input = inputfile
        self.lines = self.read_input(self.input)
        self.sop = None

    def read_input(self, file):
        """
        Read the input file and return a list of lines
        """
        with open(self.input, 'r', encoding='utf-8') as file:
            return file.readlines()

    def solve_p1(self):
        """
        Solve for part 1:

        Each rucksack has two large compartments
        All items of a given type are meant to go into exactly one of the two compartments
        The Elf that did the packing failed to follow this rule
        for exactly one item type per rucksack

        The Elves have made a list of all of the items
        currently in each rucksack (your puzzle input),
        but they need your help finding the errors
        Every item type is identified by a single lowercase or uppercase letter

        The list of items for each rucksack is given
        as characters all on a single line
        A given rucksack always has the same number of items in each of its two compartment
        The first half of the list is the items in the first compartment
        The second half is the items in the second compartment

        To help prioritize item rearrangement, every item type can be converted to a priority:
        Lowercase item types a through z have priorities 1 through 26.
        Uppercase item types A through Z have priorities 27 through 52.

        Find the item type that appears in both compartments of each rucksack
        What is the sum of the priorities of those item types?
        """

        # Initialize variables
        self.sop = 0
        # Loop through each line in the input file
        for line in self.lines:
            # Split the line into two halves
            # The first half is the items in the first compartment
            # The second half is the items in the second compartment
            half = len(line) // 2
            first = line[:half]
            second = line[half:]

            # Loop through each item in the first compartment
            for item in first:
                # If the item is in the second compartment
                if item in second:
                    # Add the priority of the item to the sum of priorities
                    # print(item)
                    self.sop += ord(item) - 96 if item.islower() else ord(item) - 38
                    break
        # Return the sum of priorities
        return self.sop

    def solve_p2(self):
        """
        Solve for part 2:

        For safety, the Elves are divided into groups of three
        Every Elf carries a badge that identifies their group

        the badge is the only item type carried by all three Elves

        All of the badges need to be pulled out of the rucksacks
        so the new authenticity stickers can be attached

        The only way to tell which item type is the right one
        is by finding the one item type that is common between all three Elves in each group

        Every set of three lines in your list corresponds to a single group
        but each group can have a different badge item type

        Find the item type that corresponds to the badges of each three-Elf group
        What is the sum of the priorities of those item types?
        """

        # Initialize variables
        self.sop = 0
        # Loop through each line in the input file
        # each line represents a rucksack
        # every three lines represent a group of three Elves
        for i in range(0, len(self.lines), 3):
            # Initialize variables
            first = self.lines[i]
            second = self.lines[i + 1]
            third = self.lines[i + 2]
            # Loop through each item in the first compartment
            for item in first:
                # If the item is in the second compartment
                # and the item is in the third compartment
                if item in second and item in third:
                    # Add the priority of the item to the sum of priorities
                    # print(item)
                    self.sop += ord(item) - 96 if item.islower() else ord(item) - 38
                    break
        # Return the sum of priorities
        return self.sop


if __name__ == '__main__':
    solver = AocSolverDay3('03-rucksack_reorganization/input.txt')
    print(f"Solution Part 1: {solver.solve_p1()}")
    print(f"Solution Part 2: {solver.solve_p2()}")
