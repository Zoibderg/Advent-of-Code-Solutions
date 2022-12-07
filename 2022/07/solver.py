"""
No Moudles
"""
class AocSolverDay7:
    """A class for solving the Advent of Code 2022 Day 7 puzzle"""
    def __init__(self, inputfile):
        self.input = inputfile
        self.data = self.read_input(self.input)
        self.lines = self.data.split('\n')
        # create root directory
        self.root = Directory('/')
        self.current_dir = self.root


    def read_input(self, file):
        """Read the input file"""
        with open(self.input, 'r', encoding='utf-8') as file:
            return file.read()

    def solve_p1(self):
        """
        Solve for Part 1:
        Find all of the directories with a total size of at most 100000.
        What is the sum of the total sizes of those directories?
        """
        for line in self.lines:
            # parse line
            if line.startswith('$'):
                # command
                line = line[1:].strip().split(' ')
                if line[0] == 'cd':
                    # change directory
                    if line[1] == '..':
                        if self.current_dir.parent is not None:
                            self.current_dir = self.current_dir.parent
                        else:
                            self.current_dir = self.root
                    else:
                        for child in self.current_dir.children:
                            if child.key == line[1]:
                                self.current_dir = child
                                break
            else:
                # determine if line is file or directory
                line = line.strip().split(' ')
                if line[0].isnumeric():
                    # file
                    self.current_dir.size += int(line[0])
                    self.current_dir.children.append(File(line[1], int(line[0]), self.current_dir))

                else:
                    # directory
                    self.current_dir.children.append(Directory(line[1], self.current_dir))

        # update all directory sizes to include children
        self.update_dir_size(self.root)

        dirs = self.find_dirs_lesser(self.root, 100000)

        # return sum of sizes
        return sum(dir.size for dir in dirs)

    def update_dir_size(self, directory):
        """update all directory sizes to include children incdluding root"""
        for child in directory.children:
            if child.marker == 'directory':
                self.update_dir_size(child)
                directory.size += child.size

    def find_dirs_lesser(self, directory, size):
        """find all directories with size <= size"""
        dirs = []
        for child in directory.children:
            if child.marker == 'directory':
                if child.size <= size:
                    dirs.append(child)
                dirs += self.find_dirs_lesser(child , size)
        return dirs

    def find_dirs_greater(self, directory, size):
        """find all directories with size >= size"""
        available_space = 70000000 - self.root.size
        dirs = []
        for child in directory.children:
            if child.marker == 'directory':
                if child.size + available_space >= size:
                    dirs.append(child)
                dirs += self.find_dirs_greater(child , size)
        return dirs

    def solve_p2(self):
        """
        Solve for Part 2:

        Now, you're ready to choose a directory to delete.

        The total disk space available to the filesystem is 70000000.
        To run the update, you need unused space of at least 30000000.
        You need to find a directory you can delete
        that will free up enough space to run the update.

        Find the smallest directory that, if deleted,
        would free up enough space on the filesystem to run the update.
        What is the total size of that directory?
        """

        # find all directories with size >= 30000000
        dirs = self.find_dirs_greater(self.root, 30000000)

        # return smallest directory
        return min(dir.size for dir in dirs)

class Directory:
    """Directory class"""
    def __init__(self, key, parent=None):
        self.key = key
        self.marker = 'directory'
        self.size = 0
        self.parent = parent
        self.children = []

class File:
    """File class"""
    def __init__(self, key, size, parent=None):
        self.key = key
        self.marker = 'file'
        self.size = size
        self.parent = parent


if __name__ == '__main__':
    solver = AocSolverDay7('2022/07/input.txt')
    print(f"Solution Part 1: {solver.solve_p1()}")
    print(f"Solution Part 2: {solver.solve_p2()}")
