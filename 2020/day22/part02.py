"""Advent of code 2020, day22, part02
"""

from copy import deepcopy


def read_input(filepath):
    with open(filepath, "r") as fobj:
        decks = fobj.read().split("\n\n")
        return [[int(value) for value in d.split("\n")[1:]] for d in decks]




def play_game(deck1, deck2):
    rounds = {}
    while len(deck1) > 0 and len(deck2) > 0:
        if rounds.get((len(deck1), len(deck2))) is None:
            rounds[(len(deck1), len(deck2))] = []
        if (deck1, deck2) in rounds[(len(deck1), len(deck2))]:
            return deck1, 0
        else:
            rounds[(len(deck1), len(deck2))].append((deck1.copy(), deck2.copy()))
        c1 = deck1.pop(0)
        c2 = deck2.pop(0)
        subwinner_deck_id = None
        if len(deck1) >= c1 and len(deck2) >= c2:
            subwinner_deck, subwinner_deck_id = play_game(
                deepcopy(deck1[:c1]), deepcopy(deck2[:c2])
            )
        if c1 > c2 and subwinner_deck_id is None:
            deck1 += [c1, c2]
        elif c1 < c2 and subwinner_deck_id is None:
            deck2 += [c2, c1]
        elif subwinner_deck_id == 0:
            deck1 += [c1, c2]
        else:
            deck2 += [c2, c1]
    return (deck1, 0) if len(deck2) == 0 else (deck2, 1)


def compute_deck_value(winner_deck):
    return sum((len(winner_deck) - idx) * value for idx, value in enumerate(winner_deck))


def run(input_str, expected_result=None):
    deck1, deck2 = read_input(input_str)
    winner_deck, winner_deck_id = play_game(deck1, deck2)
    result = compute_deck_value(winner_deck)
    print(
        "Crab recursive combat winner's score{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 291)
    run("test_input2")
    run("input")
