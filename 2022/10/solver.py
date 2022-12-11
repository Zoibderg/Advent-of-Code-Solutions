"""
No Moudles
"""
class AocSolverDay10:
    """A class for solving the Advent of Code 2022 Day 10 puzzle"""
    def __init__(self, inputfile):
        self.input = inputfile
        self.data = self.read_input(self.input)
        self.lines = self.data.split('\n')

    def read_input(self, file):
        """Read the input file"""
        with open(self.input, 'r', encoding='utf-8') as file:
            return file.read()

    def solve_p1(self):
        """
        Solver for Part 1

        Start by figuring out the signal being sent by the CPU.
        The CPU has a single register, X, which starts with the value 1.
        It supports only two instructions
        addx V takes two cycles to complete.
        After two cycles, the X register is increased by the value V. (V can be negative.)
        noop takes one cycle to complete. It has no other effect.

        The CPU uses these instructions in a program (your puzzle input) to, somehow,
        tell the screen what to draw.

        Maybe you can learn something by looking at the value of the X register
        throughout execution. For now, consider the signal strength
        (the cycle number multiplied by the value of the X register)
        during the 20th cycle and every 40 cycles after that

        Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
        What is the sum of these six signal strengths?
        """
        # create a CPU object
        cpu = CPU()

        # perfrom all the operations
        cpu.preform_operations(self.lines)

        # return the signal strength
        return cpu.signal_strength

    def solve_p2(self):
        """
        Solver for Part 2
        
        It seems like the X register controls the horizontal position of a sprite.
        Specifically, the sprite is 3 pixels wide, and the X register sets
        the horizontal position of the middle of that sprite.
        In this system, there is no such thing as "vertical position":
        if the sprite's horizontal position puts its pixels where the CRT is currently
        drawing, then those pixels will be drawn.

        You count the pixels on the CRT: 40 wide and 6 high.
        This CRT screen draws the top row of pixels left-to-right,
        then the row below that, and so on.
        The left-most pixel in each row is in position 0, and
        the right-most pixel in each row is in position 39.

        Like the CPU, the CRT is tied closely to the clock circuit: 
        the CRT draws a single pixel during each cycle. 
        Representing each pixel of the screen as a #, here are the cycles 
        during which the first and last pixel in each row are drawn

        So, by carefully timing the CPU instructions and the CRT drawing operations,
        you should be able to determine whether the sprite is visible the instant
        each pixel is drawn. If the sprite is positioned such that one of its three
        pixels is the pixel currently being drawn, the screen produces a lit pixel (#);
        otherwise, the screen leaves the pixel dark (.).
        """
        # create a CRT object
        crt = CTR()

        # draw the screen
        crt.draw_screen(self.lines)

        # print the CRT
        crt.print_crt()

        # return
        return 'See CRT'

class CPU:
    """CLASS FOR REPRESENTING THE CPU"""
    def __init__(self):
        self.x_register = 1
        self.signal_strength = 0
        self.ticks = 0

    def increment_ticks(self):
        """Increment the ticks and add to the signal strength"""""
        self.ticks += 1
        if self.ticks in range(20, 221, 40):
            self.signal_strength += self.x_register * self.ticks

    def execute_instruction(self, instruction):
        """Execute the instruction"""
        line = instruction.strip().split(' ')
        command = line[0]

        if command == 'addx':
            self.increment_ticks()
            self.increment_ticks()
            self.x_register += int(line[1])
        elif command == 'noop':
            self.increment_ticks()

    def preform_operations(self, operations):
        """Preform the operations"""
        for operation in operations:
            self.execute_instruction(operation)

class CTR:
    """CLASS FOR REPRESENTING THE CRT"""
    def __init__(self):
        self.ticks = 0
        self.x_register = 1
        self.crt = ['.' for _ in range(240)]

    def draw_pixel(self, pos):
        """Determines if the pixel is lit or not"""""
        if self.ticks % 40 in [pos-1, pos, pos+1]:
            self.crt[self.ticks] = '#'
        self.ticks += 1

    def execute_instruction(self, instruction):
        """Execute the instruction"""
        line = instruction.strip().split(' ')
        command = line[0]

        if command == 'addx':
            self.draw_pixel(self.x_register)
            self.draw_pixel(self.x_register)
            self.x_register += int(line[1])
        elif command == 'noop':
            self.draw_pixel(self.x_register)

    def draw_screen(self, operations):
        """Draw the screen to the CRT"""
        for operation in operations:
            self.execute_instruction(operation)

    def print_crt(self):
        """Print the CRT"""
        for row in range(6):
            print(''.join(self.crt[row*40:row*40+40]))


if __name__ == '__main__':
    solver = AocSolverDay10('2022/10/input.txt')
    print(f"Solution Part 1: {solver.solve_p1()}")
    print(f"Solution Part 2: {solver.solve_p2()}")
