"""
No Moudles
"""
class AocSolverDay9:
    """A class for solving the Advent of Code 2022 Day 9 puzzle"""
    def __init__(self, inputfile, knots):
        self.input = inputfile
        self.data = self.read_input(self.input)
        self.lines = self.data.split('\n')

        # create a rope object
        self.rope = Rope(knots)

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

        # create a grid of all the positions the tail of the rope visits
        tail_grid = self.rope.movement_grid

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

            # print("----------------------------------")
            # solver.visualize()

        # return the number of positions the tail visits
        return sum(tail_grid.values())

    def solve_p2(self):
        """
        Solver for Part 2
        
        Rather than two knots, you now must simulate a rope consisting of ten knots.
        One knot is still the head of the rope and moves according to the series of motions.
        Each knot further down the rope follows the knot in front of it using the same rules as before

        Now, you need to keep track of the positions the new tail visits

        Simulate your complete series of motions on a larger rope with ten knots.
        How many positions does the tail of the rope visit at least once?
        """
        # create a grid of all the positions the tail of the rope visits
        tail_grid = self.rope.movement_grid

        for instruction in self.lines:
            line = instruction.strip().split(' ')
            # the instruction is in the form of "<direction> <steps>"
            direction = line[0]
            steps = int(line[1])

            for _ in range(steps):
                # move the head in the specified direction
                self.rope.head = self.rope.move_head(self.rope.head, direction)

                # move the knots in the specified direction
                for knot in self.rope.knots:
                    # print(knot)
                    self.rope.knots[knot] = self.rope.move_knot(knot, self.rope.knots[knot])

            # print("----------------------------------")
            # solver.visualize()

        # return the number of positions the tail visits
        return sum(tail_grid.values())

    def visualize(self):
        """Visualize the grid"""

        # get the min and max x and y values
        min_x = min(self.rope.movement_grid, key=lambda x: x[0])[0]
        max_x = max(self.rope.movement_grid, key=lambda x: x[0])[0]
        min_y = min(self.rope.movement_grid, key=lambda x: x[1])[1]
        max_y = max(self.rope.movement_grid, key=lambda x: x[1])[1]


        for y in range(max_y, min_y - 1, -1):
            for x in range(min_x, max_x + 1):
                if (x, y) == self.rope.head:
                    print("H", end="")
                elif (x, y) == self.rope.tail:
                    print("T", end="")
                elif (x, y) in self.rope.knots.values():
                    print("K", end="")
                else:
                    print(".", end="")
            print()



class Rope:
    """A class for modeling a rope"""
    def __init__(self, knots):
        self.head = (0, 0)
        self.tail = (0, 0)
        self.movement_grid = {(0, 0): True}
        self.knots = {knot: (0, 0) for knot in range(knots - 1)}

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
            if self.movement_grid[(x, y)] == True:
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

    def move_knot(self, knot, position, tail=False):
        """
        the first knot follows the head
        each knot after that follows the knot in front of it
        each knot moves as if it were the tail
        the last knot is the tail
        """
        if knot == 0:
            front_position = self.head
        elif knot == len(self.knots) - 1:
            tail = True
            self.tail = self.knots[knot]
            front_knot = knot - 1
            front_position = self.knots[front_knot]
        else:
            # get the position of the knot in front of it
            front_knot = knot - 1
            front_position = self.knots[front_knot]

        # move the knot
        x, y = position
        front_x, front_y = front_position

        # if the front knot is two steps away from the knot
        if abs(front_x - x) == 2 and front_y == y:
            # move the knot one step in the same direction as the front knot
            if front_x > x:
                x += 1
            else:
                x -= 1
        elif abs(front_y - y) == 2 and front_x == x:
            # move the knot one step in the same direction as the front knot
            if front_y > y:
                y += 1
            else:
                y -= 1
        # if the front knot and knot aren't touching and aren't in the same row or column
        elif abs(front_x - x) > 1 or abs(front_y - y) > 1:
            # move the knot one step diagonally
            if front_x > x:
                x += 1
            else:
                x -= 1
            if front_y > y:
                y += 1
            else:
                y -= 1

        # update the movement grid
        if tail:
            self.movement_grid[(x, y)] = True

        return x, y

if __name__ == '__main__':
    solver = AocSolverDay9('2022/09/input.txt', 10)
    # print(f"Solution Part 1: {solver.solve_p1()}")
    # print(f"Solution Part 2: {solver.solve_p2()}")
