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
        register_cycles = self.cycle_counter(self.lines)

        # get the signal strength for the 20th, 60th, 100th, 140th, 180th, and 220th cycles
        signal_strengths = [self.get_signal_strength(register_cycles, i) for i in range(20, 240, 40)]

        return sum(signal_strengths)
    def cycle_counter(self, instructions):
        """
        Track the cycle number and the value of the X register
        """
        registers = {}
        cycle = 0

        for instruction in instructions:
            line = instruction.strip().split(' ')
            # the instruction is in the form of "<command> <value>"
            command = line[0]
            if command == 'addx':
                cycle += 2
                registers[cycle]= int(line[1])
            elif command == 'noop':
                cycle += 1
            else:
                raise ValueError(f"Unknown instruction: {instruction}")

        return registers

    def get_signal_strength(self, registers, target_cycle):
        """
        Calculate the signal strength
        """
        strength = 1
        for cycle, value in registers.items():
            if cycle < target_cycle:
                strength += value
            else:
                break
        return strength * target_cycle

    def solve_p2(self):
        """Solver for Part 2"""
        pass

if __name__ == '__main__':
    solver = AocSolverDay10('2022/10/input.txt')
    print(f"Solution Part 1: {solver.solve_p1()}")
    # print(f"Solution Part 2: {solver.solve_p2()}")
