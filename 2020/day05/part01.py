"""Advent of code 2020, day05, part01
"""

def read_input():
    with open("input", "r") as fobj:
        return fobj.readlines()


def convert_binary_sequence(seq, upper_value):
    return sum(2 ** (len(seq) - idx - 1) for idx, item in enumerate(seq) if item == upper_value)

def compute_seat_id(seat_code):
    assert len(seat_code) == 10
    row_code = seat_code[:7]
    column_code = seat_code[7:]
    row = convert_binary_sequence(row_code, "B")
    column = convert_binary_sequence(column_code, "R")
    return row * 8 + column


if __name__ == "__main__":

    lines = read_input()

    highest_seat_id = 0
    for line in lines:
        line = line.strip()
        seat_id = compute_seat_id(line)
        highest_seat_id = max(highest_seat_id, seat_id)
    print("Highest seat ID: {}".format(highest_seat_id))
