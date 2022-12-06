"""
No Moudles
"""
class AocSolverDay5:
    """
    A class for solving the Advent of Code 2022 Day 5 puzzle
    """
    def __init__(self, inputfile):
        self.input = inputfile
        self.data = self.read_input(self.input)

    def read_input(self, file):
        """
        Read the input file
        """
        with open(self.input, 'r', encoding='utf-8') as file:
            return file.read()

    def solve_p1(self):
        """
        Solve for Part 1:

        To be able to communicate with the Elves,
        the device needs to lock on to their signal.
        The signal is a series of seemingly-random characters
        that the device receives one at a time

        To fix the communication system, you need to add a subroutine
        to the device that detects a start-of-packet marker in the datastream.
        In the protocol being used by the Elves, the start of a packet
        is indicated by a sequence of four characters that are all different.

        The device will send your subroutine a datastream buffer (your puzzle input);
        your subroutine needs to identify the first position where
        the four most recently received characters were all different.
        Specifically, it needs to report the number of characters
        from the beginning of the buffer to the end of the first such four-character marker.

        How many characters need to be processed
        before the first start-of-packet marker is detected?
        """

        return self._helper(4)

    def solve_p2(self):
        """
        Solve for Part 2:

        Your device's communication system is correctly detecting packets,
        but still isn't working. It looks like it also needs to look for messages.

        A start-of-message marker is just like a start-of-packet marker,
        except it consists of 14 distinct characters rather than 4.
        """

        return self._helper(14)

    def _helper(self, arg0):
        data = self.data
        window = []
        for i, char in enumerate(data):
            window.append(char)
            if len(window) == arg0:
                # print(window)
                if len(set(window)) == arg0:
                    return i + 1
                window.pop(0)
        return -1

if __name__ == '__main__':
    solver = AocSolverDay5('2022/06/input.txt')
    print(f"Solution Part 1: {solver.solve_p1()}")
    print(f"Solution Part 2: {solver.solve_p2()}")
