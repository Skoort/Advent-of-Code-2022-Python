from Day02.Choice import Choice
from Shared.Solver import Solver, Part


class Day02Solver(Solver):
    def __init__(self, rounds: list[(Choice, Choice)]):
        self.__rounds = rounds

    def solve(self, part: Part) -> str:
        return str(sum(Day02Solver.__get_round_value(part, round) for round in self.__rounds))

    @staticmethod
    def __get_round_value(part: Part, round: (Choice, Choice)) -> int:
        if part == Part.A:
            return Day02Solver.__get_round_value_a(round)
        else:
            return Day02Solver.__get_round_value_b(round)

    @staticmethod
    def __get_round_value_a(round: (Choice, Choice)) -> int:
        theirs, mine = round
        return Day02Solver.__get_choice_value(mine) + Day02Solver.__get_outcome_value(theirs, mine)

    @staticmethod
    def __get_round_value_b(round: (Choice, Choice)) -> int:
        theirs, mine = round
        if mine == Choice.ROCK:
            # We must lose.
            mine = theirs.get_smaller()
        elif mine == Choice.PAPER:
            # We must tie.
            mine = theirs
        else:
            # We must win.
            mine = theirs.get_greater()

        return Day02Solver.__get_choice_value(mine) + Day02Solver.__get_outcome_value(theirs, mine)

    @staticmethod
    def __get_choice_value(choice: Choice):
        return choice.value + 1

    @staticmethod
    def __get_outcome_value(theirs: Choice, mine: Choice) -> int:
        if mine > theirs:
            return 6
        elif mine == theirs:
            return 3
        else:
            return 0
