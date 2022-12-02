from enum import Enum
from functools import total_ordering


@total_ordering
class Choice(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self == Choice.ROCK and other == Choice.PAPER\
            or self == Choice.PAPER and other == Choice.SCISSORS\
            or self == Choice.SCISSORS and other == Choice.ROCK

    def get_greater(self):
        return Choice((self.value + 1) % 3)

    def get_smaller(self):
        return Choice((self.value - 1) % 3)

    @staticmethod
    def parse(text):
        text = text.upper()
        if text == 'A' or text == 'X':
            return Choice.ROCK
        elif text == 'B' or text == 'Y':
            return Choice.PAPER
        elif text == 'C' or text == 'Z':
            return Choice.SCISSORS
        else:
            raise Exception(f'Text "{text}" is not a valid Choice!')


if __name__ == '__main__':
    print('Running Choice.py unit tests.')

    assert Choice.ROCK.value == 0
    assert Choice.PAPER.value == 1
    assert Choice.SCISSORS.value == 2

    assert Choice.ROCK == Choice.ROCK
    assert Choice.PAPER == Choice.PAPER
    assert Choice.SCISSORS == Choice.SCISSORS
    assert Choice.ROCK < Choice.PAPER
    assert Choice.PAPER < Choice.SCISSORS
    assert Choice.SCISSORS < Choice.ROCK
    assert Choice.ROCK > Choice.SCISSORS
    assert Choice.PAPER > Choice.ROCK
    assert Choice.SCISSORS > Choice.PAPER

    assert len(list(Choice)) == 3
    assert all(a == b for a, b in zip(list(Choice), [Choice.ROCK, Choice.PAPER, Choice.SCISSORS]))

    assert Choice.ROCK.get_smaller() == Choice.SCISSORS
    assert Choice.PAPER.get_smaller() == Choice.ROCK
    assert Choice.SCISSORS.get_smaller() == Choice.PAPER
    assert Choice.ROCK.get_greater() == Choice.PAPER
    assert Choice.PAPER.get_greater() == Choice.SCISSORS
    assert Choice.SCISSORS.get_greater() == Choice.ROCK

    assert Choice.parse('A') == Choice.parse('X') == Choice.ROCK
    assert Choice.parse('B') == Choice.parse('Y') == Choice.PAPER
    assert Choice.parse('C') == Choice.parse('Z') == Choice.SCISSORS

    print('Unit tests successful.')
