"""
No modules
"""

from collections import deque


class AocSolverDay12:
    """A class for solving the Advent of Code 2022 Day 12 puzzle"""
    def __init__(self, inputfile):
        self.input = inputfile
        self.data = self.read_input(self.input)
        self.lines = self.data.split('\n')

        self.heightmap, self.start, self.end  = self._parse_map(self.lines)

        self.visited = set()

    def read_input(self, file):
        """Read the input file"""
        with open(self.input, 'r', encoding='utf-8') as file:
            return file.read()

    def solve_p1(self):
        """
        Solver for Part 1

        You ask the device for a heightmap of the surrounding area (your puzzle input).
        The heightmap shows the local area from above broken into a grid; the elevation
        of each square of the grid is given by a single lowercase letter, where a is
        the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

        Also included on the heightmap are marks for your current position (S) and the
        location that should get the best signal (E). Your current position (S)
        has elevation a, and the location that should get the best signal (E) has elevation z.

        You'd like to reach E, but to save energy, you should do it in as few steps as possible.
        During each step, you can move exactly one square up, down, left, or right.
        To avoid needing to get out your climbing gear, the elevation of the destination square
        can be at most one higher than the elevation of your current square;
        that is, if your current elevation is m, you could step to elevation n,
        but not to elevation o.
        (This also means that the elevation of the destination square can be much lower than
        the elevation of your current square.)

        What is the fewest steps required to move from your current position to the
        location that should get the best signal?
        """

        # use bfs to find the shortest path
        queue = deque()
        queue.append((self.start, 0))
        self.visited.add(self.start)

        while queue:
            pos, steps = queue.popleft()
            if pos == self.end:
                return steps

            for neighbor in self._get_neighbors(pos):
                if neighbor not in self.visited:
                    queue.append((neighbor, steps + 1))
                    self.visited.add(neighbor)

    def solve_p2(self):
        """Solver for Part 2
        reverse the search direction
        start from the end and find the shortest path to any location
        at elevation a
        """
        # use bfs to find the shortest path
        queue = deque()
        queue.append((self.end, 0))
        self.visited.add(self.end)

        while queue:
            pos, steps = queue.popleft()
            if self.heightmap[pos] == ord('a'):
                return steps

            for neighbor in self._get_neighbors(pos, reverse=True):
                if neighbor not in self.visited:
                    queue.append((neighbor, steps + 1))
                    self.visited.add(neighbor)

    def _get_neighbors(self, pos, reverse=False):
        """Get all valid neighbors of a position"""
        x, y = pos
        neighbors = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
        if reverse:
            return [n for n in neighbors if self._is_valid(pos, n, reverse=True)]
        return [n for n in neighbors if self._is_valid(pos, n)]

    def _is_valid(self, pos, check, reverse=False):
        """Check if a position is valid"""

        # check if the position is in the heightmap
        if check not in self.heightmap:
            return False

        # check if the position is higher than the current position
        if reverse:
            if self.heightmap[pos] - self.heightmap[check] <= 1:
                return True

        elif self.heightmap[check] - self.heightmap[pos] <= 1:
            return True
        return False

    def visualize_map(self):
        "print the heightmap in its starting state"
        for pos, char in self.heightmap.items():
            if pos == self.start:
                print(ord('a'), end='  ')
            elif pos == self.end:
                print(ord('z'), end='  ')
            elif pos in self.visited:
                print('X', end='  ')
            else:
                print(char, end='  ')
            if pos[0] == max(self.heightmap.keys())[0]:
                print()

    def _parse_map(self, lines):
        """Parse the heightmap"""
        heightmap = {}
        start = None
        end = None

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == 'S':
                    heightmap[(x, y)] = ord('a')
                    start = (x, y)
                elif char == 'E':
                    heightmap[(x, y)] = ord('z')
                    end = (x, y)
                else:
                    heightmap[(x, y)] = ord(char)

        return heightmap, start, end

if __name__ == '__main__':
    solver = AocSolverDay12('2022/12/input.txt')
    # print(f"Solution Part 1: {solver.solve_p1()}")
    print(f"Solution Part 2: {solver.solve_p2()}")