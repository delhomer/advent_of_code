"""Advent of code 2020, day11, part02
"""

def read_input(filepath):
    with open(filepath, "r") as fobj:
        waiting_area = []
        for line in fobj:
            waiting_area.append(line.strip())
        return waiting_area


def visible_seats(warea, x, y):
    visible_seats = ""
    y_ = y
    x_ = x
    while(y_ < len(warea[x]) - 1):  # east
        y_ += 1
        if warea[x][y_] == "#" or warea[x][y_] == "L":
            visible_seats += warea[x][y_]
            break
    y_ = y
    while(y_ > 0):  # west
        y_ -= 1
        if warea[x][y_] == "#" or warea[x][y_] == "L":
            visible_seats += warea[x][y_]
            break
    y_ = y
    while(x_ > 0):  # north
        x_ -= 1
        if warea[x_][y] == "#" or warea[x_][y] == "L":
            visible_seats += warea[x_][y]
            break
    x_ = x
    while(x_ < len(warea) - 1):  # south
        x_ += 1
        if warea[x_][y] == "#" or warea[x_][y] == "L":
            visible_seats += warea[x_][y]
            break
    x_ = x
    while(x_ > 0 and y_ > 0):  # north-west
        x_ -= 1
        y_ -= 1
        if warea[x_][y_] == "#" or warea[x_][y_] == "L":
            visible_seats += warea[x_][y_]
            break
    y_ = y
    x_ = x
    while(x_ > 0 and y_ < len(warea[x]) - 1):  # north-east
        x_ -= 1
        y_ += 1
        if warea[x_][y_] == "#" or warea[x_][y_] == "L":
            visible_seats += warea[x_][y_]
            break
    y_ = y
    x_ = x
    while(x_ < len(warea) - 1 and y_ > 0):  # south-west
        x_ += 1
        y_ -= 1
        if warea[x_][y_] == "#" or warea[x_][y_] == "L":
            visible_seats += warea[x_][y_]
            break
    y_ = y
    x_ = x
    while(x_ < len(warea) - 1 and y_ < len(warea[x]) - 1):  # south-east
        x_ += 1
        y_ += 1
        if warea[x_][y_] == "#" or warea[x_][y_] == "L":
            visible_seats += warea[x_][y_]
            break
    return visible_seats


def switch_seat_status(warea):
    new_warea = []
    is_there_any_change = False
    nb_occupied_seats = 0
    for i in range(len(warea)):
        seat_range = warea[i]
        new_range = ""
        for j in range(len(seat_range)):
            if warea[i][j] == ".":
                new_range += "."
            elif warea[i][j] == "#":
                if sum(s == "#" for s in visible_seats(warea, i, j)) >= 5:
                    new_range += "L"
                    is_there_any_change = True
                else:
                    new_range += "#"
                    nb_occupied_seats += 1
            elif warea[i][j] == "L":
                if sum(s == "#" for s in visible_seats(warea, i, j)) == 0:
                    new_range += "#"
                    nb_occupied_seats += 1
                    is_there_any_change = True
                else:
                    new_range += "L"
        new_warea.append(new_range)
    return new_warea, is_there_any_change, nb_occupied_seats



def run(input_filepath, expected_result=None):
    waiting_area = read_input(input_filepath)
    while(True):
        waiting_area, change, result = switch_seat_status(waiting_area)
        if not change:
            break
    print(
        "Number of occupied seats{}: {}".format(
            "" if expected_result is None else " (test set)", result
        )
    )
    if expected_result:
        assert result == expected_result


if __name__ == "__main__":

    run("test_input", 26)
    run("input")
