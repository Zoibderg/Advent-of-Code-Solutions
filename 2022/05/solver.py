"""
No Moudles
"""
import re
from collections import defaultdict
class AocSolverDay5:
    """
    A class for solving the Advent of Code 2022 Day 5 puzzle
    """
    def __init__(self, inputfile):
        self.input = inputfile
        self.lines = self.read_input(self.input)
        self.stacks = defaultdict(list)
        self.commands = None

    def read_input(self, file):
        """
        Read the input file and return a list of lines
        """
        with open(self.input, 'r', encoding='utf-8') as file:
            return file.read()

    def parse_input(self):
        """
        Parse the input file and return a the stacks and commands
        """
        raw_stacks, raw_commands = self.lines.split('\n\n')
        data = raw_stacks.split('\n')

        # create the stacks
        rows = data[:-1]
        self.stacks = defaultdict(list)

        for row in rows:
            results = re.findall(r'(\[([A-Z])\]|\s{3})\s?', row)
            for i, (_, result) in enumerate(results):
                if result != '':
                    self.stacks[i + 1].append(result)

        # reverse the stacks
        for stack in self.stacks.values():
            stack.reverse()

        self.commands = ([re.findall(r'move (\d+) from (\d+) to (\d+)', command)
        for command in raw_commands.split('\n')])

        return self.stacks, self.commands

    def solve_p1(self):
        """
        Solve for part 1:
        Supplies are stored in stacks of marked crates,
        but because the needed supplies are buried under many other crates,
        the crates need to be rearranged.

        they forgot to ask her which crate will end up where,
        and they want to be ready to unload them as soon as possible so they can embark.

        They do, however, have a drawing
        of the starting stacks of crates and
        the rearrangement procedure (your puzzle input).

        Crates are moved one at a time

        After the rearrangement procedure completes,
        what crate ends up on top of each stack?
        """

        self.parse_input()

        for command in self.commands:
            # first is the number of crates to move
            # second is the stack to move from
            # third is the stack to move to
            num, frm, stop = command[0]

            # move the crates
            self.stacks[int(stop)].extend([self.stacks[int(frm)].pop() for _ in range(int(num))])

        # return the top of each stack
        return ''.join([self.stacks[i].pop() for i in range(1, len(self.stacks) + 1)])

    def solve_p2(self):
        """
        Solve for part 2:

        As you watch the crane operator expertly rearrange the crates,
        you notice the process isn't following your prediction.
        Some mud was covering the writing on the side of the crane,
        and you quickly wipe it away.
        The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

        The new version of the crane can move multiple crates at once,

        After the rearrangement procedure completes, what crate ends up on top of each stack?
        """

        self.parse_input()

        for command in self.commands:
            # first is the number of crates to move
            # second is the stack to move from
            # third is the stack to move to
            num, frm, stop = command[0]

            # move the crates
            crates_to_move = self.stacks[int(frm)][-int(num):]
            self.stacks[int(stop)].extend(crates_to_move)
            self.stacks[int(frm)] = self.stacks[int(frm)][:-int(num)]

        # return the top of each stack
        return ''.join([self.stacks[i].pop() for i in range(1, len(self.stacks) + 1)])



if __name__ == '__main__':
    solver = AocSolverDay5('05-supply_stacks/input.txt')
    print(f"Solution Part 1: {solver.solve_p1()}")
    print(f"Solution Part 2: {solver.solve_p2()}")
