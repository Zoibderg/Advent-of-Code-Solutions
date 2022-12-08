"""
No Moudles
"""
class AocSolverDay8:
    """A class for solving the Advent of Code 2022 Day 7 puzzle"""
    def __init__(self, inputfile):
        self.input = inputfile
        self.data = self.read_input(self.input)
        self.lines = self.data.split('\n')
        self.trees = {}

        self._build_tree_map()

    def read_input(self, file):
        """Read the input file"""
        with open(self.input, 'r', encoding='utf-8') as file:
            return file.read()

    def solve_p1(self):
        """
        Solver for Part 1

        The expedition comes across a peculiar patch of tall trees
        all planted carefully in a grid. The Elves explain that a
        previous expedition planted these trees as a reforestation effort.
        Now, they're curious if this would be a good location for a tree house.

        First, determine whether there is enough tree cover here
        to keep a tree house hidden. To do this,
        you need to count the number of trees that are visible
        from outside the grid when looking directly along a row or column.

        Each tree is represented as a single digit whose value is its height,
        where 0 is the shortest and 9 is the tallest.

        A tree is visible if all of the other trees between it
        and an edge of the grid are shorter than it.
        Only consider trees in the same row or column;
        that is, only look up, down, left, or right from any given tree.

        All of the trees around the edge of the grid are visible -
        since they are already on the edge, there are no trees to block the view

        Consider your map; how many trees are visible from outside the grid?
        """
        return sum(bool(self.is_visible(x, y)) for x, y in self.trees.items())

    def solve_p2(self):
        """
        Solver for Part 2

        Content with the amount of tree cover available,
        the Elves just need to know the best spot to build their tree house:
        they would like to be able to see a lot of trees.

        To measure the viewing distance from a given tree,
        look up, down, left, and right from that tree;
        stop if you reach an edge or at the first tree
        that is the same height or taller than the tree under consideration.
        (If a tree is right on the edge, at least one of its viewing distances will be zero.)

        A tree's scenic score is found by
        multiplying together its viewing distance in each of the four directions.

        Consider each tree on your map. What is the highest scenic score possible for any tree?
        """
        return max(self.get_tree_scores(x, y) for x, y in self.trees.items())

    def get_tree_scores(self, location, height):
        """
        A tree's scenic score is found by
        multiplying together its viewing distance in each of the four directions
        trees on the edge will have no viewing distance in that direction
        """
        x, y = location
        scoreup, scoredown, scoreleft, scoreright = 0, 0, 0, 0

        # check the top
        for y2 in range(y - 1, -1, -1):
            if self.trees[(x, y2)] >= height:
                scoreup += 1
                break
            scoreup += 1

        # check the bottom
        for y2 in range(y + 1, len(self.lines)):
            if self.trees[(x, y2)] >= height:
                scoredown += 1
                break
            scoredown += 1

        # check the left
        for x2 in range(x - 1, -1, -1):
            if self.trees[(x2, y)] >= height:
                scoreleft += 1
                break
            scoreleft += 1

        # check the right
        for x2 in range(x + 1, len(self.lines[0])):
            if self.trees[(x2, y)] >= height:
                scoreright += 1
                break
            scoreright += 1

        return scoreup * scoredown * scoreleft * scoreright

    def _build_tree_map(self):
        """build the tree map"""""
        for y, line in enumerate(self.lines):
            for x, char in enumerate(line):
                self.trees[(x, y)] = int(char)

    def is_visible(self, location, height):
        """
        Check if a tree is visible from outside the grid
        """
        # get the height of the tree
        x, y = location

        # check the top
        for y2 in range(y - 1, -1, -1):
            if self.trees[(x, y2)] >= height:
                break
        else:
            # print(f"Tree at {x}, {y} is visible from the top")
            return True

        # check the bottom
        for y2 in range(y + 1, len(self.lines)):
            if self.trees[(x, y2)] >= height:
                break
        else:
            # print(f"Tree at {x}, {y} is visible from the bottom")
            return True

        # check the left
        for x2 in range(x - 1, -1, -1):
            if self.trees[(x2, y)] >= height:
                break
        else:
            # print(f"Tree at {x}, {y} is visible from the left")
            return True

        # check the right
        for x2 in range(x + 1, len(self.lines[0])):
            if self.trees[(x2, y)] >= height:
                break
        else:
            # print(f"Tree at {x}, {y} is visible from the right")
            return True

        return False

    def visualize_taller_trees(self):
        """
        Visualize the trees, putting brackets around the visible trees
        """
        for y, line in enumerate(self.lines):
            for x, char in enumerate(line):
                if self.is_visible((x, y), int(char)):
                    print(f"[{char}]", end='')
                else:
                    print(f" {char} ", end='')
            print()

    def visualize_tree_scores(self):
        """
        Visualize the trees, replacing each tree with its score
        """
        for y, line in enumerate(self.lines):
            for x, char in enumerate(line):
                print(f"{self.get_tree_scores((x, y), int(char)):3}", end='')
            print()

if __name__ == '__main__':
    solver = AocSolverDay8('2022/08/input.txt')
    print(f"Solution Part 1: {solver.solve_p1()}")
    print(f"Solution Part 2: {solver.solve_p2()}")
    # solver.visualize_taller_trees()
    # solver.visualize_tree_scores()
