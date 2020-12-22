"""Advent of code 2020, day22, part01
"""


def read_input(filepath):
    with open(filepath, "r") as fobj:
        decks = fobj.read().split("\n\n")
        return [[int(value) for value in d.split("\n")[1:]] for d in decks]


def play_game(deck1, deck2):
    while len(deck1) > 0 and len(deck2) > 0:
        c1 = deck1.pop(0)
        c2 = deck2.pop(0)
        if c1 > c2:
            deck1 += [c1, c2]
        else:
            deck2 += [c2, c1]
    winner_deck = deck1 if len(deck2) == 0 else deck2
    return sum((len(winner_deck) - idx) * value for idx, value in enumerate(winner_deck))


def run(input_str, expected_result=None):
    deck1, deck2 = read_input(input_str)
    result = play_game(deck1, deck2)
    print(
        "Crab combat winner's score{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 306)
    run("input")
