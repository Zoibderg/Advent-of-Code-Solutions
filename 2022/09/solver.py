"""
No Moudles
"""
class AocSolverDay9:
    """A class for solving the Advent of Code 2022 Day 9 puzzle"""
    def __init__(self, inputfile):
        self.input = inputfile
        self.data = self.read_input(self.input)
        self.lines = self.data.split('\n')

        # create a rope object
        self.rope = Rope()

        # create a grid of all the positions the tail of the rope visits
        self.tail_grid = self.rope.movement_grid

    def read_input(self, file):
        """Read the input file"""
        with open(self.input, 'r', encoding='utf-8') as file:
            return file.read()

    def solve_p1(self):
        """
        Solver for Part 1

        This rope bridge creaks as you walk along it.
        You aren't sure how old it is, or whether it can even support your weight.

        It seems to support the Elves just fine, though. The bridge spans a gorge
        which was carved out by the massive river far below you.

        You step carefully; as you do, the ropes stretch and twist.
        You decide to distract yourself by modeling rope physics;
        maybe you can even figure out where not to step.

        Consider a rope with a knot at each end; these knots mark the head
        and the tail of the rope. If the head moves far enough away from the tail,
        the tail is pulled toward the head.

        you should be able to model the positions of the knots on a two-dimensional grid.
        Then, by following a hypothetical series of motions (your puzzle input)
        for the head, you can determine how the tail will move.

        the rope must be quite short; in fact, the head (H) and tail (T)
        must always be touching (diagonally adjacent and even overlapping both count as touching)

        If the head is ever two steps directly up, down, left, or right from the tail,
        the tail must also move one step in that direction so it remains close enough

        Otherwise, if the head and tail aren't touching and aren't in the same row or column,
        the tail always moves one step diagonally to keep up

        Simulate your complete hypothetical series of motions.
        How many positions does the tail of the rope visit at least once?
        """

        for instruction in self.lines:
            line = instruction.strip().split(' ')
            # the instruction is in the form of "<direction> <steps>"
            direction = line[0]
            steps = int(line[1])

            for _ in range(steps):
                # move the head in the specified direction
                self.rope.head = self.rope.move_head(self.rope.head, direction)

                # move the tail in the specified direction
                self.rope.tail = self.rope.move_tail(self.rope.tail, self.rope.head)

        # return the number of positions the tail visits
        return sum(self.tail_grid.values())

    def solve_p2(self):
        """Solver for Part 2"""
        pass

class Rope:
    """A class for modeling a rope"""
    def __init__(self):
        self.head = (0, 0)
        self.tail = (0, 0)
        self.movement_grid = {(0, 0): True}

    def move_head(self, head, direction):
        """Move the head in the specified direction and return the new position"""
        x, y = head

        if direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        elif direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1

        # update the movement grid
        try:
            pass
        except KeyError:
            self.movement_grid[(x, y)] = False

        return x, y

    def move_tail(self, tail, head):
        """
        Move the tail in the specified direction and return the new position
        update the movement grid, to track the positions the tail visits

        If the head is ever two steps directly up, down, left, or right from the tail,
        the tail must also move one step in that direction so it remains close enough

        Otherwise, if the head and tail aren't touching and aren't in the same row or column,
        the tail always moves one step diagonally to keep up
        """
        x, y = tail
        head_x, head_y = head

        # if the head is two steps away from the tail
        if abs(head_x - x) == 2 and head_y == y:
            # move the tail one step in the same direction as the head
            if head_x > x:
                x += 1
            else:
                x -= 1
        elif abs(head_y - y) == 2 and head_x == x:
            # move the tail one step in the same direction as the head
            if head_y > y:
                y += 1
            else:
                y -= 1
        # if the head and tail aren't touching and aren't in the same row or column
        elif abs(head_x - x) > 1 or abs(head_y - y) > 1:
            # move the tail one step diagonally
            if head_x > x:
                x += 1
            else:
                x -= 1
            if head_y > y:
                y += 1
            else:
                y -= 1

        # update the movement grid
        self.movement_grid[(x, y)] = True

        return x, y

    def visulize_grid(self):
        """
        Print the grid of positions the head and tail visit
        
        mark the head with an 'H'
        mark the tail with a 'T'
        and spots that are visited by the tail with a 'x'
        """
        # find the range of the x and y coordinates
        x_min = min(self.movement_grid.keys(), key=lambda x: x[0])[0]
        x_max = max(self.movement_grid.keys(), key=lambda x: x[0])[0]
        y_min = min(self.movement_grid.keys(), key=lambda x: x[1])[1]
        y_max = max(self.movement_grid.keys(), key=lambda x: x[1])[1]

        # print the grid
        for y in range(y_max, y_min - 1, -1):
            for x in range(x_min, x_max + 1):
                if (x, y) == self.head:
                    print('H', end='')
                elif (x, y) == self.tail:
                    print('T', end='')
                elif (x, y) in self.movement_grid:
                    print('x', end='')
                else:
                    print('.', end='')
            print()

if __name__ == '__main__':
    solver = AocSolverDay9('2022/09/input.txt')
    print(f"Solution Part 1: {solver.solve_p1()}")
    # print(f"Solution Part 2: {solver.solve_p2()}")
    # solver.rope.visulize_grid()
