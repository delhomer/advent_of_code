"""Advent of code 2020, day23, part01
"""


def reorder_cups(draw, new_cup, drop_ref=False):
    resulting_draw = ""
    for idx, item in enumerate(draw):
        if item != new_cup:
            resulting_draw += item
        else:
            start_idx = idx + 1 if drop_ref else idx
            resulting_draw = draw[start_idx:] + resulting_draw
            return resulting_draw


def play_game(draw):
    int_draw = [int(d) for d in draw]
    min_cup = min(int_draw)
    max_cup = max(int_draw)
    for i in range(100):
        current_cup = draw[0]
        picked_cups = draw[1:4]
        ccup = int(current_cup)
        while True:
            ccup -= 1
            destination_cup = str(ccup)
            if ccup < min_cup:
                ccup = max_cup + 1
                continue
            if destination_cup not in picked_cups:
                break
        destination_idx = draw.index(destination_cup) + 1
        draw = draw[0] + draw[4:destination_idx] + draw[1:4] + draw[destination_idx:]
        draw = reorder_cups(draw, new_cup=draw[1])
    return reorder_cups(draw, new_cup="1", drop_ref=True)


def run(input_str, expected_result=None):
    result = play_game(input_str)
    print(
        "Crab cup game result{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("389125467", "67384529")
    run("963275481")
