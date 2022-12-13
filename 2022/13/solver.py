"""
No modules
"""
import ast
from itertools import zip_longest
from functools import cmp_to_key

class AocSolverDay13:
    """A class for solving the Advent of Code 2022 Day 13 puzzle"""
    def __init__(self, inputfile):
        self.input = inputfile
        self.lines = self.read_input(self.input)
        self.raw_packets = self.lines
        self.packets = self._parse_packets(self.lines)

    def read_input(self, file):
        """Read the input file"""
        with open(self.input, 'r', encoding='utf-8') as file:
            return file.readlines()

    def solve_p1(self):
        """
        Solver for Part 1

        Your handheld device must still not be working properly;
        the packets from the distress signal got decoded out of order.
        You'll need to re-order the list of received packets (your puzzle input)
        to decode the message

        Your list consists of pairs of packets; pairs are separated by a blank line.
        You need to identify how many pairs of packets are in the right order.

        Packet data consists of lists and integers. Each list starts with [, ends with ],
        and contains zero or more comma-separated values (either integers or other lists).
        Each packet is always a list and appears on its own line.

        When comparing two values, the first value is called left and the second value
        is called right. Then:

        If both values are integers, the lower integer should come first.
        If the left integer is lower than the right integer, the inputs are in the right order.

        If both values are lists, compare the first value of each list, then the second value,
        and so on. If the left list runs out of items first, the inputs are in the right order.

        If the lists are the same length and no comparison makes a decision about the order,
        continue checking the next part of the input.

        If exactly one value is an integer, convert the integer to a list
        which contains that integer as its only value, then retry the comparison.
        """

        # count the number of packets that are in the right order
        # and return the sum of their indices
        return (sum(i + 1 for i, packet in enumerate(self.packets)
        if self.compare(packet.left, packet.right) >= 0))

    def solve_p2(self):
        """Solver for Part 2"""
        markers = [[[6]], [[2]]]
        packets_markers = self.add_markers(self.raw_packets, markers)
        idx1, idx2 = [packets_markers.index(marker) for marker in markers]

        return (idx1 + 1) * (idx2 + 1)

    def _parse_packets(self, lines):
        """Parse the input file into packets"""
        packets = [ast.literal_eval(line) for line in lines if line.strip()]

        self.raw_packets = packets

        return [Packet(left, right) for left, right in zip_longest(packets[::2], packets[1::2])]

    def compare(self, left, right):
        """Compare two packets"""

        if isinstance(left, int):
            if isinstance(right, int):
                return 1 if left < right else -1 if left > right else 0

            left = [left]

        if isinstance(right, int):
            right = [right]

        return (next((c for c in (self.compare(le, re) for le, re in zip(left, right))
        if c != 0), 1 if len(left) < len(right) else -1 if len(left) > len(right) else 0))

    def add_markers(self, packets, markers):
        """Add markers to a packet"""
        return sorted(packets + markers, key=cmp_to_key(self.compare), reverse=True)

class Packet:
    """A class for storing packets"""
    def __init__(self, left, right):
        self.left = left
        self.right = right

if __name__ == '__main__':
    solver = AocSolverDay13('2022/13/input.txt')
    # print(f"Solution Part 1: {solver.solve_p1()}")
    print(f"Solution Part 2: {solver.solve_p2()}")
