"""Advent of code 2020, day11, part01
"""

def read_input(filepath):
    with open(filepath, "r") as fobj:
        waiting_area = []
        for line in fobj:
            waiting_area.append(line.strip())
        return waiting_area


def adjacent_seats(warea, x, y):
    if x == 0:
       foreward_seats = ""
    else:
        foreward_seats = warea[x-1][max(0, y-1):min(y+2, len(warea[x]))]
    left_seat = warea[x][y-1] if y > 0 else ""
    right_seat = warea[x][y+1] if y < len(warea[x]) - 1 else ""
    if x == len(warea) - 1:
       backward_seats = ""
    else:
        backward_seats = warea[x+1][max(0, y-1):min(y+2, len(warea[x]))]
    return foreward_seats + left_seat + right_seat + backward_seats


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
                if sum(s == "#" for s in adjacent_seats(warea, i, j)) >= 4:
                    new_range += "L"
                    is_there_any_change = True
                else:
                    new_range += "#"
                    nb_occupied_seats += 1
            elif warea[i][j] == "L":
                if sum(s == "#" for s in adjacent_seats(warea, i, j)) == 0:
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

    run("test_input", 37)
    run("input")
