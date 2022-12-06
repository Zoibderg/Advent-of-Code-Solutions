"""
No Moudles
"""

class AocSolverDay2:
    """
    A class for solving the Advent of Code 2022 Day 2 puzzle
    """
    def __init__(self, inputfile):
        self.input = inputfile
        self.lines = self.read_input(self.input)
        self.score = 0
        self.decode = {
            'Rock': ['A', 'X'],
            'Paper': ['B', 'Y'],
            'Scissors': ['C', 'Z']
        }
        self.beats = {
            'Rock': 'Scissors',
            'Paper': 'Rock',
            'Scissors': 'Paper'
        }
        self.points = {
            'Rock': 1,
            'Paper': 2,
            'Scissors': 3,
            'Win': 6,
            'Draw': 3,
            'Lose': 0
        }


    def read_input(self, file):
        """
        Read the input file and return a list of lines
        """
        with open(self.input, 'r', encoding='utf-8') as file:
            return file.readlines()

    def solve_p1(self):
        """
        Solve for part 1:

        Elf gives you an encrypted strategy guide (your puzzle input)
        The first column is what your opponent is going to play:
        A for Rock, B for Paper, and C for Scissors

        The second column is what you should play to beat your opponent:
        X for Rock, Y for Paper, and Z for Scissors

        The winner of the whole tournament is the player with the highest score
        Your total score is the sum of your scores for each round

        The score for a single round is the score for the shape you selected
        1 for Rock, 2 for Paper, and 3 for Scissors

        plus the score for the outcome of the round
        rock beats scissors, sissors beats paper, and paper beats rock
        0 if you lost, 3 if the round was a draw, and 6 if you won

        What would your total score be if everything goes exactly according to your strategy guide?
        """

        # get the total score for each line, keeping track of the score
        # use beats to determine the outcome of the round
        for line in self.lines:
            if line.strip() == '':
                break

            # get the shape for the opponent and the shape for you
            # compencate for the spcae between the two shapes
            opponent = line.strip()[0]
            you = line.strip()[2]

            # decode the opponent and your shapes
            # add the points for the shape you selected
            for shape, code in self.decode.items():
                if opponent == code[0]:
                    opponent = shape

                if you == code[1]:
                    you = shape
                    self.score += self.points[you]
            # print(opponent, you)

            # determine the outcome of the round
            if opponent == you:
                outcome = 'Draw'
            elif self.beats[you] == opponent:
                outcome = 'Win'
            else:
                outcome = 'Lose'
            # print(outcome)

            # determine the score for the round
            self.score += self.points[outcome]

        return self.score

    def solve_p2(self):
        """
        Solve for part 2:
        Our assumptions were wrong and now we need to update our strategy guide

        The first column is what your opponent is going to play
        A for Rock, B for Paper, and C for Scissors

        The second column says how the round needs to end
        X means you need to lose,
        Y means you need to end the round in a draw,
        and Z means you need to win

        Following the Elf's instructions for the second column
        what would your total score be if everything goes exactly according to your strategy guide?
        """

        # reset the score
        self.score = 0

        # adjust decode to the new rules
        self.decode = {
            'Rock': 'A',
            'Paper': 'B',
            'Scissors': 'C',
            'Win': 'Z',
            'Draw': 'Y',
            'Lose': 'X'
        }

        # we already know the outcome of the round
        # so we can just use the decode to get the shape we need to play
        for line in self.lines:
            if line.strip() == '':
                break

            # get the shape for the opponent and the outcome of the round
            # compencate for the spcae between the two shapes
            opponent = line.strip()[0]
            outcome = line.strip()[2]
            you = None

            # decode the opponent and the outcome of the round
            for shape, code in self.decode.items():
                if opponent == code[0]:
                    opponent = shape

                if outcome == code[0]:
                    outcome = shape
            # print(opponent, outcome)

            # determine the shape we need to play to get the desired outcome
            if outcome == 'Draw':
                you = opponent
            elif outcome == 'Win':
                you = self.beats[self.beats[opponent]]
            else:
                you = self.beats[opponent]
            # print(you)

            # determine the score for the round
            # print(self.points[you])
            # print(self.points[outcome])
            # print(self.points[outcome] + self.points[you])
            self.score += (self.points[outcome] + self.points[you])

        return self.score

if __name__ == '__main__':
    solver = AocSolverDay2('02-rock_paper_scissors/input.txt')
    print(f"Solution Part 1: {solver.solve_p1()}")
    print(f"Solution Part 2: {solver.solve_p2()}")
